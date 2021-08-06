# Project Euler Problem 4
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers 
# is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def main():
    # list of all 3-digit numbers
    x = list(range(100,1000))
    y = list(range(100,1000))

    largestPal = 0
    pal = 0
    numbers = []
    #check all possible products
    for i in x:
        for j in y:
            prod = i * j
            numbers.append(prod)
    for k in numbers:
        first = []
        second = []
        counter = 0
        for l in str(k):
            if counter < 3:
                first.append(l)
                counter += 1
            else:
                second.append(l)
        second.reverse() #Reverse second list to compare with first one
        if first == second:
            pal = k
        if pal > largestPal:
            largestPal = pal

    print(largestPal)

if __name__ == "__main__":
    main()
