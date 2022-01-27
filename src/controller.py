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

if __name__ == '__main__':
    start_time = time.time()
    # Create objects
    mtr1 = motor.Motor(1)
    enc1 = encoder.Encoder(1)
    ctr = Controller()
    
    # Enable motor
    mtr1.enable()
    
    ctr.set_gain(0.1)
    ctr.set_position(10000)
    
    while time.time() - start_time < 1:
        power = ctr.update(enc1.read())
        mtr1.set_duty_cycle(power)
        print(enc1.read())
        
    mtr1.disable()
   
