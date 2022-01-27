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

class pc_com:
    '''!
        @brief Interface with quadrature encoders
        @details Creates a class that can be called into other python files that
                 is used to interface and read out the position of an encoder.
                 The class contains 3 methods. One to construct an encoder object,
                 one to get the position that the encoder reads, and one to set the 
                 position of the encoder to a specified value.
    '''

    def __init__(self, COMx):
        
        '''!
            @brief Constructs an encoder object
            @details Instantiates an encoder object that contains 2 different
                     methods that can be used in other python files. This also
                     generally sets up the use of any encoder so multiple can 
                     be called in any file.
            @param enc_num Value used to establish each instance of the encoder.
                           Currently, this driver only supports up to 2 encoders.
                           Therefore this argument is either 1 or 2.
        '''
        self.COMx = COMx
        
        with serial.Serial (self.COMx, 115200) as s_port:
            print (s_port.readline ().split (b','))
            
    def read(self):
        '''!
            @brief Updates encoder position 
            @details Creates an update method that when ran will update the position
                     of the specfied encoder
            @return Returns the position of the encoder
        '''
        ## Defines the position of the encoder as the the timer linked to the encoder
        


## main testing encoder code
if __name__ == '__main__':
    encoder1 = Encoder(1)
    encoder2 = Encoder(2)
    while(True):
        time.sleep(0.1)
        print([encoder1.read(), encoder2.read()])
        
