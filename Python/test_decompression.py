#!/usr/bin/env python3
"""
Test script for the modified eLink_Decompress_Measure class
to handle 566-byte padded data blocks.
"""

import sys
import os

# Add the directory containing the module to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from eLink_Decompress_Measure import eLink_Decompress_Measure

def test_decompression(binary_file_path):
    """Test the decompression with padded 566-byte blocks."""
    
    if not os.path.exists(binary_file_path):
        print(f"Error: Binary file '{binary_file_path}' not found.")
        return False
    
    print(f"Testing decompression of: {binary_file_path}")
    print(f"File size: {os.path.getsize(binary_file_path)} bytes")
    
    try:
        # Initialize the decompressor
        decompressor = eLink_Decompress_Measure(binary_file_path)
        
        print(f"\nSuccessfully parsed {len(decompressor.measures)} measurement blocks")
        
        # Display first few measurements for verification
        for i, measure in enumerate(decompressor.measures[:3]):
            print(f"\nMeasurement {i+1}:")
            print(f"  Pressure samples: {len(measure['pressure'])}")
            print(f"  Flow samples: {len(measure['flow'])}")
            print(f"  Acceleration samples: {len(measure['ax'])}")
            
            # Show some sample values
            if measure['pressure']:
                print(f"  Pressure range: {min(measure['pressure'])} - {max(measure['pressure'])}")
            if measure['flow']:
                print(f"  Flow range: {min(measure['flow'])} - {max(measure['flow'])}")
            if measure['ax']:
                print(f"  Accel X range: {min(measure['ax'])} - {max(measure['ax'])}")
        
        return True
        
    except Exception as e:
        print(f"Error during decompression: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Main test function."""
    
    # Check if binary file path is provided
    if len(sys.argv) != 2:
        print("Usage: python test_decompression.py <path_to_binary_file>")
        print("Example: python test_decompression.py data.bin")
        return
    
    binary_file = sys.argv[1]
    success = test_decompression(binary_file)
    
    if success:
        print("\n✅ Decompression test completed successfully!")
    else:
        print("\n❌ Decompression test failed!")

if __name__ == "__main__":
    main()