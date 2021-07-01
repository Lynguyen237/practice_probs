'''
You're given a two-dimensional array of distinct integers and a target integer. 
Each row in the matrix is sorted, and each colunm is also sorted; 
the matrix doesn't necessarily have the same height and width.

Write a function that returns an array of the row and column indices of the target integer 
if it's contained in the matrix, otherwise return [-1, -1]

Optimal solution is O(n+m)time O(1)space

matrix = [
            [1,  4,   7,   12,  15, 1000],
            [2,  5,   19,  31,  32, 1001],
            [3,  8,   24,  33,  35, 1002],
            [40, 41,  42,  44,  45, 1003],
            [99, 100, 103, 106, 128, 1004]
          ]

target = 44 => return [3,3]
target = 46 => return [-1,-1]
'''

matrix = [
            [1,  4,   7,   12,  15, 1000],
            [2,  5,   19,  31,  32, 1001],
            [3,  8,   24,  33,  35, 1002],
            [40, 41,  42,  44,  45, 1003],
            [99, 100, 103, 106, 128, 1004]
          ]

# ==== Solution 1 - start from the top right corner ====
def find_target(matrix, target):
    
    # Start from the top right corner
    r = 0
    c = len(matrix[0]) - 1

    while c >= 0 and r < len(matrix):

        if target < matrix[r][c]:
            c -= 1
        elif target > matrix[r][c]:
            r += 1
        else:
            return [r,c]    
    return [-1,-1]


assert find_target(matrix, 44) == [3,3]
assert find_target(matrix, 46) == [-1,-1]
assert find_target(matrix, 35) == [2,4]
assert find_target(matrix, 1003) == [3,5]

