"""
Luis RD
April 12, 2020

------------------------------------------------
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""
def makePandigitalList():
    """
    Enumerate all 9! 1-9 pandigital numbers thru recursion tree
    """
    init = [1,2,3,4,5,6,7,8,9]

    return pandigitals

def swaps(vals, fidx, sidx):
    """
    fidx is index of last fixed value in list
    sidx is current index of swap operation
    """
    vals[fidx+1], vals[sidx] = vals[sidx], vals[fidx+1]
    return vals



def main():


if __name__ == '__main__':
    main()