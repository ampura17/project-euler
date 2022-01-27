# Project Euler problem 15: LATTICE PATH
# Starting in the top left corner of a 2x2 grid, and only being able
# to move to the right and down, there are exactly 6 routes to the
# bottom right corner

# How many such routes are there through a 20x20 grid?

# SOLUTION: Wikipedia Lattice Path, 
# number of connections are counted by the binomial coefficient,
# and arranged by the Pascal triangle.

import math

def main():
    
    grWidth = 20
    grHeight = 20
    n = int(grWidth) + int(grHeight)
    k = int(grHeight)
    numRoutes = (math.factorial(n)) / (math.factorial(k) * math.factorial(n-k))

    return print(numRoutes)

if __name__=='__main__':
    main()