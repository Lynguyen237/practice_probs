# [Codility] Write a function:

# def solution(A)

# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

# Given A = [1, 2, 3], the function should return 4.

# Given A = [−1, −3], the function should return 1.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].


# Solution
def solution(a):
    A = set(a)
    ans = 1
    while ans in A:
       ans += 1
    return ans

print(solution([1, 3, 6, 4, 1, 2])) #5
print(solution([-1,-9,-3,1])) #2
print(solution([-1,-9,-3,5])) #1
print(solution([-100000])) #1
print(solution([4,5])) #3

# Attempted incorrect solution - not covering cases where the answer is smaller than the smallest first integer [3,4,5]
# def solution(A):
        
#     B = sorted(A) #sort the array
    
#     # Edge cases: list length 0, all negative numbers
#     if len(B) == 0 or B[-1] < 0: 
#         return 1

#     # Edge case: 2nd to last number < 0 and last number > 1
#     if B[-2] < 0 and B[-1]>0:
#         if B[-1] == 1:
#             return 2
#         return B[-1]-1

    # for i in range(len(B)-1):
    #     if B[i] > 0 and B[i+1] != B[i]+1 and B[i] != B[i+1]:
    #         return B[i]+1
    
    # return B[-1]+1



