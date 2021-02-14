# An array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one index, and the last element of the array is moved to the first place. For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one index and 6 is moved to the first place).

# The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.

# Write a function:

# def solution(A, K)

# that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.

# For example, given

#     A = [3, 8, 9, 7, 6]
#     K = 3
# the function should return [9, 7, 6, 3, 8]. Three rotations were made:

#     [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
#     [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
#     [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
# For another example, given

#     A = [0, 0, 0]
#     K = 1
# the function should return [0, 0, 0]

# Given

#     A = [1, 2, 3, 4]
#     K = 4
# the function should return [1, 2, 3, 4]

# Assume that:

# N and K are integers within the range [0..100];
# each element of array A is an integer within the range [−1,000..1,000].

# SOLUTION

def solution(A,K):
    if len(A) == 0:
        return A
    
    K = K % len(A)
    return A[-K:] + A[:-K]

print(solution([1,2,4,6],2)) #[4,6,1,2]
print(solution([1,1,1,1],3)) #[1,1,1,1]
print(solution([],2)) #[]


# Method 1: create a dictionary to store new values of each index

def find_rotated_array(A,K):
    
    # Edge cases where K is the length of the array or K = 0 or the array only has one value
    if K % len(A) == 0 or len(set(A)) == 1 or len(A) == 0:
        return A
    
    idx_value_dict = {}

    K = K % len(A) # solve for cases where K > N

    for i in range(len(A)):
        if i + K > len(A) - 1:
            idx_value_dict[i+K-len(A)] = A[i]
        else:
            idx_value_dict[i+K] = A[i]
    
    for i in idx_value_dict:
        A[i] = idx_value_dict[i]
    
    return A

print(find_rotated_array([1,1,1,8],9)) #[8,1,1,1]


