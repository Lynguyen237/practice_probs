# An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

# Your goal is to find that missing element.

# Write a function:

# def solution(A)

# that, given an array A, returns the value of the missing element.

# For example, given array A such that:

#   A[0] = 2
#   A[1] = 3
#   A[2] = 1
#   A[3] = 5
# the function should return 4, as it is the missing element.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [0..100,000];
# the elements of A are all distinct;
# each element of array A is an integer within the range [1..(N + 1)].

# Mathematical solutions:
def missing_int(A):
    
    full_len = len(A) + 1
  
    total_sum = full_len*(full_len+1)/2

    actual_sum = 0
    
    for i in A:
        actual_sum += i
    
    return int(total_sum - actual_sum)


print(missing_int([2,3,5,1])) # 4
print(missing_int([1,2,3,4,5,6])) # 7

# Solution N^2, timeout error for big numbers
def solution(A):
    
    set_A = set(A)

    missing_no = 1

    while missing_no in set(A):
        missing_no += 1
    
    return missing_no