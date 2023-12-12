#!/usr/bin/env python3
import multiprocessing
import time
import sys
import os
from datetime import timedelta

def count_up(start, end, result_queue):
    count = 0
    for i in range(start, end):
        count += 1
    result_queue.put(count)

def uin_Int():
    os.system('clear') # Let's start clean
    uin = input("Enter a number, or, 'q' to quit: ") # Accepting as a string, will change to integer later
    if uin == 'q':
        os.system('clear') #Why not?
        print("Goodbye!")
        time.sleep(2) #Arbitrary time to keep the goodbye on screen
        os.system('clear') #Keeping it clean
        sys.exit(0) #Exit the program
    try:
        nuin = int(uin) #Make sure it's an integer
        return nuin #Make this available
    except ValueError:
        print("I need an integer to continue.")
        time.sleep(1.5) #Arbitrary time to keep error message on screen
        return(uin_Int())

def main():
    nuin = int(uin_Int()) # Convert string into integer
    print("    Counting to " + format(nuin, ',d')) #Format output to a more readable number
    num_processors = os.cpu_count() # Get the number of cores/threads
    print("    Number of cores to be used: " + str(num_processors))
    
    chunk_size = nuin // num_processors # Break up the user number as equally as possible
    start = 0
    
    result_queue = multiprocessing.Queue()
    processes = []
    
    start_time = time.time()
    
    for _ in range(num_processors):
        end = start + chunk_size
        process = multiprocessing.Process(target=count_up, args=(start, end, result_queue))
        processes.append(process)
        start = end
    
    for process in processes:
        process.start()
    
    for process in processes:
        process.join()
        
    total_count = sum(result_queue.get() for _ in range(num_processors))
    end_time = time.time()
    endtd = timedelta(seconds=(end_time - start_time)) # How long did it take?
    print("    Completed LOOP in: " + str(endtd)[:-3] + " seconds") #Limit to three decimal points and keep it clean

if __name__ == "__main__":
    main()
