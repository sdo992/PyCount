#!/usr/bin/env python
import time
a = 1 # Declare variable before time stamp and loop
uin = int(input("Enter an integer up to which you would like the system to count: "))
print("Counting to " + str(uin))
start = time.time() # Get the current time
while a <= uin:
    a = a + 1
ending = time.time() # Get the time at which the while loop ended
stp = str(round(ending - start, 3)) # Limit to three decimal places and convert to a string
print("Completed in: " + stp + " seconds")
