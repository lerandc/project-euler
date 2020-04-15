"""
Luis RD
April 12, 2020

------------------------------------------------
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""


def main():
    #only need to check within 1024 < N < ~350000
    viable = []
    for N in range(1024,350000):
        digits = [int(i) for i in str(N)]
        if sum(digits) % 10 == N % 10: #ones place is bounded
            if sum([i**5 for i in digits]) == N:
                viable.append(N)

    print(viable)
    print(sum(viable))

if __name__ == '__main__':
    main()