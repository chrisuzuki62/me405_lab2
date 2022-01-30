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
    s_port.write(b"teststring\r")
    print ("Already wrote through serial port")
    
    data = s_port.readlines()
    
    