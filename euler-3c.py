# Project Euler Problem 3 
# The prime factors of 13195 are 5,7,13 and 29.
# What is the largest prime factor of the number 600851475143?

def main():

    number = int(600851475143)
    new_number = number
    largestFact = 0
    counter = 2

    while counter*counter <= new_number:
        if new_number % counter == 0:
            new_number = new_number / counter
            largestFact = counter
        else:
            counter += 1

    if new_number > largestFact:
        largestFact = new_number
    
    print(largestFact)

if __name__ == "__main__":
    main()
