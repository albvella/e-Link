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
        offset = 0
        while offset + 6 <= len(data):
            # Leggi metadati
            pressure_size = struct.unpack_from('<H', data, offset)[0]
            flow_size = struct.unpack_from('<H', data, offset+2)[0]
            accel_size = struct.unpack_from('<H', data, offset+4)[0]
            offset += 6
            # Leggi dati compressi
            pressure_bytes = data[offset:offset+pressure_size]
            offset += pressure_size
            flow_bytes = data[offset:offset+flow_size]
            offset += flow_size
            accel_bytes = data[offset:offset+accel_size]
            offset += accel_size
            # Decomprimi
            pressure = self._adpcm_decompress(pressure_bytes, 12)
            flow = self._rle_decompress_flow(flow_bytes)
            ax, ay, az = self._adpcm_decompress_accel(accel_bytes)
            self.measures.append({
                'pressure': pressure,
                'flow': flow,
                'ax': ax,
                'ay': ay,
                'az': az
            })

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
        # Decompressione ADPCM generica
        if bits == 12:
            step_size_table = self._step_size_table_12bit()
        else:
            step_size_table = self._step_size_table_16bit()
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
            for shift in [0, 4]:
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
            idx += 1
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
    compressed_filename = 'data.bin'
    decompressor = eLink_Decompress_Measure(compressed_filename)
    for measure in decompressor.measures:
        print(measure)