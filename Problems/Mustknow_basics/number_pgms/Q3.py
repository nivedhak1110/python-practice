"""
Q-3
Python program to check if the given number is Happy Number
A number is said to be happy if it yields 1 when replaced by 
the sum of squares of its digits repeatedly. If this process 
results in an endless cycle of numbers containing 4, then 
the number will be an unhappy number.

Let's understand by an example:

Number = 32
32+ 22 = 13
12 + 32 = 10
12 + 02 = 1


In this example, we split 32 to get the sum of squares of 
its digits which forms another number (13), we replace 32 by 
13 to continue this cycle until result 1. We found 32 a 
happy number.

If the above cycle for any number results in 1 then that 
number will be a Happy number otherwise that will be an 
unhappy number resulting 4, 16, 37, 58, 89, 145, 42, 20.....

Some Happy numbers are 7, 28, 100, 320, etc.
"""
