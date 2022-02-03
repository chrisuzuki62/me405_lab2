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


# Create motor, encoder, and controller objects
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
        
        # Wait for an input through the serial port
        input()
        
        # Establish the desired gain and position
        ctr.set_gain(0.01)
        ctr.set_position(20000)
        
        # Reset the list inside the controller class
        ctr.positional_data = []
            
        # Establish reference time
        start_time = time.time()
        
        # Run the step response for two seconds
        while time.time() - start_time < 2:
            
            # Run the controller every 10ms
            power = ctr.step_response(enc1.read())
            mtr1.set_duty_cycle(power)
            utime.sleep_ms(10)
        
        # Disable motor after step response
        mtr1.disable()
        
        # Print data through serial port
        ctr.get_position()
    
    except KeyboardInterrupt:
        break
   

