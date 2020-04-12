"""
Luis RD
April 11 2020

Common algorithms and methods for use in Project Euler problems.
"""
import numpy as np

def isPrime(N):
    """
    Check if number N is a prime integer
    """
    #first check if less than zero or not an integer
    if (N > 0) and (np.equal(np.floor(N),N)):
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
        