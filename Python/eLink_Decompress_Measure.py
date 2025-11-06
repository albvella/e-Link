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
        self.flow_valid_counts = []
        self.ax_data = []
        self.ay_data = []
        self.az_data = []
        
        offset = 0
        block_count = 0
        
        while offset < len(data) - 6:
            # ✅ CERCA IL PROSSIMO HEADER VALIDO (come prima)
            found_header = False
            search_start = offset
            
            # Cerca entro i prossimi 10 bytes per un header valido
            for test_offset in range(search_start, min(search_start + 10, len(data) - 6)):
                metadata = data[test_offset:test_offset+6]
                pressure_size = struct.unpack_from('<H', metadata, 0)[0]
                flow_size = struct.unpack_from('<H', metadata, 2)[0]
                accel_size = struct.unpack_from('<H', metadata, 4)[0]
                
                # ✅ HEADER VALIDO CON NUOVE DIMENSIONI
                if (pressure_size == 102 and  # Era 101, ora 102!
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
            
            # Leggi metadata confermato
            metadata = data[offset:offset+6]
            pressure_size = struct.unpack_from('<H', metadata, 0)[0]
            flow_size = struct.unpack_from('<H', metadata, 2)[0]
            accel_size = struct.unpack_from('<H', metadata, 4)[0]
            
            # Calcola dimensione blocco
            expected_data_size = 6 + pressure_size + flow_size + accel_size  # Dovrebbe essere 518
            
            # Verifica che ci siano abbastanza dati
            if offset + expected_data_size > len(data):
                print(f"Not enough data for block at offset {offset}")
                print(f"Expected size: {expected_data_size}, available: {len(data) - offset}")
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
                flow, valid_count = self._get_flow(flow_bytes)
                ax, ay, az = self._adpcm_decompress_accel(accel_bytes)
                
                self.pressure_data.extend(pressure)
                self.flow_data.extend(flow)
                self.flow_valid_counts.append(valid_count)
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

    def _get_flow(self, comp_bytes: bytes) -> tuple[List[int], int]:
        """
        Lettura diretta di un valore uint32_t (NO RLE).
        
        Returns:
            tuple: (lista_con_un_solo_valore, 1)
        """
        if len(comp_bytes) < 4:
            return [0], 1
        
        # Leggi direttamente il valore a 32 bit (little-endian)
        value = struct.unpack_from('<I', comp_bytes, 0)[0]
        
        # Ritorna una lista con un solo valore
        return [value], 1

    def _adpcm_decompress(self, comp_bytes: bytes, bits: int) -> List[int]:
        # Decompressione ADPCM generica
        if bits == 12:
            step_size_table = self._step_size_table_12bit()
            target_samples = 200  # ✅ SEMPRE 200 CAMPIONI PER PRESSIONE
        else:
            step_size_table = self._step_size_table_16bit()
            target_samples = None  # Per accelerometro, processa tutto
            
        index_adjustment_table = [-1, -1, -1, -1, 2, 4, 6, 8]
        out = []
        idx = 0
        step_index = 0
        
        # Valore iniziale - gestione corretta signed/unsigned
        if bits == 12:
            # 12-bit: unsigned (0-4095)
            prev = struct.unpack_from('<H', comp_bytes, 0)[0]
        else:
            # 16-bit: signed (-32768 to +32767)
            prev = struct.unpack_from('<h', comp_bytes, 0)[0]
            
        out.append(prev)
        idx = 2
        
        while idx < len(comp_bytes):
            byte = comp_bytes[idx]
            
            # ✅ GESTIONE SPECIALE PER L'ULTIMO BYTE DELLA PRESSIONE
            if bits == 12 and len(out) == target_samples - 1:
                # Ultimo campione: elabora solo il primo nibble
                nibble = byte & 0xF
                sign = nibble & 8
                delta = nibble & 7
                step = step_size_table[step_index]
                diff = (step * delta) // 4 + step // 8
                if sign:
                    diff = -diff
                prev = prev + diff
                prev = max(0, min(4095, prev))
                out.append(prev)
                break  # ✅ STOP! Abbiamo raggiunto i 200 campioni
            
            # ✅ ELABORAZIONE NORMALE: 2 nibbles per byte
            for shift in [0, 4]:
                # ✅ CONTROLLO CAMPIONI TARGET PER PRESSIONE
                if bits == 12 and target_samples and len(out) >= target_samples:
                    break
                    
                nibble = (byte >> shift) & 0xF
                sign = nibble & 8
                delta = nibble & 7
                step = step_size_table[step_index]
                diff = (step * delta) // 4 + step // 8
                if sign:
                    diff = -diff
                prev = prev + diff
                
                # CLAMP DINAMICO BASATO SUI BITS
                if bits == 12:
                    # Dati 12-bit ADC: unsigned 0-4095
                    prev = max(0, min(4095, prev))
                else:
                    # Dati 16-bit accelerometro: signed -32768 to +32767
                    prev = max(-32768, min(32767, prev))
                
                out.append(prev)
                step_index += index_adjustment_table[delta]
                step_index = max(0, min(87, step_index))
            
            # ✅ CONTROLLO CAMPIONI TARGET PER PRESSIONE
            if bits == 12 and target_samples and len(out) >= target_samples:
                break
                
            idx += 1
        
        return out

    def _adpcm_decompress_accel(self, comp_bytes: bytes):
        # Decompressione accelerometro: restituisce tre array ax, ay, az
        step_size_table = self._step_size_table_16bit()
        index_adjustment_table = [0, 0, 1, 1, 2, 2, 3, 3]
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
        return [16, 17, 19, 20, 21, 23, 25, 27, 29, 31, 33, 36, 39, 42, 45, 48, 52, 56, 60, 65, 69,
                75, 80, 87, 93, 100, 108, 116, 125, 134, 145, 156, 168, 180, 194, 209, 225, 242, 260,
                280, 302, 325, 349, 376, 404, 435, 468, 504, 542, 584, 628, 676, 728, 783, 843, 907, 976,
                1050, 1130, 1216, 1309, 1409, 1516, 1632, 1756, 1890, 2033, 2188, 2355, 2534, 2727, 2935,
                3159, 3399, 3658, 3937, 4237, 4560, 4907, 5281, 5683, 6116, 6581, 7083, 7622, 8203, 8828, 9500]

    def _step_size_table_12bit(self):
        return [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4,
                4, 5, 5, 6, 6, 7, 8, 8, 9, 10, 11, 12, 13, 15, 16, 18,
                20, 22, 24, 26, 29, 32, 35, 38, 42, 46, 51, 56, 62, 68, 75, 83,
                91, 100, 110, 121, 133, 146, 160, 176, 193, 212, 233, 256, 281, 308, 337, 369,
                404, 442, 483, 528, 577, 630, 688, 751, 819, 893, 974, 1062, 1157, 1261, 1373, 1499,
                1629, 1682, 1850, 2035, 2238, 2462, 2709, 2979]


if __name__ == "__main__":
    compressed_filename = 'C:/Users/albve/STM32CubeIDE/workspace_1.6.1/Smart_Joint/Python/251106_1454_comp.bin'
    decompressor = eLink_Decompress_Measure(compressed_filename)

    import matplotlib.pyplot as plt
    import numpy as np

    f = 800
    block_duration = 200 / f  
    press_fullscale = 50  
    t = np.linspace(0, len(decompressor.ax_data) / f, len(decompressor.ax_data))
    
    t_flow = np.linspace(0, len(decompressor.flow_data) / f * 200, len(decompressor.flow_data))

    ax = np.array(decompressor.ax_data) * 0.061 
    ay = np.array(decompressor.ay_data) * 0.061
    az = np.array(decompressor.az_data) * 0.061

    pressure = np.array(decompressor.pressure_data) * press_fullscale / 4096
    
    clock_freq = 80000000
    flow_data = np.array(decompressor.flow_data)
    with np.errstate(divide='ignore', invalid='ignore'):
        flow = np.where(flow_data != 0, clock_freq / flow_data, 0)

    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 10))
    
    ax1.plot(t, pressure, 'b-', linewidth=1)
    ax1.set_title('Pressione', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Pressione [bar]', fontsize=12)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(0, max(t) if len(t) > 0 else 1)

    ax2.plot(t_flow, flow, 'g-', linewidth=1)
    ax2.set_title('Flusso', fontsize=14, fontweight='bold')
    ax2.set_ylabel('Flusso [L/s]', fontsize=12)
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(0, max(t_flow) if len(t_flow) > 0 else 1)
    
    ax3.plot(t, ax, 'r-', label='Ax', linewidth=1)
    ax3.plot(t, ay, 'g-', label='Ay', linewidth=1)
    ax3.plot(t, az, 'b-', label='Az', linewidth=1)
    ax3.set_title('Accelerazioni', fontsize=14, fontweight='bold')
    ax3.set_xlabel('Tempo [s]', fontsize=12)
    ax3.set_ylabel('Accelerazione [mg]', fontsize=12)
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    ax3.set_xlim(0, max(t) if len(t) > 0 else 1)
    
    plt.tight_layout()
    plt.subplots_adjust(hspace=0.3) 
    
    plt.show()