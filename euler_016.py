# Project Euler problem 15: POWER DIGIT SUM
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26
# What is the sum of the digits of the number 2^1000?

import math

def main():
    base = 2
    power = 1000
    number = int(math.pow(base, power))

    total = 0
    for digit in str(number):
        total += int(digit)
    
    return print(total)

if __name__=='__main__':
    main()