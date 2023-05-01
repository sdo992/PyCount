#!/usr/bin/env python
import time
import sys
import os
from datetime import timedelta

def uin_Int():
    os.system('clear') #Clear the screen before beginning
    uin = input("Enter a number, or, 'q' to quit: ")
    if uin == 'q':
        os.system('clear') #Why not?
        print("Goodbye!")
        time.sleep(2) #Arbitrary time to keep the goodbye on screen
        os.system('clear') #Keeping it clean
        sys.exit(0) #Exit the program
    try:
        nuin = int(uin)
        return nuin #Make this available
    except ValueError:
        print("I need an integer to continue.")
        time.sleep(1.5) #Arbitrary time to keep error message on screen
        return(uin_Int())
    
nuin = uin_Int()
print("Counting to " + format(nuin, ',d')) #Format output to a more readable number
a = 1 # Declare variable before time stamp and loop
start = time.time() # Get the current time

while a <= nuin:
    a = a + 1
ending = time.time() # Get the time at which the while loop ended
stp = str(round(ending - start, 3)) #Limit to three decimal places and convert to a string
endtd = timedelta(seconds=(ending - start)) #Evaluating a different method to show time
print("Completed WHILE LOOP in: " + stp + " seconds")
print("Completed WHILE LOOP in: " + str(endtd)[:-3] + " seconds") #Limit to three decimal points

fstart = time.time() #Evaluating difference between WHILE and FOR loops
for i in range(nuin):
	a += 1
fending = time.time()
fstp = str(round(fending - fstart, 3))
fendtd = timedelta(seconds=(fending - fstart))
print("Completed FOR LOOP in: " + fstp + " seconds")
print("Completed FOR LOOP in: " + str(fendtd)[:-3] + " seconds")
