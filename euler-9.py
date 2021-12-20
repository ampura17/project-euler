"""
A Pythagorean triplet is a set of three natural numbers, a<b<c, for which, a^2+b^2=c^2
For example, 3^2+4^2=9+16=25=5^2.
There exists exactly one Pythagorean triplet for which a+b+c=1000.
Find the product abc.
"""
def main():
    sum = 1000
    for a in range(1,int(sum/3+1)):
        for b in range(1,int(sum/2+1)):
            c=sum-a-b
            if a**2+b**2==c**2:
                print("The Pythagorean Triplet, whose sum is 1000, are:\n{}, {}, {}".format(a,b,c))
                print("Product of abc is", a*b*c)
if __name__ == '__main__':
    main()