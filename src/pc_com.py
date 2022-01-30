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

"""
with serial.Serial('COM4', 115200) as s_port:

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
"""

data = ['teststring\r\n', '0,0 \r\n', '\r\n', '11,129 \r\n', '\r\n', '21,478 \r\n', '\r\n', '31,957 \r\n', '\r\n', '41,1509 \r\n', '\r\n', '51,2105 \r\n', '\r\n', '61,2730 \r\n', '\r\n', '71,3373 \r\n', '\r\n', '81,4028 \r\n', '\r\n', '91,4688 \r\n', '\r\n', '101,5352 \r\n', '\r\n', '111,6021 \r\n', '\r\n', '121,6691 \r\n', '\r\n', '131,7362 \r\n', '\r\n', '141,8035 \r\n', '\r\n', '151,8706 \r\n', '\r\n', '161,9380 \r\n', '\r\n', '171,10055 \r\n', '\r\n', '181,10728 \r\n', '\r\n', '191,11403 \r\n', '\r\n', '201,12077 \r\n', '\r\n', '211,12751 \r\n', '\r\n', '221,13426 \r\n', '\r\n', '231,14101 \r\n', '\r\n', '241,14777 \r\n', '\r\n', '251,15453 \r\n', '\r\n', '261,16108 \r\n', '\r\n', '271,16634 \r\n', '\r\n', '281,16901 \r\n', '\r\n', '291,16896 \r\n', '\r\n', '301,16740 \r\n', '\r\n', '311,16535 \r\n', '\r\n', '321,16348 \r\n', '\r\n', '331,16231 \r\n', '\r\n', '341,16220 \r\n', '\r\n', '351,16256 \r\n', '\r\n', '361,16272 \r\n', '\r\n', '371,16271 \r\n', '\r\n', '381,16271 \r\n', '\r\n', '391,16271 \r\n', '\r\n', '401,16271 \r\n', '\r\n', '411,16271 \r\n', '\r\n', '421,16271 \r\n', '\r\n', '431,16271 \r\n', '\r\n', '441,16271 \r\n', '\r\n', '451,16271 \r\n', '\r\n', '461,16271 \r\n', '\r\n', '471,16271 \r\n', '\r\n', '481,16271 \r\n', '\r\n', '491,16271 \r\n', '\r\n', '501,16271 \r\n', '\r\n', '511,16271 \r\n', '\r\n', '521,16271 \r\n', '\r\n', '531,16271 \r\n', '\r\n', '541,16270 \r\n', '\r\n', '551,16270 \r\n', '\r\n', '561,16270 \r\n', '\r\n', '571,16270 \r\n', '\r\n', '581,16270 \r\n', '\r\n', '591,16270 \r\n', '\r\n', '601,16270 \r\n', '\r\n', '611,16270 \r\n', '\r\n', '621,16270 \r\n', '\r\n', '631,16270 \r\n', '\r\n', '641,16270 \r\n', '\r\n', '651,16270 \r\n', '\r\n', '661,16270 \r\n', '\r\n', '671,16270 \r\n', '\r\n', '681,16270 \r\n', '\r\n', '691,16270 \r\n', '\r\n', '701,16270 \r\n', '\r\n', '711,16270 \r\n', '\r\n', '721,16270 \r\n', '\r\n', '731,16270 \r\n', '\r\n', '741,16270 \r\n', '\r\n', '751,16270 \r\n', '\r\n', '761,16270 \r\n', '\r\n', '771,16270 \r\n', '\r\n', '781,16270 \r\n', '\r\n', '791,16270 \r\n', '\r\n', '801,16270 \r\n', '\r\n', '811,16270 \r\n', '\r\n', '821,16270 \r\n', '\r\n', '831,16270 \r\n', '\r\n', '841,16270 \r\n', '\r\n', '851,16270 \r\n', '\r\n', '861,16270 \r\n', '\r\n', '871,16270 \r\n', '\r\n', '881,16270 \r\n', '\r\n', '891,16270 \r\n', '\r\n', '901,16270 \r\n', '\r\n', '911,16270 \r\n', '\r\n', '921,16270 \r\n', '\r\n', '931,16270 \r\n', '\r\n', '941,16270 \r\n', '\r\n', '951,16270 \r\n', '\r\n', '961,16270 \r\n', '\r\n', '971,16270 \r\n', '\r\n', '981,16270 \r\n', '\r\n', '991,16270 \r\n', '\r\n', '1001,16270 \r\n', '\r\n', '1011,16270 \r\n', '\r\n', '1021,16270 \r\n', '\r\n', '1031,16270 \r\n', '\r\n', '1041,16270 \r\n', '\r\n', '1051,16270 \r\n', '\r\n', '1061,16270 \r\n', '\r\n', '1071,16270 \r\n', '\r\n', '1081,16270 \r\n', '\r\n', '1091,16270 \r\n', '\r\n', '1101,16270 \r\n', '\r\n', '1111,16270 \r\n', '\r\n', '1121,16270 \r\n', '\r\n', '1131,16270 \r\n', '\r\n', '1141,16270 \r\n', '\r\n', '1151,16270 \r\n', '\r\n', '1161,16270 \r\n', '\r\n', '1171,16270 \r\n', '\r\n', '1181,16270 \r\n', '\r\n', '1191,16270 \r\n', '\r\n', '1201,16270 \r\n', '\r\n', '1211,16270 \r\n', '\r\n', '1221,16270 \r\n', '\r\n', '1231,16270 \r\n', '\r\n', '1241,16270 \r\n', '\r\n', '1251,16270 \r\n', '\r\n', '1261,16270 \r\n', '\r\n', '1271,16270 \r\n', '\r\n', '1281,16270 \r\n', '\r\n', '1291,16270 \r\n', '\r\n', '1301,16270 \r\n', '\r\n', '1311,16270 \r\n', '\r\n', '1321,16270 \r\n', '\r\n', '1331,16270 \r\n', '\r\n', '1341,16270 \r\n', '\r\n', '1351,16270 \r\n', '\r\n', '1361,16270 \r\n', '\r\n', '1371,16270 \r\n', '\r\n', '1381,16270 \r\n', '\r\n', '1391,16270 \r\n', '\r\n', '1401,16270 \r\n', '\r\n', '1411,16270 \r\n', '\r\n', '1421,16270 \r\n', '\r\n', '1431,16270 \r\n', '\r\n', '1441,16270 \r\n', '\r\n', '1451,16270 \r\n', '\r\n', '1461,16270 \r\n', '\r\n', '1471,16270 \r\n', '\r\n', '1481,16270 \r\n', '\r\n', '1491,16270 \r\n', '\r\n', '1501,16270 \r\n', '\r\n', '1511,16270 \r\n', '\r\n', '1521,16270 \r\n', '\r\n', '1531,16270 \r\n', '\r\n', '1541,16270 \r\n', '\r\n', '1551,16270 \r\n', '\r\n', '1561,16270 \r\n', '\r\n', '1571,16270 \r\n', '\r\n', '1581,16270 \r\n', '\r\n', '1591,16270 \r\n', '\r\n', '1601,16270 \r\n', '\r\n', '1611,16270 \r\n', '\r\n', '1621,16270 \r\n', '\r\n', '1631,16270 \r\n']

x = []
y = []

#my_str = '11,129999054 \r\n'
#my_str = '\r\n'

#new_str = my_str[0:-3]

runs = 0

for idx in data:
    if runs != 0:
        p = idx[0:-3].split(',')
        if p[0] != "" and p[1] != "":
            x.append(p[0])
            y.append(p[1])
    runs += 1

plt.plot(x,y,'bo')
plt.xlabel('X Value (Units)')
plt.ylabel('Y Value (Units)')
    
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
