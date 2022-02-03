"""!
@file       main.py
@brief    Runs the main program and creates all objects to rotate the motor the to desired angle  
@details  This program is to be installed and ran on the MicroPython board. It creates the class
          objects motor, controller, and encoder. The program runs a loop until the user types a
          value into the serial port starting the step response test. The motor will run to the desired
          angle which rely on the encoder and controller feedback to control the motor output.

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


##Create objects
mtr1 = motor.Motor(1)
enc1 = encoder.Encoder(1)
ctr = controller.Controller()

while True:
    try:
        # Enable motor
        mtr1.enable()
        
        # Test code to be used later
        #tempgain = b'0.35\r'
        #input_gain = float(input().decode()[0:-1])
        #print(type(input_gain))
        #ctr.set_gain(tempgain.decode()[0:-1])
        #input_position = int(input().decode()[0:-1])
        
        input()
        ctr.set_gain(0.01)
        ctr.set_position(20000)
        
        # Create empty variables
        ctr.positional_data = []
        time_array = []
        position_array = []
            
        # Start Reference Time
        start_time = time.time()

        while time.time() - start_time < 2:
            power = ctr.step_response(enc1.read())
            mtr1.set_duty_cycle(power)
            utime.sleep_ms(10)
            
        mtr1.disable()
        ctr.get_position()
    
    except KeyboardInterrupt:
        break
   

