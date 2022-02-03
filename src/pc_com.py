'''!
@file     pc_com.py
@brief    A program that runs a step response prompted by the PC and plots resulting data
@details  This is a program for the PC which will run step response tests by sending
          characters through the USB serial port to the Nucleo board, reading the resulting data,
          and plotting the step response with labeled axes. This program allows us to efficiently
          test various gain, Kp, values on a step response run through a prompt from the PC user. 
@author Damond Li
@author Chris Or
@author Chris Suzuki
@date 2-Feb-2022 SPL Original file
'''
import serial
import time
import numpy as np
import matplotlib.pyplot as plt

## Set the communication channel and serial data rate for the serial port
with serial.Serial('COM3', 115200) as s_port:

    while True:
        ## Set input as any text value and enter to proceed
        start_step = input("Type any text + Enter to run a step response ")
        try:
            # Convert string value to a float
            float(start_step)
            # Revert value to string to encode and add return
            s_port.write(str(start_step).encode() + b'\r')
            break
        except ValueError:
            # Exception for an input that is not numerical
            print('Invalid Value')

    ## Boolean variable describing whether all of the data has been read
    bool = True
    ## Initialize list for data to be collected
    data = []
    
    # Check for when the data has finished and ends the loop
    while bool:
        buffer = s_port.readline()
        # At 'DATA' the data has finished
        if buffer == b'DATA\r\n':
            bool = False
            break
        else:
            # Appends data to the 'data' list
            data.append(buffer.decode())
            
## Initialize lists for data to be plotted        
x = []
y = []

## Object for number of runs to complete all data points
runs = 0

# Loops until data is finished
for idx in data:
    if runs != 0:
        # Deletes irrelevant characters and splits csv data
        p = idx[0:-3].split(',')
        # Eliminates empty data and appends to each corresponding list based on position
        if p[0] != "" and p[1] != "":
            x.append(p[0])
            y.append(p[1])
    # Adds to run for each iteration of the loop
    runs += 1

# Plot the resulting data
# Set the x and y tick ranges for the axes
plt.xticks(range(int(min(x)),int(max(x)), 10))
plt.yticks(range(int(min(y)),int(max(y)), 10))
# Plot the data
plt.plot(x,y)
# Axes labels for x and y axes
plt.xlabel('Time (Sec)')
plt.ylabel('Encoder Value (Ticks)')
# Show plot on Thonny
plt.show()

