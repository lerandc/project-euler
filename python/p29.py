"""
Luis RD
April 12, 2020

------------------------------------------------
Consider all integer combinations of ab for 2 ≤ a ≤ 5 and 2 ≤ b ≤ 5:

22=4, 23=8, 24=16, 25=32
32=9, 33=27, 34=81, 35=243
42=16, 43=64, 44=256, 45=1024
52=25, 53=125, 54=625, 55=3125
If they are then placed in numerical order, with any repeats removed, we get the following sequence of 15 distinct terms:

4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

How many distinct terms are in the sequence generated by ab for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?
"""

from algorithms import factorize
def prod(vals):
    """
    List product
    """
    product = 1
    for i in vals:
        product *= i
    return product

def countDuplicates(vals):
    """
    Count duplicates in sorted tuple list
    """
    count = 0
    for i in range(1,len(vals)):
        if vals[i] == vals[i-1]:
            count+=1

    return count


def main():
    #strategy is to reduce numbers to their prime factorizations
    #keep prime factors in one list, ordered; exponents in corresponding list, also ordered

    #generate prime factors for 2-100
    factors = []
    exponents = []
    for i in range(2,101):
        f, e = factorize(i)
        if len(f) > 0:
            factors.append(f)
            if len(e) > 0:
                exponents.append(e)
            else:
                exponents.append([1])
        else:
            factors.append([i])
            exponents.append([1])

    factors_a = []
    exponents_b = []
    for i in range(0,len(factors)):
        for b in range(2,101):
            factors_a.append(factors[i])
            exponents_b.append([j*b for j in exponents[i]])


    #join lists
    union = []
    for i in range(0,len(factors_a)):
        union.append((factors_a[i],exponents_b[i]))

    # print(union[0:100])
    union = sorted(union, key=lambda x: (prod(x[0]),x[1]))
    # count = countDuplicates(union)
    new_union = [union[0]]
    for i in range(1,len(union)):
        if union[i] != union[i-1]:
            new_union.append(union[i])

    print(len(union))
    print(len(new_union))
    print(new_union)

    
if __name__ == '__main__':
    main()