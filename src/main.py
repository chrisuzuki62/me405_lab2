"""!
@file       main.py
@brief      
@details    

@author Damond Li
@author Chris Or
@author Chris Suzuki
@date   27-Jan-2022 SPL Original file
"""

import pyb
import motor
import controller
import encoder
import utime
import struct
import time

# Create objects
mtr1 = motor.Motor(1)
enc1 = encoder.Encoder(1)
ctr = controller.Controller()

# Enable motor
mtr1.enable()

input_gain = input("")

ctr.set_gain(0.1)
ctr.set_position(16300)

time_array = []
position_array = []
    
# Start Reference Time
start_time = time.time()



while time.time() - start_time < 5:
    power = ctr.step_response(enc1.read())
    mtr1.set_duty_cycle(power)
    utime.sleep_ms(10)
    
ctr.get_position()
   

