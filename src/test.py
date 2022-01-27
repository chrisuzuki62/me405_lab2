"""
ME405: Mechatronics
HW0x00

Written by: Damond Li
"""

# import matplotlib.pyplot as plt
import serial
import struct

with serial.Serial('COM4', 115200) as s_port:
    
    gain = input("Please input the desired gain.")
    value1 = bytearray(struct.pack("f", float(gain)))
    s_port.write(value1)
    
    gain = input("Please input the desired gain.")
    value1 = bytearray(struct.pack("f", float(gain)))
    s_port.write(value1)
    
"""
    # Plot with approprate formatting
    plt.plot(x, y, 'ko')
    plt.xlabel('X Values')
    plt.ylabel('Y Values')
    plt.title('HW0x00 Plot')
    plt.grid()
    plt.show()
"""
    