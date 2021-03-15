# Codility - lesson 4 - Max Counters
# You are given N counters, initially set to 0, and you have two possible operations on them:

# increase(X) − counter X is increased by 1,
# max counter − all counters are set to the maximum value of any counter.
# A non-empty array A of M integers is given. This array represents consecutive operations:

# if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
# if A[K] = N + 1 then operation K is max counter.
# For example, given integer N = 5 and array A such that:

#     A[0] = 3
#     A[1] = 4
#     A[2] = 4
#     A[3] = 6
#     A[4] = 1
#     A[5] = 4
#     A[6] = 4
# the values of the counters after each consecutive operation will be:

#     (0, 0, 1, 0, 0)
#     (0, 0, 1, 1, 0)
#     (0, 0, 1, 2, 0)
#     (2, 2, 2, 2, 2)
#     (3, 2, 2, 2, 2)
#     (3, 2, 2, 3, 2)
#     (3, 2, 2, 4, 2)
# The goal is to calculate the value of every counter after all operations.

# Write a function:

# def solution(N, A)

# that, given an integer N and a non-empty array A consisting of M integers, 
# returns a sequence of integers representing the values of the counters.

# Result array should be returned as an array of integers.

# For example, given:

#     A[0] = 3
#     A[1] = 4
#     A[2] = 4
#     A[3] = 6
#     A[4] = 1
#     A[5] = 4
#     A[6] = 4
# the function should return [3, 2, 2, 4, 2], as explained above.

# Write an efficient algorithm for the following assumptions:

# N and M are integers within the range [1..100,000];
# each element of array A is an integer within the range [1..N + 1].

# Complexity N + M
def max_counters(N, A):
    
    N_counters = [0] * N
    max_counter = 0


    if len(set(A)) == 1:
        if A[0] == N+1: # If all values in the array is the same and have max_counter operations
            return N_counters
        else:
            N_counters[A[0]-1] = len(A) # If all values in the array in the same and have increment_by_1 operations
            return N_counters


    for i in A:
        if i <= N:
            N_counters[i-1] += 1 # if the item is small than N, implement increment_by_1 operation
            if N_counters[i-1] > max_counter: # if counter > max_counter, reassign a new max_counter value
                max_counter = N_counters[i-1]
        elif i == N+1:
            N_counters = [max_counter] * N
    
    return N_counters

print(max_counters(5,[3,4,4,6,1,4,4])) #[3, 2, 2, 4, 2]
print(max_counters(3,[1])) #[1]
print(max_counters(3,[1,1,1])) #[3,0,0]
print(max_counters(3,[1,4,1])) #[2,1,1]
print(max_counters(3,[1,1,4])) #[2,2,2]
print(max_counters(1000,[1,1,999,999,999,1001])) # [3,3,3...,3]
print(max_counters(100000,[100001]*100001)) # [0,0...,0]

# Alternative solution: https://codesays.com/2014/solution-to-max-counters-by-codility/