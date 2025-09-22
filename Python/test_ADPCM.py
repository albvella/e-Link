import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt

# --- Tabelle ADPCM (IMA standard, come suggerito) ---
step_size_table = [
    1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4,
    4, 5, 5, 6, 6, 7, 8, 8, 9, 10, 11, 12, 13, 15, 16, 18,
    20, 22, 24, 26, 29, 32, 35, 38, 42, 46, 51, 56, 62, 68, 75, 83,
    91, 100, 110, 121, 133, 146, 160, 176, 193, 212, 233, 256, 281, 308, 337, 369,
    404, 442, 483, 528, 577, 630, 688, 751, 819, 893, 974, 1062, 1157, 1261, 1373, 1499,
    1629, 1682, 1850, 2035, 2238, 2462, 2709, 2979
]
index_adjustment_table = [-1, -1, -1, -1, 2, 4, 6, 8]

class AdpcmState:
    def __init__(self, prev=0, idx=0):
        self.previous_value = prev
        self.step_index = idx

def adpcm_compress(data):
    state = AdpcmState(int(data[0]), 0)
    compressed = [int(data[0])] # primo campione non compresso
    packed_byte = None
    for i in range(1, len(data)):
        diff = int(data[i]) - state.previous_value
        step = step_size_table[state.step_index]
        nibble = 0
        if diff < 0:
            nibble = 8
            diff = -diff
        temp = diff * 4
        if temp < step:
            nibble |= 0
        else:
            nibble |= min(7, temp // step)
        # Ricostruzione per predizione
        reconstructed_diff = (step * (nibble & 7)) // 4 + step // 8
        if nibble & 8:
            reconstructed_diff = -reconstructed_diff
        state.previous_value += reconstructed_diff
        state.previous_value = max(-32768, min(32767, state.previous_value))
        state.step_index += index_adjustment_table[nibble & 7]
        state.step_index = max(0, min(87, state.step_index))
        # Packing
        if packed_byte is None:
            packed_byte = nibble
        else:
            packed_byte |= (nibble << 4)
            compressed.append(packed_byte)
            packed_byte = None
    if packed_byte is not None:
        compressed.append(packed_byte)
    return compressed

def adpcm_decompress(compressed):
    state = AdpcmState(int(compressed[0]), 0)
    decompressed = [state.previous_value]
    for byte in compressed[1:]:
        for shift in [0, 4]:
            nibble = (byte >> shift) & 0xF
            step = step_size_table[state.step_index]
            reconstructed_diff = (step * (nibble & 7)) // 4 + step // 8
            if nibble & 8:
                reconstructed_diff = -reconstructed_diff
            state.previous_value += reconstructed_diff
            state.previous_value = max(-32768, min(32767, state.previous_value))
            state.step_index += index_adjustment_table[nibble & 7]
            state.step_index = max(0, min(87, state.step_index))
            decompressed.append(state.previous_value)
    return decompressed[:len(decompressed)-1] # rimuove l'ultimo campione extra

def load_data():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Seleziona file xlsx o python", filetypes=[("Excel files", "*.xlsx"), ("Python files", "*.py")])
    if file_path.endswith('.xlsx'):
        # Leggi solo la colonna B del foglio 'Dati'
        df = pd.read_excel(file_path, sheet_name='Dati', usecols='B')
        col_name = df.columns[0]
        # Normalizza i float tra 0 e 65535, preservando l'andamento
        col_data = df[col_name].dropna().values
        # Rimappa: 0 -> 0, 6 -> 4096
        min_val = 0.0
        max_val = 6.0
        col_data = np.clip(col_data, min_val, max_val)
        data = ((col_data - min_val) / (max_val - min_val) * 4095).astype(np.uint16)
    elif file_path.endswith('.py'):
        # Cerca una variabile chiamata 'pressure_data' nel file python
        import importlib.util
        spec = importlib.util.spec_from_file_location("user_module", file_path)
        user_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(user_module)
        if hasattr(user_module, 'pressure_data'):
            data = np.array(user_module.pressure_data, dtype=int)
        else:
            raise ValueError("Nel file python deve esserci una variabile 'pressure_data'.")
    else:
        raise ValueError("Formato file non supportato.")
    return data

def main():
    data = load_data()
    block_size = 200
    num_blocks = len(data) // block_size
    for i in range(num_blocks):
        block = data[i*block_size:(i+1)*block_size]
        print(f"\nBlocco {i+1}:")
        print(f"  Lunghezza dati originali: {len(block)*2} byte")
        compressed = adpcm_compress(block)
        print(f"  Lunghezza dati compressi: {len(compressed)} byte")
        decompressed = adpcm_decompress(compressed)
        plt.figure(figsize=(10,5))
        plt.plot(block, label='Originale')
        plt.plot(decompressed, label='Decompressa', alpha=0.7)
        plt.legend()
        plt.title(f'Blocco {i+1}: ADPCM Compressione/Decompressione')
        plt.show()
    # Se ci sono dati residui, processali
    if len(data) % block_size != 0:
        block = data[num_blocks*block_size:]
        print(f"\nBlocco finale:")
        print(f"  Lunghezza dati originali: {len(block)*2} byte")
        compressed = adpcm_compress(block)
        print(f"  Lunghezza dati compressi: {len(compressed)} byte")
        decompressed = adpcm_decompress(compressed)
        plt.figure(figsize=(10,5))
        plt.plot(block, label='Originale')
        plt.plot(decompressed, label='Decompressa', alpha=0.7)
        plt.legend()
        plt.title('Blocco finale: ADPCM Compressione/Decompressione')
        plt.show()

if __name__ == "__main__":
    main()
