'''!
    @file pc_com.py
    @brief A driver for communicating data from the encoders
    @details This file creates an encoder calss that contains 3 methods that can
             be used in other files to get the change of the position of an
             encoder over time. It contains a construcotr method to instantiate each
             class object. A  get position method that returns the position of the encoder. 
             A zero poistion method that zeroes the position of the encoder to a specifed
             value. 
    @author Damond Li
    @author Chris Or
    @author Chris Suzuki
    @date 1/25/22
'''
import serial
import time
import numpy as np
import matplotlib.pyplot as plt

def is_number(string):
    """!
    @brief   Identifies if the csv value can be converted into a float
    @param   string    The entire csv value to be tested
    """
    try:
        # Try converting the string value to a float value
        float(string)
        # Return boolean true if possible
        return True
    except ValueError:
        # Return boolean false if not possible
        return False


with serial.Serial('COM3', 115200) as s_port:


    while True:
        gain = input("Please input the desired gain: ")
        try:
            float(gain)
            s_port.write(str(gain).encode() + b'\r')
            break
        except ValueError:
            print('Invalid Value')
    
#     while True:    
#         position = input("Please input the desired position: ")
#         try:
#             int(position)
#             s_port.write(str(position).encode() + b'\r')
#             break
#         except ValueError:
#             print('Invalid Value')        
    
    bool = True
    data = []
    
    while bool:
        temp = s_port.readline()
        if temp == b'DATA\r\n':
            bool = False
            break
        else:
            data.append(temp.decode())
            


x = []
y = []


runs = 0

for idx in data:
    if runs != 0:
        p = idx[0:-3].split(',')
        if p[0] != "" and p[1] != "":
            x.append(p[0])
            y.append(p[1])
    runs += 1

#plt.axis([min(x), max(x), min(y), max(y)])
# plt.yticks(np.arange(int(min(y)), int(max(y)) + 1, step = 5, dtype=int))
# plt.xticks(np.arange(int(min(x)), int(max(x)) + 1, step = 10, dtype=int))
plt.xticks(range(int(min(x)),int(max(x)), 10))
plt.yticks(range(int(min(y)),int(max(y)), 10))
plt.plot(x,y)
plt.xlabel('Time (Sec)')
plt.ylabel('Encoder Value (Ticks)')
plt.show()

