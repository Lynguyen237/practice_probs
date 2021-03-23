# Codility - Lesson 5, prefix_sum https://codility.com/media/train/3-PrefixSums.pdf
# A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N, is called a slice of array A (notice that the slice contains at least two elements). The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice. To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

# For example, array A such that:

#     A[0] = 4
#     A[1] = 2
#     A[2] = 2
#     A[3] = 5
#     A[4] = 1
#     A[5] = 5
#     A[6] = 8
# contains the following example slices:

# slice (1, 2), whose average is (2 + 2) / 2 = 2;
# slice (3, 4), whose average is (5 + 1) / 2 = 3;
# slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
# The goal is to find the starting position of a slice whose average is minimal.

# Write a function:

# def solution(A)

# that, given a non-empty array A consisting of N integers, returns the starting position of the slice with the minimal average. If there is more than one slice with a minimal average, you should return the smallest starting position of such a slice.

# For example, given array A such that:

#     A[0] = 4
#     A[1] = 2
#     A[2] = 2
#     A[3] = 5
#     A[4] = 1
#     A[5] = 5
#     A[6] = 8
# the function should return 1, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [2..100,000];
# each element of array A is an integer within the range [−10,000..10,000].

#==== Solution 1 - 100% correct but failing performance. O(n^2)
# https://app.codility.com/demo/results/trainingRE9ZGT-M6P/

def solution(A):
    min_avg = sum(A[0:2])/2
    starting_point = 0

    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if sum(A[i:j+1])/len(A[i:j+1]) < min_avg:
                min_avg = sum(A[i:j+1])/len(A[i:j+1])
                starting_point = i
    
    return starting_point

#==== Optimal solution https://codesays.com/2014/solution-to-min-avg-two-slice-by-codility/
# It is based on math proving that:
# (1) There must be some slices, with length of two or three, having the minimal average value among all the slices.
# (2) And all the longer slices with minimal average are built up with these 2-element and/or 3-element small slices.


# test
# [-1,1,2,3] #0
# [7,6,5,4,3] #3
# [5,9,9,5,9] #0
# [1000,99,50,-100] #2
# [0,100,-10,100] #0

# Prefix Sums Explained
def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)

    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    
    return P

print(prefix_sums([1,2,3,4,5])) # [0, 1, 3, 6, 10, 15]