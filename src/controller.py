"""!
@file       controller.py
@brief      
@details    

@author Damond Li
@author Chris Or
@author Chris Suzuki
@date   27-Jan-2022 SPL Original file
"""

import pyb
import motor
import encoder
import time
import utime

class Controller:
    '''! 
    @brief      
    @details    
    '''

    def __init__(self):
        '''! 
        @brief      
        @details    
        '''
        self.gain = 0
        self.positional_data = []
        self.start_time = utime.ticks_ms()
        self.offset_time = 0
        self.runs = 1
            
    def update(self, current_position):
        '''! 
        @brief      
        @details    
        '''
        error = self.des_pos - current_position
        output = error * self.gain
        return output
        
        
    def set_gain(self, desired_gain):
        '''! 
        @brief      
        @details    
        '''
        self.gain = desired_gain

    def set_position(self, desired_position):
        '''! 
        @brief      
        @details    
        '''
        self.des_pos = desired_position

    def step_response(self, current_position):
        '''! 
        @brief      
        @details    
        '''
        error = int(self.des_pos) - int(current_position)
        output = error * self.gain
        if self.runs == 1:
            self.offset_time = utime.ticks_diff(utime.ticks_ms(), self.start_time)
                                           
        self.positional_data.append([utime.ticks_diff(utime.ticks_ms(), self.start_time) - self.offset_time, current_position])
        self.runs += 1
        return int(output)
    
    def get_position(self):
        for item in self.positional_data:
           print(str(item[0]) + "," + str(item[1]), "\n")
        print("DATA")
        self.runs = 1
        

if __name__ == '__main__':
    start_time = time.time()
    # Create objects
    mtr1 = motor.Motor(1)
    enc1 = encoder.Encoder(1)
    ctr = Controller()
    
    # Enable motor
    mtr1.enable()
    
    ctr.set_gain(0.1)
    ctr.set_position(16300)
    
    while time.time() - start_time < 2:
        power = ctr.update(enc1.read())
        mtr1.set_duty_cycle(power)
        print(enc1.read())
        
    mtr1.disable()
   
