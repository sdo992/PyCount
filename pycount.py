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
    while True:
        os.system('clear')
        uin = input("Enter a number or 'q' to quit: ")
        try:
            if uin == 'q':
                os.system('clear')
                print("Goodbye!")
                time.sleep(2.0)
                os.system('clear')
                sys.exit(0)
            else:
                nuin = int(uin)
                break
        except ValueError:
            os.system('clear')
            print("Error! You need to enter an integer.")
            time.sleep(2.0)
    return nuin

def ucpu():
    while True:
        num_processors = os.cpu_count()
        print("Number of CPU cores available: " + str(num_processors))
        ucpui = input("Enter the number of cores you would like to use: ")
        try:
            ucpue = int(ucpui)
            if ucpue <= num_processors:
                break
            else:
                os.system('clear')
                print("Error! The number you entered exceeds the amount of CPU cores available. Try again.")
                time.sleep(2.0)
        except ValueError:
            os.system('clear')
            print("Error! The value entered must be an integer.")
            time.sleep(2.0)
    return ucpue

def main():
    nuin = int(uin_Int())
    ucpue = int(ucpu())
    print("    Counting to " + format(nuin, ',d')) #Format output to a more readable number
    print("    Using total number of CPU cores: " + str(ucpue))
    
    chunk_size = nuin // ucpue
    start = 0
    
    result_queue = multiprocessing.Queue()
    processes = []
    
    start_time = time.time()
    
    for _ in range(ucpue):
        end = start + chunk_size
        process = multiprocessing.Process(target=count_up, args=(start, end, result_queue))
        processes.append(process)
        start = end
    
    for process in processes:
        process.start()
    
    for process in processes:
        process.join()
        
    total_count = sum(result_queue.get() for _ in range(ucpue))
    end_time = time.time()
    endtd = timedelta(seconds=(end_time - start_time)) # How long did it take?
    print("    Completed in: " + str(endtd)[:-3] + " seconds") #Limit to three decimal points and keep it clean

if __name__ == "__main__":
    main()
