import time

from primes import primes, primes_dict
from typing import Any, Dict, Tuple
from math import sqrt
from sympy import isprime as is_prime

'''
def is_prime(n):
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n)), 2):
        if n % i == 0:
            return False
    return True
'''


def reverse_integer(n) -> Tuple[int, bool]:
    copy = n
    reverse = 0

    while n:
        # Multiply reverse by 10 to add place for a digit, calculate the digit
        # to add by doing mod 10 on n, which gives us the last digit of n, and
        # add it to reverse, then perform integer division on n by 10 to remove
        # the last digit.
        reverse = reverse * 10 + n % 10
        n //= 10

    # Reversing the integer also allows us to check if it's a palindrome by
    # saving a copy of the original number, and if it's equal to the final
    # value of n that we reversed, then it's a palindrome. So we are basically
    # "killing 2 birds with one stone"!
    return reverse, reverse == copy


def is_reversible(n: int, prime_dict: Dict[int, Any]) -> Tuple[int, bool]:
    reverse, is_palindrome = reverse_integer(n)
    if is_palindrome:
        # If palindrome, simply return False and don't run the remaining
        # computations.
        return reverse, False
    val = sqrt(reverse)
    int_val = int(val)
    if val % 1 > 0:
        # If square root mod 1 > 0, this means the number is not an integer, so
        # it can't be a prime.
        prime_check = False
    else:
        prime_check = is_prime(int_val)
        # since we generated a dictionary that contains primes, we can just
        # check if int_val is in that dictionary which is an O(1) operation
        # instead of running an is_prime algorithm. However, after testing,
        # simply calling is_prime yields basically the same runtime, so I guess
        # sympy's isprime() function is super efficient.
        '''
        prime_check = (
            is_prime(int_val) if int_val > 32452843 else int_val in prime_dict
        )'''

    return reverse, prime_check


def main():
    sum = 0
    count = 0
    for prime in primes:
        square = prime**2
        _, is_rev = is_reversible(square, primes_dict)
        if is_rev:
            print(f'{square} is reversible and prime is {prime}')
            sum += square
            count += 1
            if count == 50:
                break
    # Would be ideal to add a condition to check if we indeed found 50 primes,
    # but the first 50 reversible square primes correspond to primes that are
    # within the first 2 million primes, so for values greater than 50 we would
    # absolutely need this condition, and perhaps have another file with even
    # more primes that we load only after we exhausted the first 2 million.
    # Also, when printing the prime numbers that correspond to the reversible
    # prime squares, we can see that their digits are only 0,1,2,3, so we could
    # also find a pattern. 
    print(f'Answer: {sum}, {count} were found')


if __name__=='__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    # Takes ≈2.7s including loading in the 2M primes from the file.
    print(f'Time taken is: {end_time-start_time}')
