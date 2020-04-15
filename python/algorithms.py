"""
Luis RD
April 11 2020

Common algorithms and methods for use in Project Euler problems.
"""
import numpy as np

def count(fn):
    """
    Function eval counter
    From: https://stackoverflow.com/questions/33312853/simple-way-to-count-the-number-of-times-def-fx-is-evaluated
    by: labheshr
    """
    def wrapper(*args, **kwargs):
        wrapper.called+= 1
        return fn(*args, **kwargs)
    wrapper.called= 0
    wrapper.__name__= fn.__name__
    return wrapper

def isPrime(N):
    """
    Check if number N is a prime integer
    """
    #first check if less than 1 or not an integer
    if (N > 1) and (np.equal(np.floor(N),N)):
        if N < 4:
            return True
        elif not (N % 2):
            return False
        else:
            for i in range(2,np.int(np.floor(np.sqrt(N)))+1):
                if not N % i:
                    return False
        return True

    return False #if not greater than zero nor integer

def prime_sieve1(max_N):
    """
    Returns list of primes up to integer max_N
    Implementation of Sieve of Eratosthenes
    """
    list_of_primes = range(2,max_N+1)
    for N in range(2,np.int(np.floor(np.sqrt(max_N)))+1):
        list_of_primes = [i for i in list_of_primes if (i % N) or (i <= N)]

    return list_of_primes
        
def factorize(N):
    """
    Similar algorithm to sieve
    Returns two lists, prime factors and exponents for integer N
    """
    assert(type(N)==int), "N is not an integer"
    factors = []
    exponents = []
    for i in prime_sieve1(np.int(np.sqrt(N))):
        if not N % i:
            factors.append(i)
            exponents.append(1)
            N /= i
            while(not N % i):
                exponents[-1] += 1
                N /= i
    
    if N != 1:
        factors.append(int(N))
        exponents.append(1)

    return factors, exponents