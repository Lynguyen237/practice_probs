# Codility - lesson 5
# Write a function:

# def solution(A, B, K)

# that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

# { i : A ≤ i ≤ B, i mod K = 0 }

# For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

# Write an efficient algorithm for the following assumptions:

# A and B are integers within the range [0..2,000,000,000];
# K is an integer within the range [1..2,000,000,000];
# A ≤ B.

#==== Solution (https://stackoverflow.com/questions/25661519/find-the-number-of-multiples-for-a-number-in-range)
def solution(A, B, K):
    # Number of integer in the range [1 .. X] that divisible by K is X/K. 
    # So, within the range [A .. B], the result is B/K - (A - 1)/K
    b = B//K
    if A > 0:
        a = (A-1) // K
        return (b-a)
    else:
        return b+1

# Test cases: 
# [5,7,11] # 0
# [0,1,10] # 1
# [0,12,3] # 5

#==== First Solution, time complexity O(1)
def solution(A, B, K):
    ans = 0

    if A != 0 and B < K: # if the end value is greater than K and the beginning value is not 0
        return ans # there's 0 number divisible by K
    

    remainder = A % K

    if remainder == 0: # if A is divisible by K
        ans = (B-A) // K + 1
    else:
        if A > K: # if A is greater than K, then the first divisible value will be A + K - remainder
            first_divisible_no = A + K - remainder
        else:
            first_divisible_no = K # if A is smaller than K, then the first divisible value is K itself
        
        if B < first_divisible_no: # if B is smaller than K itself, there's no number divible by K in the range
            return 0
        else:
            ans = (B - first_divisible_no) // K + 1
    
    return ans


#Lesson learned: Test A = B, test extreme value, test for 0