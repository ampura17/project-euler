# Project Euler Problem 5
# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all
# of the numbers from 1 to 20?
# lcm(a,b) = ab/gcd(a,b)
# lcm - least common multiple
# gcd - greatest common divisor
# To avoid overflow use lcm = a /gcd(a,b) * b
def gcd(a,b):
    if a > b:
        larger = a
        smaller = b
    else:
        larger = b
        smaller = a
    r = 1
    while r != 0:
        r = larger % smaller
        larger = smaller
        smaller = r
    return larger 

def lcm(a,b):
    result = a/gcd(a,b)*b
    return result

def main():
    numbers = list(range(1,20))
    a = 1
    for index in range(len(numbers)):
        #lcm(a,b)=a/gcd(a,b)*b
        b = numbers[index]
        temp = lcm(a,b)
        a = temp

    print(int(a))

if __name__ ==  "__main__":
    main()
