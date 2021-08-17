# By listing the first six prime numbers: 2, 3, 5, 7, 11 and 13,
# we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def isPrime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    counter = 3
    while counter*counter <= num:
        if num % counter == 0:
            return False
        else:
            counter += 2
    return True

def main():
    numPrimes = 1
    num = 1

    while (numPrimes < 10001):
        num = num + 2
        if isPrime(num):
            numPrimes += 1
    print(num)

if __name__ == "__main__":
    main()
