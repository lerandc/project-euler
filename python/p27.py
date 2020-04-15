"""
Luis RD
April 11, 2020

------------------------------------------------
Euler discovered the remarkable quadratic formula:

n^2+n+41
It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39.
However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41 is clearly divisible by 41.

The incredible formula n2−79n+1601 was discovered, 
which produces 80 primes for the consecutive values 0≤n≤79. 
The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b, for the quadratic expression 
that produces the maximum number of primes for consecutive values of n, starting with n=0.
"""

import numpy as np
from algorithms import isPrime, count, prime_sieve1

@count
def evaluate_polynomial(A,B,N):
    """
    Evaluate if value of polynomial expression N^2+A*N+B is prime
    """
    return isPrime(N**2+A*N+B)

def main():
    best = 0 #running best number of consecutive primes
    best_list = []
    A = 0 #running best coefficient A
    B = 0 #running best coefficient B

    #brute force solution
    # for b in range(-1000,1001): #in range(-1000,1001):
    #     for a in range(-999,1000): #in range(0,1000):

    #         N = 0
    #         while(evaluate_polynomial(a,b,N)):
    #             N += 1
            
    #         if N > best:
    #             best = N
    #             best_list.append(N)
    #             A = a
    #             B = b

    # print("Best A: ", A)
    # print("Best B: ", B)
    # print("Number of consecutive primes: ", best)
    # print("Product: ", A*B)
    # print("Function evals: ", evaluate_polynomial.called)
    # print(best_list)


    #eliminate bad solns early, limit function evals
    best = 0 #running best number of consecutive primes
    best_list = []
    A = 0 #running best coefficient A
    B = 0 #running best coefficient B

    #check only odd B coefficients
    #check if best is prime, then continue into while
    # for b in range(-999,1000,2): #in range(-1000,1001):
    #     for a in range(-999,1000): #in range(0,1000):
    #         N = 0
    #         if(evaluate_polynomial(a,b,best)):
    #             while(evaluate_polynomial(a,b,N)):
    #                 N += 1
            
    #         if N > best:
    #             best = N
    #             best_list.append(N)
    #             A = a
    #             B = b 

    # print("Best A: ", A)
    # print("Best B: ", B)
    # print("Number of consecutive primes: ", best)
    # print("Product: ", A*B)
    # print("Function evals: ", evaluate_polynomial.called)

    #for quadratic polynomial, and N = 0, b should be prime
    best = 0 #running best number of consecutive primes
    A = 0 #running best coefficient A
    B = 0 #running best coefficient B
    b_list = prime_sieve1(1000)

    for b in b_list: #primes in range(-1000,1001):
        for a in range(-999,1000): #in range(0,1000):
            N = 0
            if(evaluate_polynomial(a,b,best)):
                while(evaluate_polynomial(a,b,N)):
                    N += 1
            
            if N > best:
                best = N
                best_list.append(N)
                A = a
                B = b 

    print("Best A: ", A)
    print("Best B: ", B)
    print("Number of consecutive primes: ", best)
    print("Product: ", A*B)
    print("Function evals: ", evaluate_polynomial.called)


if __name__ == '__main__':
    main()