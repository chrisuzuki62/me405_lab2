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
from matplotlib import pyplot

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

    gain = input("Please input the desired gain: ")
    s_port.write(b'teststring\r')
    
    start_time = time.time()
    
    while time.time() < start_time + 5:
        pass
    
    bool = True
    data = []
    
    while bool:
        temp = s_port.readline()
        if temp == b'DATA\r\n':
            bool = False
            break
        else:
            data.append(temp.decode())
            
    print(data)
    
    
    
'''
    x = []
    y = []
    for values in data:
        #number = values.split(b',')
        if is_number(values[0].strip()) and is_number(values[1].strip()) :  
            x.append(float(values[0].strip()))
            y.append(float(values[1].strip()))
        else:
            pass

    pyplot.plot(x,y,'bo')
    pyplot.xlabel('X Value (Units)')
    pyplot.ylabel('Y Value (Units)')
 '''
