import math

primes = {
    2:"yes",
    3:"yes",
    5:"yes",
    7:"yes",
    11:"yes",
    13:"yes",
    17:"yes",
    19:"yes",
    23:"yes",
    29:"yes",
    31:"yes"
}

'''
Recursive function

Parameters: 
n (int): The root of the binary factor tree.
no_num (boolean): Flag to generate a restrictive tree (with numbers) or general tree (with '1' instead of numbers).

Returns: 
- Base case: 1 if no_num, n otherwise
- Recursive case: [axb] where a and b are the recursive calls of this function on n=left subtree root and n=right subtree root, respectively
'''
def _num_to_string_rec(n, no_num):
    result = "1" if no_num else str(n)
    factors = (0,0)
    if n not in primes:
        factors = find_factors(n)
    if factors[0] == 0 and factors[1] == 0:
        return result
    result = (f"[{_num_to_string_rec(factors[0], no_num)}x{_num_to_string_rec(factors[1], no_num)}]")
    return result

'''
Helper function for correct formatting

Parameters: 
n (int): The root of the binary factor tree.
no_num (boolean): Flag to generate a restrictive tree (with numbers) or general tree (with '1' instead of numbers).

Example: 
945 = [3x[3x3]]x[5x7] (no_num=False)
    = [1x[1x1]]x[1x1] (no_num=True)

Returns: The string representation
'''
def num_to_string(n, no_num=False):
    result = "1" if no_num else str(n)
    factors = (0,0)
    if n not in primes:
        factors = find_factors(n)
    if factors[0] == 0 and factors[1] == 0:
        return result
    result = (f"{_num_to_string_rec(factors[0], no_num)}x{_num_to_string_rec(factors[1], no_num)}")
    return result

def double_factorial(n):

    if n<0:
        return 0
    if n <= 2:
        return n

    total = 1
    for i in range(n, 1, -2):
        total*=i
    
    return total

'''
Function that stores the smallest number with binary factor tree of the same shape as T(n) for 2<=n<=1000000.

Returns: 
(dict): dictionary containing the string representations as keys and the smallest number for that tree shape as value.
(int): greatest number with a binary factor tree that was not previously in the tree
'''
def find_factors(n):
    is_prime = n in primes
    if is_prime:
        return (0,0)
    diff = n
    a, b = 0,0 
    for i in range(2, int(math.sqrt(n))+1):
        if (n%i==0): #found a factor of n
            other_factor = n//i
            curr_diff = abs(i-other_factor)
            if curr_diff < diff:
                diff = curr_diff
            a, b = min(i, other_factor), max(i, other_factor)
    
    return (a,b)
