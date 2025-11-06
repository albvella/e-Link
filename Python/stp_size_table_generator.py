import numpy as np

# Parametri
n_steps = 88
start_value = 16
end_value = 9500

# Interpolazione logaritmica
log_start = np.log(start_value)
log_end = np.log(end_value)

# Genera 88 punti in scala logaritmica
log_values = np.linspace(log_start, log_end, n_steps)
step_size_table = np.round(np.exp(log_values)).astype(int)

# Verifica la lunghezza
print(f"Lunghezza: {len(step_size_table)}")  # Deve essere 88
print("Tabella step size (88 elementi):")
print(step_size_table.tolist())