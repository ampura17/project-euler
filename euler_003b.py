# Project Euler Problem 3:
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

# Prime number formula: 6n+1 or 6n-1, where n is natural number.

import math
import numpy as np

def main():
    #while True:
    #    try:
    #        x = int(input('Insert the number for biggest Factorization\n'))
    #        break
    #    except:
    #        print("That is not a valid option")

    def factor_into_2(x):
        a = math.ceil(np.sqrt(x))
        b2 = a*a - x
        b = math.sqrt(b2)
        check = True
  
        while check == True:
            #Check if the number is perfect square
            if int(b + 0.5) ** 2 == b2:
                check = False
            else:
                a = a + 1
                b2 = a*a - x
                b = math.sqrt(b2)
        f1 = a+b
        f2 = a-b
        
        return f1, f2

    x = int(600851475143)       
    f1,f2 = factor_into_2(x)
    print(f1,' ', f2)

    if f1>f2: 
        f1,f2 = factor_into_2(f2)
    else:
        f1,f2 = factor_into_2(f1)
    print(f1,' ',f2)
    

if __name__ == "__main__":
    main()


