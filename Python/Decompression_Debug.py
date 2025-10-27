import struct
from typing import List

class eLink_Decompress_Measure:
    def __init__(self, bin_path: str):
        self.bin_path = bin_path
        self.measures = []
        self._decompress_file()

    def _decompress_file(self):
        with open(self.bin_path, 'rb') as f:
            data = f.read()

        self.pressure_data = []
        self.flow_data = []
        self.ax_data = []
        self.ay_data = []
        self.az_data = []
        
        offset = 0
        block_count = 0
        
        while offset < len(data) - 6:
            # ✅ CERCA IL PROSSIMO HEADER VALIDO
            found_header = False
            search_start = offset
            
            # Cerca entro i prossimi 10 bytes per un header valido
            for test_offset in range(search_start, min(search_start + 10, len(data) - 6)):
                metadata = data[test_offset:test_offset+6]
                pressure_size = struct.unpack_from('<H', metadata, 0)[0]
                flow_size = struct.unpack_from('<H', metadata, 2)[0]
                accel_size = struct.unpack_from('<H', metadata, 4)[0]
                
                # ✅ HEADER VALIDO TROVATO
                if (pressure_size == 101 and 
                    0 < flow_size < 50 and 
                    0 < accel_size < 500):
                    
                    if test_offset != search_start:
                        print(f"🔧 Adjusted offset from {search_start} to {test_offset} (skipped {test_offset - search_start} bytes)")
                    
                    offset = test_offset
                    found_header = True
                    break
            
            if not found_header:
                print(f"❌ No valid header found starting from offset {search_start}")
                break
            
            # Leggi metadata
            metadata = data[offset:offset+6]
            pressure_size = struct.unpack_from('<H', metadata, 0)[0]
            flow_size = struct.unpack_from('<H', metadata, 2)[0]
            accel_size = struct.unpack_from('<H', metadata, 4)[0]
            
            # Calcola dimensione blocco
            expected_data_size = 6 + pressure_size + flow_size + accel_size
            
            # Verifica che ci siano abbastanza dati
            if offset + expected_data_size > len(data):
                print(f"Not enough data for block at offset {offset}")
                break
            
            # Leggi blocco
            block_data = data[offset:offset + expected_data_size]
            
            print(f"Block {block_count}: offset={offset}, size={expected_data_size}, pressure={pressure_size}, flow={flow_size}, accel={accel_size}")
            
            # Estrai dati compressi
            data_start = 6
            pressure_bytes = block_data[data_start:data_start + pressure_size]
            data_start += pressure_size
            
            flow_bytes = block_data[data_start:data_start + flow_size]
            data_start += flow_size
            
            accel_bytes = block_data[data_start:data_start + accel_size]
            
            # Decomprimi
            try:
                pressure = self._adpcm_decompress(pressure_bytes, 12)
                flow = self._rle_decompress_flow(flow_bytes)
                ax, ay, az = self._adpcm_decompress_accel(accel_bytes)
                
                self.pressure_data.extend(pressure)
                self.flow_data.extend(flow)
                self.ax_data.extend(ax)
                self.ay_data.extend(ay)
                self.az_data.extend(az)
                
            except Exception as e:
                print(f"❌ Decompression error in block {block_count}: {e}")
                break
            
            # Avanza al prossimo blocco
            offset += expected_data_size
            block_count += 1
        
        print(f"\n✅ Successfully processed {block_count} blocks")
        print(f"Total samples: pressure={len(self.pressure_data)}, flow={len(self.flow_data)}, accel={len(self.ax_data)}")

    def _rle_decompress_flow(self, comp_bytes: bytes) -> List[int]:
            # Decompressione RLE per dati di flusso (uint32_t)
            out = []
            idx = 0
            while idx + 5 <= len(comp_bytes):
                value = struct.unpack_from('<I', comp_bytes, idx)[0]
                run_len = comp_bytes[idx+4]
                out.extend([value] * run_len)
                idx += 5
            return out

    def _adpcm_decompress(self, comp_bytes: bytes, bits: int) -> List[int]:
        if len(comp_bytes) < 2:
            return []
            
        print(f"\n=== ADPCM DEBUG (bits={bits}) ===")
        print(f"Input bytes: {len(comp_bytes)}")
        print(f"First 10 bytes: {comp_bytes[:10].hex()}")
        print(f"Last 10 bytes: {comp_bytes[-10:].hex()}")
        
        if bits == 12:
            step_size_table = self._step_size_table_12bit()
        else:
            step_size_table = self._step_size_table_16bit()
        index_adjustment_table = [-1, -1, -1, -1, 2, 4, 6, 8]
        out = []
        step_index = 0
        
        # Valore iniziale (primi 2 bytes)
        if bits == 12:
            prev = struct.unpack_from('<H', comp_bytes, 0)[0]
        else:
            prev = struct.unpack_from('<h', comp_bytes, 0)[0]
            
        out.append(prev)
        print(f"Initial value: {prev}")
        
        # ✅ CALCOLO CORRETTO BASATO SUL FIRMWARE
        # Se PRESS_HALF_SAMPLES = 200:
        # - Campione 0: non compresso (già aggiunto)  
        # - Campioni 1-199: 199 campioni compressi
        # - 199 nibbles → ceil(199/2) = 100 bytes (ultimo byte ha solo nibble basso)
        
        compressed_data_bytes = len(comp_bytes) - 2  # 99 o 100 bytes
        expected_compressed_samples = 199  # Sempre 199 campioni compressi
        expected_total_samples = 200       # 1 iniziale + 199 compressi
        
        print(f"Compressed data bytes: {compressed_data_bytes}")
        print(f"Expected compressed samples: {expected_compressed_samples}")
        print(f"Expected total samples: {expected_total_samples}")
        
        # ✅ PROCESSA I NIBBLES CON GESTIONE DELL'ULTIMO BYTE DISPARI
        processed_samples = 0
        nibble_count = 0  # Conta i nibbles processati
        
        for idx in range(2, len(comp_bytes)):
            byte = comp_bytes[idx]
            
            if idx < 7 or idx >= len(comp_bytes) - 5:
                print(f"Processing byte {idx}: 0x{byte:02x}")
            
            # ✅ PRIMO NIBBLE (bits 0-3) - SEMPRE PRESENTE
            if processed_samples < expected_compressed_samples:
                nibble = byte & 0xF
                sign = nibble & 8
                delta = nibble & 7
                step = step_size_table[step_index]
                diff = (step * delta) // 4 + step // 8
                if sign:
                    diff = -diff
                prev = prev + diff
                
                if bits == 12:
                    prev = max(0, min(4095, prev))
                else:
                    prev = max(-32768, min(32767, prev))
                
                out.append(prev)
                processed_samples += 1
                nibble_count += 1
                step_index += index_adjustment_table[delta]
                step_index = max(0, min(87, step_index))
                
                if processed_samples >= expected_compressed_samples:
                    print(f"Reached target samples after nibble {nibble_count}")
                    break
            
            # ✅ SECONDO NIBBLE (bits 4-7) - SOLO SE NON È L'ULTIMO BYTE DISPARI
            if processed_samples < expected_compressed_samples:
                # ✅ CONTROLLA SE QUESTO È L'ULTIMO BYTE E SE È DISPARI
                is_last_byte = (idx == len(comp_bytes) - 1)
                remaining_samples = expected_compressed_samples - processed_samples
                
                if is_last_byte and remaining_samples == 1:
                    # Ultimo byte con solo nibble basso utilizzato
                    print(f"Skipping high nibble of last byte {idx} (only low nibble used)")
                    break
                
                nibble = (byte >> 4) & 0xF
                sign = nibble & 8
                delta = nibble & 7
                step = step_size_table[step_index]
                diff = (step * delta) // 4 + step // 8
                if sign:
                    diff = -diff
                prev = prev + diff
                
                if bits == 12:
                    prev = max(0, min(4095, prev))
                else:
                    prev = max(-32768, min(32767, prev))
                
                out.append(prev)
                processed_samples += 1
                nibble_count += 1
                step_index += index_adjustment_table[delta]
                step_index = max(0, min(87, step_index))
                
                if processed_samples >= expected_compressed_samples:
                    print(f"Reached target samples after nibble {nibble_count}")
                    break
        
        print(f"Processed compressed samples: {processed_samples}")
        print(f"Total nibbles processed: {nibble_count}")
        print(f"Output samples: {len(out)}")
        print(f"First 10 values: {out[:10]}")
        print(f"Last 10 values: {out[-10:]}")
        
        if len(out) == expected_total_samples:
            print(f"✅ PERFECT! Got expected {len(out)} samples")
        else:
            print(f"⚠️  Expected {expected_total_samples}, got {len(out)}")
            
            # ✅ Se manca 1 campione, probabilmente è l'ultimo nibble
            while len(out) < expected_total_samples:
                out.append(prev)  # Duplica l'ultimo valore
                print(f"Added missing sample: {prev}")
        
        return out

    def _adpcm_decompress_accel(self, comp_bytes: bytes):
        # Decompressione accelerometro: restituisce tre array ax, ay, az
        step_size_table = self._step_size_table_16bit()
        index_adjustment_table = [-1, -1, -1, -1, 2, 4, 6, 8]
        ax, ay, az = [], [], []
        idx = 0
        # Primo pacchetto non compresso (7 bytes)
        if len(comp_bytes) < 7:
            return ax, ay, az
        raw = comp_bytes[:7]
        # Interpretazione come signed per accelerometro 16-bit
        x = struct.unpack_from('<h', raw, 1)[0]
        y = struct.unpack_from('<h', raw, 3)[0]
        z = struct.unpack_from('<h', raw, 5)[0]
        ax.append(x)
        ay.append(y)
        az.append(z)
        idx = 7
        # Stati ADPCM
        x_state = {'prev': x, 'step_index': 0}
        y_state = {'prev': y, 'step_index': 0}
        z_state = {'prev': z, 'step_index': 0}
        while idx + 2 <= len(comp_bytes):
            b1 = comp_bytes[idx]
            b2 = comp_bytes[idx+1]
            # X
            nibble_x = b1 & 0xF
            sign = nibble_x & 8
            delta = nibble_x & 7
            step = step_size_table[x_state['step_index']]
            diff = (step * delta) // 4 + step // 8
            if sign:
                diff = -diff
            x_state['prev'] = x_state['prev'] + diff
            # CLAMP per 16-bit signed accelerometro
            x_state['prev'] = max(-32768, min(32767, x_state['prev']))
            x_state['step_index'] += index_adjustment_table[delta]
            x_state['step_index'] = max(0, min(87, x_state['step_index']))
            ax.append(x_state['prev'])
            # Y
            nibble_y = (b1 >> 4) & 0xF
            sign = nibble_y & 8
            delta = nibble_y & 7
            step = step_size_table[y_state['step_index']]
            diff = (step * delta) // 4 + step // 8
            if sign:
                diff = -diff
            y_state['prev'] = y_state['prev'] + diff
            # CLAMP per 16-bit signed accelerometro
            y_state['prev'] = max(-32768, min(32767, y_state['prev']))
            y_state['step_index'] += index_adjustment_table[delta]
            y_state['step_index'] = max(0, min(87, y_state['step_index']))
            ay.append(y_state['prev'])
            # Z
            nibble_z = b2 & 0xF
            sign = nibble_z & 8
            delta = nibble_z & 7
            step = step_size_table[z_state['step_index']]
            diff = (step * delta) // 4 + step // 8
            if sign:
                diff = -diff
            z_state['prev'] = z_state['prev'] + diff
            # CLAMP per 16-bit signed accelerometro
            z_state['prev'] = max(-32768, min(32767, z_state['prev']))
            z_state['step_index'] += index_adjustment_table[delta]
            z_state['step_index'] = max(0, min(87, z_state['step_index']))
            az.append(z_state['prev'])
            idx += 2
        return ax, ay, az

    def _step_size_table_16bit(self):
        return [7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 19, 21, 23, 25, 28, 31,
            34, 37, 41, 45, 50, 55, 60, 66, 73, 80, 88, 97, 107, 118, 130, 143,
            157, 173, 190, 209, 230, 253, 279, 307, 337, 371, 408, 449, 494, 544, 598, 658,
            724, 796, 876, 963, 1060, 1166, 1282, 1411, 1552, 1707, 1878, 2066, 2272, 2499, 2749, 3024,
            3327, 3660, 4026, 4428, 4871, 5358, 5894, 6484, 7132, 7845, 8630, 9493, 10442, 11487, 12635, 13899,
            15289, 16818, 18500, 20350, 22385, 24623, 27086, 29794]

    def _step_size_table_12bit(self):
        return [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4,
            4, 5, 5, 6, 6, 7, 8, 8, 9, 10, 11, 12, 13, 15, 16, 18,
            20, 22, 24, 26, 29, 32, 35, 38, 42, 46, 51, 56, 62, 68, 75, 83,
            91, 100, 110, 121, 133, 146, 160, 176, 193, 212, 233, 256, 281, 308, 337, 369,
            404, 442, 483, 528, 577, 630, 688, 751, 819, 893, 974, 1062, 1157, 1261, 1373, 1499,
            1629, 1682, 1850, 2035, 2238, 2462, 2709, 2979]


