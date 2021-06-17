'''
Factorial of a non-negative integer, is multiplication of all integers smaller than or equal to n. 
For example factorial of 6 is 6*5*4*3*2*1 which is 720.
'''

def factorial(n):

    result = 1

    for i in range(1,n+1):
        result *= i
    
    return result

assert factorial(6) == 720
assert factorial(1) == 1


def factorial_recursive(n):

    if n == 1:
        return 1
    else:
        return n*factorial_recursive(n-1)

assert factorial_recursive(6) == 720
assert factorial_recursive(1) == 1