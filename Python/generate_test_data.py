#!/usr/bin/env python3
"""
Generate sample binary data in the 566-byte padded format
for testing the decompression algorithm.
"""

import struct
import random

def generate_test_data(filename, num_blocks=5):
    """Generate test data with 566-byte padded blocks."""
    
    block_size = 566
    
    with open(filename, 'wb') as f:
        for block_num in range(num_blocks):
            # Generate random but reasonable metadata sizes
            pressure_size = random.randint(50, 150)   # ADPCM compressed pressure data
            flow_size = random.randint(20, 100)      # RLE compressed flow data  
            accel_size = random.randint(100, 300)    # ADPCM compressed accelerometer data
            
            # Calculate total content size
            total_content = 6 + pressure_size + flow_size + accel_size
            
            # Ensure it fits in 566 bytes (leave room for padding)
            if total_content > block_size:
                # Reduce sizes proportionally
                scale = (block_size - 6) / (pressure_size + flow_size + accel_size)
                pressure_size = int(pressure_size * scale * 0.9)  # Leave some margin
                flow_size = int(flow_size * scale * 0.9)
                accel_size = int(accel_size * scale * 0.9)
                total_content = 6 + pressure_size + flow_size + accel_size
            
            padding_size = block_size - total_content
            
            print(f"Block {block_num + 1}: pressure={pressure_size}, flow={flow_size}, "
                  f"accel={accel_size}, padding={padding_size}")
            
            # Write metadata (6 bytes)
            f.write(struct.pack('<H', pressure_size))   # 2 bytes
            f.write(struct.pack('<H', flow_size))       # 2 bytes  
            f.write(struct.pack('<H', accel_size))      # 2 bytes
            
            # Write dummy compressed data (pressure)
            for _ in range(pressure_size):
                f.write(bytes([random.randint(0, 255)]))
            
            # Write dummy compressed data (flow)
            for _ in range(flow_size):
                f.write(bytes([random.randint(0, 255)]))
            
            # Write dummy compressed data (acceleration)
            for _ in range(accel_size):
                f.write(bytes([random.randint(0, 255)]))
            
            # Write zero padding to reach 566 bytes
            f.write(b'\x00' * padding_size)
    
    print(f"\nGenerated {filename} with {num_blocks} blocks of {block_size} bytes each")
    print(f"Total file size: {num_blocks * block_size} bytes")

def main():
    """Generate test data."""
    test_filename = "test_data_566.bin"
    generate_test_data(test_filename, num_blocks=10)
    
    print(f"\nTest file '{test_filename}' created successfully!")
    print("You can now test the decompression with:")
    print(f"python test_decompression.py {test_filename}")

if __name__ == "__main__":
    main()