if __name__ == "__main__":
    compressed_filename = 'C:/Users/albve/STM32CubeIDE/workspace_1.6.1/Smart_Joint/Python/251024_1333_comp.bin'
    
    # ✅ DEBUG: Limita ai primi 3 blocchi per vedere l'output chiaramente
    class DebugDecompressor(eLink_Decompress_Measure):
        def _decompress_file(self):
            # Copia il codice originale ma aggiungi limite
            with open(self.bin_path, 'rb') as f:
                data = f.read()

            self.pressure_data = []
            self.flow_data = []
            self.ax_data = []
            self.ay_data = []
            self.az_data = []
            
            offset = 0
            block_count = 0
            max_blocks = 3  # ✅ DEBUG: Solo primi 3 blocchi
            
            while offset < len(data) - 6 and block_count < max_blocks:
                # ... resto del codice uguale ...
                found_header = False
                search_start = offset
                
                for test_offset in range(search_start, min(search_start + 10, len(data) - 6)):
                    metadata = data[test_offset:test_offset+6]
                    pressure_size = struct.unpack_from('<H', metadata, 0)[0]
                    flow_size = struct.unpack_from('<H', metadata, 2)[0]
                    accel_size = struct.unpack_from('<H', metadata, 4)[0]
                    
                    if (pressure_size == 101 and 
                        0 < flow_size < 50 and 
                        0 < accel_size < 500):
                        
                        if test_offset != search_start:
                            print(f"🔧 Adjusted offset from {search_start} to {test_offset}")
                        
                        offset = test_offset
                        found_header = True
                        break
                
                if not found_header:
                    break
                
                metadata = data[offset:offset+6]
                pressure_size = struct.unpack_from('<H', metadata, 0)[0]
                flow_size = struct.unpack_from('<H', metadata, 2)[0]
                accel_size = struct.unpack_from('<H', metadata, 4)[0]
                expected_data_size = 6 + pressure_size + flow_size + accel_size
                
                if offset + expected_data_size > len(data):
                    break
                
                block_data = data[offset:offset + expected_data_size]
                print(f"\n📦 BLOCK {block_count}: offset={offset}, pressure_size={pressure_size}")
                
                data_start = 6
                pressure_bytes = block_data[data_start:data_start + pressure_size]
                data_start += pressure_size
                
                flow_bytes = block_data[data_start:data_start + flow_size]
                data_start += flow_size
                
                accel_bytes = block_data[data_start:data_start + accel_size]
                
                try:
                    pressure = self._adpcm_decompress(pressure_bytes, 12)
                    print(f"✅ Block {block_count} pressure decompressed: {len(pressure)} samples")
                    
                    flow = self._rle_decompress_flow(flow_bytes)
                    ax, ay, az = self._adpcm_decompress_accel(accel_bytes)
                    
                    self.pressure_data.extend(pressure)
                    self.flow_data.extend(flow)
                    self.ax_data.extend(ax)
                    self.ay_data.extend(ay)
                    self.az_data.extend(az)
                    
                except Exception as e:
                    print(f"❌ Decompression error in block {block_count}: {e}")
                    break
                
                offset += expected_data_size
                block_count += 1
            
            print(f"\n=== SUMMARY ===")
            print(f"Processed blocks: {block_count}")
            print(f"Total pressure samples: {len(self.pressure_data)}")
            print(f"Expected pressure samples: {block_count * 200}")
            print(f"Samples per block: {len(self.pressure_data) / block_count if block_count > 0 else 0}")
    
    decompressor = DebugDecompressor(compressed_filename)