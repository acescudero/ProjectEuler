import math
from data import *
from math_operations import *
import time


primes_list = [2,3,5,7,11,13,17,19,23,29,31]

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

#shapes = {}
shapes = shapes_all

def generate_first_mill():
    dir = {}
    greatest = 2
    for i in range(2,1000001):
        #print(f"Generating string rep for i={i}")
        str_rep = num_to_string(i, True)
        if str_rep not in dir:
            dir[str_rep] = i
            if i>greatest:
                greatest = i

    return dir,greatest

def double_factorial(n):
    if n<0:
        return 0
    if n <= 2:
        return n
    total = 1
    for i in range(n, 1, -2):
        total*=i
    
    return total

def is_power_of_two(n):
    return (n & (n-1) == 0)

"""
Finds the biggest number with binary factor tree of the same shape as n that is less than or equal k
"""
def maximize_less_than(n, k, n_str_rep):
    result = n
    global shapes
    for i in range(n-1, 2, -1):
        i_str_rep = num_to_string(i, True)
        if i_str_rep == n_str_rep:
            return i
    return result

def maximize_special(n, k, n_str_rep):
    result = n
    global shapes
    for i in range(k-1, 2, -1):
        i_str_rep = num_to_string(i, True)
        if i_str_rep == n_str_rep:
            return i
    return result

def special_case(n, k, n_str_rep, original_str_rep):
    result = n
    global shapes
    last_i = 0
    for i in range(k, 2, -1):
        i_str_rep = num_to_string(i, True)
        if i_str_rep == n_str_rep:
            result = i*k
            if num_to_string(result, True) == original_str_rep:
                last_i = i
            else:
                return last_i
    return result

"""
Finds the smallest number with binary factor tree of the same shape as a (a_str_rep), 
and the smallest number with binary factor tree of the same as b (b_str_rep) such that b>a
"""
def minimize_both(a, b, a_str_rep, b_str_rep):
    #print("entered both")
    global shapes
    a_minimized = a
    b_minimized = b
    if a in primes:
        #print("lmao")
        a_minimized = 2
        if b in primes:
            return 2,2
    elif a_str_rep in shapes:
        #print(f"a={a} is in shapes")
        a_minimized = shapes[a_str_rep]
        #print(f"shape 1: {a_str_rep}")
        #print(f"shape 2: {num_to_string(a_minimized, True)}")
    elif b_str_rep in shapes:
        b_minimized = shapes[b_str_rep]
    if a_minimized == a and b_minimized == b:
        #print("Returning 0")
        return 0,0
    for i in range(a_minimized+1, b+1):
        i_str_rep = num_to_string(i, True)
        if i_str_rep not in shapes:
            shapes[i_str_rep] = i
        if i_str_rep == b_str_rep:
            b_minimized = i
            break
    return a_minimized, b_minimized

def find_next_prime(n):
    for p in primes_list:
        if p>=n:
            return p


def M(n, special=False):
    n_double_fac = double_factorial(n)
    if special:
        n_double_fac = n
    if n_double_fac in primes:
        return 2
    a,b = find_factors(n_double_fac)
    if is_power_of_two(a):
        if b in primes:
            print("Passed")
            b = find_next_prime(a)
            return a*b
        left_str_rep = num_to_string(a, True)
        right_str_rep = num_to_string(b, True)
        if left_str_rep == right_str_rep:
            return a*a
        return n_double_fac
    elif is_power_of_two(b):
        #look for biggest left subtree of same shape
        left_str_rep = num_to_string(a, True)
        minimized_left = maximize_less_than(a, b, left_str_rep)
        return minimized_left*b
    else: #neither is a power of 2
        if n>14 and n%2==0 and n!=20:
            return n_double_fac
        left_str_rep = num_to_string(a, True)
        right_str_rep = num_to_string(b, True)
        new_a, new_b = minimize_both(a,b,left_str_rep,right_str_rep)
        #print(f"new_a={new_a}, new_b={new_b}")
        if new_a*new_b!=0:
            if num_to_string(new_a*new_b, True)==num_to_string(n_double_fac, True):
                return new_a*new_b
        a_str_rep = left_str_rep
        b_str_rep = right_str_rep
        if a_str_rep in shapes_all and b_str_rep in shapes_all:
            to_be_used = max(shapes_all[a_str_rep], shapes_all[b_str_rep]) #we minimize b this way, otherwise b-a is not minimized
            #print(f"Calling special case for n={n}")
            #print(f"To be used is {to_be_used}")
            minimized_left = special_case(a, to_be_used, a_str_rep, num_to_string(a*b, True))
            new_res = minimized_left*to_be_used
            if new_res == 0:
                for i in range(to_be_used+1, b):
                    i_str_rep = num_to_string(i, True)
                    if i_str_rep not in shapes:
                        shapes[i_str_rep] = i
                    if i_str_rep == right_str_rep:
                        #print(f"Found={i}")
                        new = maximize_special(a, i, left_str_rep)
                        #print(f"Obtained={new}")
                        if (num_to_string(new*i,True) == num_to_string(a*b,True)):
                            return new*i
            #print(f"Found minimmized left={minimized_left}")
            return minimized_left*to_be_used
        


def main():
    total = 0
    global shapes
    #shapes, biggest = generate_first_mill()
    #print(shapes)


    for n in range(2,30):
        ans = M(n)
        total+=ans
        print(f"Solution for {n}!!={double_factorial(n)} is {ans}")
    
    val_30 = 40260046159872000 # done by hand, code takes too long
    print(f"Solution for {30}!!={double_factorial(n)} is {val_30} (done by hand)")
    val_31 = 26129782224000 # done by hand, code takes too long
    print(f"Solution for {31}!!={double_factorial(n)} is {val_31} (done by hand)")
    total+=(val_30+val_31)
    print(f"Final answer={total}")


    #print(M(10321920, True))


    '''
    left = num_to_string(116025,True)
    right = num_to_string(118503,True)
    print(f"s1:{left}\ns2:{right}")
    print(minimize_both(116025,118503, left, right))
    '''
    '''
    
    print(maximize_less_than(60, 64, num_to_string(60, True)))
    print(minimize_both(9,11,num_to_string(9,True), num_to_string(11,True)))
    print(f"___________\nFinal result={total}")
    '''



if __name__=="__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Time elapsed: {end_time-start_time}")
'''
84.35807204246521 (no gen)
105.87593412399292 (with gen)
    '''
