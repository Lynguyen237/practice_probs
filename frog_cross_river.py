# A small frog wants to get to the other side of a river. The frog is initially located on 
# one bank of the river (position 0) and wants to get to the opposite bank (position X+1). 
# Leaves fall from a tree onto the surface of the river.

# You are given an array A consisting of N integers representing the falling leaves. 
# A[K] represents the position where one leaf falls at time K, measured in seconds.

# The goal is to find the earliest time when the frog can jump to the other side of the river. 
# The frog can cross only when leaves appear at every position across the river from 1 to X 
# (that is, we want to find the earliest moment when all the positions from 1 to X are covered by leaves). 
# You may assume that the speed of the current in the river is negligibly small, 
# i.e. the leaves do not change their positions once they fall in the river.

# For example, you are given integer X = 5 and array A such that:

#   A[0] = 1
#   A[1] = 3
#   A[2] = 1
#   A[3] = 4
#   A[4] = 2
#   A[5] = 3
#   A[6] = 5
#   A[7] = 4
# In second 6, a leaf falls into position 5. This is the earliest time when leaves appear in every position across the river.

# Write a function:

# def solution(X, A)

# that, given a non-empty array A consisting of N integers and integer X, returns the earliest time when the frog can jump to the other side of the river.

# If the frog is never able to jump to the other side of the river, the function should return −1.
# Write an efficient algorithm for the following assumptions:

# N and X are integers within the range [1..100,000];
# each element of array A is an integer within the range [1..X].

#==== METHOD 1 =====
def frog_cross_river(X, A):
    
    if len(A) < X:
        return -1

    current_path_set = set() # Empty set to track the current path as we loop through the array later
    
    for i in range(len(A)):
        current_path_set.add(A[i]) # Add the position to the current_path
        if len(current_path_set) == X: # If the length of the current path is the same as the number of steps needed 
            return i

    return -1

print(frog_cross_river(5, [1,3,1,4,2,3,5,4])) #6
print(frog_cross_river(3, [1, 3, 1, 3, 2, 1, 3])) #4


#==== METHOD 2 ====
def frog_cross_river2(X, A):
    leaf_fallen, sum_step = [False] * X, 0
    
    for sec, position in enumerate(A):
        
        if not(leaf_fallen[position-1]): # if the leave in a current position is not falling yet (if not False)
            leaf_fallen[position-1] = True # change the value of the leaf_fallen[position-1] to True
            sum_step += 1 # Increment the total step by 1
            
            if sum_step == X : # if the number of steps is X, then return the current time
                return sec
    
    return -1

print(frog_cross_river2(5, [1,3,1,4,2,3,5,4])) #6
print(frog_cross_river2(3, [1, 3, 1, 3, 2, 1, 3])) #4
