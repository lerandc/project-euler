"""
Luis RD
April 12, 2020

------------------------------------------------
A unit fraction contains 1 in the numerator. 
The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. 
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

from algorithms import prime_sieve1

def main():

    #first look for unit fractions that are repeating at least to 6th decimal
    primes = [7,11,13,17,19,23] #prime_sieve1(1000)
    r_lengths =[] #length of repetends by Fermat little theoerem
    for i in primes:
        tmp = 10 % i
        for j in range(1,i):
            if (tmp**j % i) == 1:
                r_lengths.append(j)
                break
    
    print(r_lengths)
    print(max(r_lengths))


if __name__ == '__main__':
    main()