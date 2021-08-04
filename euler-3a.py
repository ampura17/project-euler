# Project Euler Problem 3:
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

# This program only find prime numbers in range. (lower and upper)
def main():
    lower = 1  
    upper = 100
    primes = []
    goal = 600851475143
    
    results = []

    for num in range(lower, upper+1):
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    print(primes)
    
if __name__ == "__main__":
    main()
