"""!
    @file       controller.py
    @brief      A module for proportional gain control
    @details    This controller module is written to be a generic proportional controller
                which can easily be integrated with other procedures. After specifying
                a desired gain, simply pass in the current value/position/state of the
                system and the controller will output the necessary value for the plant in
                the closed-loop negative feedback system.
    @author Damond Li
    @author Chris Or
    @author Chris Suzuki
    @date 2/3/22
"""

import pyb
import motor
import encoder
import time
import utime

class Controller:
    '''! 
    @brief      Class for a proportional controller
    @details    This class contains the approprate methods to set the gain,
                set the desired position, run the proportional controller, run a step response for a
                motor, and print out the data from the step response.
    '''

    def __init__(self):
        '''! 
        @brief      Constructs a controller object
        @details    Establishes the initial values used by the methods in this class. The proportional
                    gain is initially set to zero. There is an empty list used to collect encoder data.
                    Variables to keep track of time are also established
        '''
        
        ## Proportional gain for the controller
        self.gain = 0
        
        ## Empty list to store encoder data
        self.positional_data = []
        
        ## Reference start time used to zero data for time
        self.start_time = utime.ticks_ms()
        
        ## Variable used to offset our time data so that the step response starts at zero seconds
        self.offset_time = 0
        
        ## A counter for how many times the controller runs
        self.runs = 1
            
    def update(self, current_position):
        '''! 
        @brief      Runs one instance of the proportional controller
        @details    Calculates the error between the current position and the desired position.
                    This error is multiplied by a proportional gain to get an input for the plant.
        @param current_position  The current value/position of the system. This is the negative
                                 feedback loop for the closed-loop system.
        @return     Returns the input that goes into the plant of the closed loop system
        '''
        
        ## Difference between the desired value and the current value
        error = self.des_pos - current_position
        
        ## The controller output
        output = error * self.gain
        
        # Return output
        return output
        
        
    def set_gain(self, desired_gain):
        '''! 
        @brief      Sets the proportional gain for the controller
        @param desired_gain The desired gain for the controller
        '''
        self.gain = desired_gain

    def set_position(self, desired_position):
        '''! 
        @brief      Sets the desired value/position for the controller
        @details    The controller will used this value to calculate the necessary output
                    to bring the system closer to the desired position
        @param desired_position The desired value/position for the system
        '''
        ## Desired position/value for the controller
        self.des_pos = desired_position

    def step_response(self, current_position):
        '''! 
        @brief      Runs a step response for the motor
        @details    This method calculates the PWM duty cycle to operate the motor to get it to
                    reach a specified position
        @param current_position The current position of the motor. The difference between the current position
                                and the desired position will be used to calculate the appropriate PWM duty
                                cycle to operate the motor.
        @return     Returns the duty cycle to operate the motor
        '''
        error = int(self.des_pos) - int(current_position)
        output = error * self.gain
        
        # Determine the time offset using only the first run of the controller
        if self.runs == 1:
            self.offset_time = utime.ticks_diff(utime.ticks_ms(), self.start_time)
                                           
        # Collect encoder data
        self.positional_data.append([utime.ticks_diff(utime.ticks_ms(), self.start_time) - self.offset_time, current_position])
        
        # Count number of times the controller is run
        self.runs += 1
        
        # Returns PWM duty cycle
        return int(output)
    
    def get_position(self):
        '''! 
        @brief      Prints out the time and encoder data in a new line
        @details    This method is intended to be used with writing data through the serial port.
                    Printing the time and encoder data in a new line for each data point makes it
                    simpler to handle the data when reading from the serial port. After all data is
                    printed out, it prints an additional string indicating that all of the data has
                    been read.
        '''
        for item in self.positional_data:
           print(str(item[0]) + "," + str(item[1]), "\n")
        
        # Print marker
        print("DATA")
        
        # Reset the number of runs in order to calculate the offset time for the next step response
        self.runs = 1
        

if __name__ == '__main__':
    # Establish reference time
    start_time = time.time()
    
    # Create motor, encoder, and controller objects
    mtr1 = motor.Motor(1)
    enc1 = encoder.Encoder(1)
    ctr = Controller()
    
    # Enable motor
    mtr1.enable()
    
    # Set desired gain and position
    ctr.set_gain(0.1)
    ctr.set_position(16300)
    
    # Run the controller for two seconds
    while time.time() - start_time < 2:
        power = ctr.update(enc1.read())
        mtr1.set_duty_cycle(power)
        print(enc1.read())
    
    # Disable motor after two seconds
    mtr1.disable()
   
