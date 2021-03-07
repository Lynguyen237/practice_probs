# [Codility] A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

# Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

# The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

# In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

# For example, consider array A such that:

#   A[0] = 3
#   A[1] = 1
#   A[2] = 2
#   A[3] = 4
#   A[4] = 3
# We can split this tape in four places:

# P = 1, difference = |3 − 10| = 7
# P = 2, difference = |4 − 9| = 5
# P = 3, difference = |6 − 7| = 1
# P = 4, difference = |10 − 3| = 7
# Write a function:

# def solution(A)

# that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

# For example, given:

#   A[0] = 3
#   A[1] = 1
#   A[2] = 2
#   A[3] = 4
#   A[4] = 3
# the function should return 1, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [2..100,000];
# each element of array A is an integer within the range [−1,000..1,000]


def min_abs_diff(A):
    total_sum = sum(A)
    min_diff = abs(total_sum - 2*A[0]) # suppose p = 1 is when the difference is minimum. See explanation below
    left_sum = 0

    for p in range(1,len(A)):
        left_sum += A[p-1] # As we increament p by 1, the sum of the left side of the array is incremented by A[p-1]
    
        abs_diff = abs(total_sum - 2*left_sum) # = abs(right_sum - left_sum) See explaination at the end below
  
        if abs_diff < min_diff:
            min_diff = abs_diff
    
    return min_diff

print(min_abs_diff([3,1,2,4,3])) #1
print(min_abs_diff([-3,-5])) # 2
print(min_abs_diff([0,2000])) # 2000
print(min_abs_diff([-3,100])) # 103
print(min_abs_diff([-3,100,99])) # 2

#====Explanation behind the math: why (right_sum - left_sum) = (total_sum - 2*left_sum)?
# A_sum = A[0] + A[1] + A[2] + ... + A[n-1]
# A_left_sum = LA = A[0] + A[1] + A[p-1]
# A_right_sum = RA = A[p]+ ... + A[n-1]
# Abs_diff = |RA - LA| = |RA + LA - 2*LA| = |A_sum - 2*LA| (no need to calculate RA)

