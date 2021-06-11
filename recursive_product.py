# Write a recursive function to multiply two positive integers without using the * operator. 
# You can use addition, subtraction, and bit shifting but you should minimize the number of those operations */
# Question 8.5 in 6th edition in cracking the coding interview
# https://replit.com/@KristalGarcia2/AutomaticCoolFinance#index.js


import timeit
import time


#==== Brute force solution

def recursive_product(num1, num2):

    if num2 == 1:
        return num1

    return num1 + recursive_product(num1, num2-1)

assert recursive_product(2, 8) == 16, "2*8=16"


#==== Caching solution
def create_cache(num1, num2):
        
    cache = {1: num1}

    for i in range(2,num2+1):
        cache[i] = cache[i-1] + num1
    
    return cache

def get_product(num1, num2):
    """ Create a dictionary to hold the multiplication of num1 with 1,2,3...num2"""
    if num1 < num2:
        get_product(num2, num1)
    
    cache = create_cache(num1, num2)

    return cache[num2]

assert get_product(4, 5) == 20, "4*5=20"
assert get_product(3, 5) == 15, "4*5=20"


#==== Cut one number in half solution
def recurse(num, num_of_calls):
        if num_of_calls == 1:
            return num
        
        return num + recurse(num, num_of_calls - 1)


def recursive_product_half(num1, num2):
    smaller_num = min(num1, num2)
    bigger_num = max(num1, num2)
    num_of_calls = smaller_num//2 #The number of calls is half of the smaller number
    
    total = recurse(bigger_num, num_of_calls)
    total += total

    if smaller_num % 2 != 0:
        total += bigger_num
    
    return total

assert recursive_product_half(2, 8) == 16


#==== Compare performance of the 3 solutions
"""
It is not ideal to measure how long a function takes to run by wrapping inside another function
Review timeit module here https://www.geeksforgeeks.org/timeit-python-examples/
"""
def get_time1():
    recursive_product(9999,50)

print(f'The time it takes for brute force solution: {timeit.timeit(get_time1)}')


start = time.perf_counter()
recursive_product(9999,50)
finish = time.perf_counter()
print(f'The time it takes for the brute force solution (measuring with perf_counter): {round(finish-start, 10)}')


def get_time2():
    get_product(9999, 50)

print(f'The time it takes for the caching solution: {timeit.timeit(get_time2)}')


def get_time3():
    recursive_product_half(9999, 50)

print(f'Time it takes for the cut-in-half solution: {timeit.timeit(get_time3)}')

# To multiply 9999 with 100:
'''
The time it takes for brute force solution: 6.055295
The time it takes for the brute force solution (measuring with perf counter): 9.833e-06
The time it takes for the caching solution: 5.381367333999999
Time it takes for the cut-in-half solution: 3.4107203329999987
'''
