# A non-empty array A consisting of N integers and sorted in a non-decreasing order (i.e. A[0] ≤ A[1] ≤ ... ≤ A[N−1]) is given. The leader of this array is the value that occurs in more than half of the elements of A.

# You are given an implementation of a function:

# class Solution { public int solution(int[] A); }

# that, given a non-empty array A consisting of N integers, sorted in a non-decreasing order, returns the leader of array A. The function should return −1 if array A does not contain a leader.

# For example, given array A consisting of ten elements such that:

#   A[0] = 2
#   A[1] = 2
#   A[2] = 2
#   A[3] = 2
#   A[4] = 2
#   A[5] = 3
#   A[6] = 4
#   A[7] = 4
#   A[8] = 4
#   A[9] = 6
# the function should return −1, because the value that occurs most frequently in the array, 2, occurs five times, and 5 is not more than half of 10.

# Given array A consisting of five elements such that:

#   A[0] = 1
#   A[1] = 1
#   A[2] = 1
#   A[3] = 1
#   A[4] = 50
# the function should return 1.

# Assume that:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [0..2,147,483,647];
# array A is sorted in non-decreasing order.
# In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.

def find_leader(lst):

    #edge case
    if len(lst) < 1:
        return -1

    #find the min frequency of the leader
    leader_frq = len(lst)/2
    # print(f'length: {len(lst)}, leader_frq: {leader_frq}')

    count = 0
    leader = lst[0]

    #loop through the list, keep count of the frequency & reassign leader if count > len(lst)/2
    for i in range(len(lst)-1):
        if lst[i+1] == lst[i]:
            count += 1
            # print(f'{lst[i]}, count {count}')
        else:
            if count >= leader_frq:
                leader = lst[i]
                return leader
            count = 1
    
    return -1

print(find_leader([2,2,2,2,2,3,4,4,4,6]))
print(find_leader([2,2,2,2,2,5]))
print(find_leader([2]))