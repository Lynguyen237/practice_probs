# A non-empty array A consisting of N integers is given.

# A permutation is a sequence containing each element from 1 to N once, and only once.

# For example, array A such that:

#     A[0] = 4
#     A[1] = 1
#     A[2] = 3
#     A[3] = 2
# is a permutation, but array A such that:

#     A[0] = 4
#     A[1] = 1
#     A[2] = 3
# is not a permutation, because value 2 is missing.

# The goal is to check whether array A is a permutation.

# Write a function:

# def solution(A)

# that, given an array A, returns 1 if array A is a permutation and 0 if it is not.

# For example, given array A such that:

#     A[0] = 4
#     A[1] = 1
#     A[2] = 3
#     A[3] = 2
# the function should return 1.

# Given array A such that:

#     A[0] = 4
#     A[1] = 1
#     A[2] = 3
# the function should return 0.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [1..1,000,000,000].

#==== SOLUTION 1
def permutation_check(A):

    A_set = set(A)

    if len(A_set) > len(A):
        return 0 # A has duplicated values
    
    missing_element = 1

    while missing_element in A_set:
        missing_element += 1
    
    if missing_element > len(A):
        return 1 # if missing element is greater than N (length of A), then A is a permutation
    
    return 0


#==== SOLUTION 2
def permutation_check2(A):
    
    counters = [0] * len(A)

    for i in A:
        if not 1 <= i <= len(A):
            return 0 # if the item in the array is greater than the length of the array, then the array is not a perm
        else:
            if counters[i-1] == 0:
                counters[i-1] = 1
            else:
                return 0 # if counter of a given position is not 0, then it's a duplicated value
    
    return 1