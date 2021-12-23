'''
Project Euler problem 10:
The sum of the primes below 10 is 2+3+5+7=17.
Find the sum of all primes below two million.
'''
# Sieve of Eratosthenes
# 1. Set sum equal to zero
# 2. Create an array (sieve) of True with N elements
# 3. For p=2 to N, if p-th element in sieve is True, add the number to the sum
# 4. Starting from square of p to N by p step turn all elements in sieve to False
# 5. Show resulting sum after outer loop.
import numpy as np

def main():
    target=2000000
    sum, sieve = 0, [True]*target
    for p in range(2,target):
        if sieve[p]:
            sum += p
            for i in range(p*p, target, p):
                sieve[i] = False
    print(sum)

if __name__== '__main__':
    main()

