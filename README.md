# PyCount
<p align="left">
  <a aria-label="license" href="https://github.com/primer/css/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/primer/css.svg" alt="">
  </a>
</p>

Python code to count to a user-supplied number.

I play a game that has let stat inflation go unchecked. Another game customer created a spreadsheet where damage was in the trillions and I started thinking about how long it would take a system to count to one trillion.

It would be an incredibly long time.

## Current Code

The recent update implemented multiprocessor use. I implemented a function to chunk the number into as equal sized numbers as possible based on the amount of cores/threads <em>os.system</em> finds. This program will count up to that number and display the time it took to reach the count rounded to 3 decimal places. It's a work in progress.

Goals:
- Have the user enter the number of cores to use
- <color=red>COMPLETED</color>: Parallel processing; rather than use one CPU, use all available
- Extrapolate larger numbers; for example, if it takes 0.05 seconds to count to 100,000, how long would it take to count to 1 trillion?
- Have the program add human-readable numbers (such as with commas, where appropriate) based on input and results
- Have fun!

## Notes
I know that Python isn't the language most suited to the fastest count from 1 to any given number. It's something I wanted to do and have fun doing it. If you can use the code, please do so. If you know of a more efficient way, please let me know.
