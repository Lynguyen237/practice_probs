'''
https://leetcode.com/problems/number-of-islands/
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
'''

#==== Solution 1, recursion ====

def count_islands(matrix):
    
    def dfs(i, j, matrix):
        if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]) and matrix[i][j] == '1':
            matrix[i][j] = "x" # Turn "1" into "x" to indicate that we have already checked this cell
            dfs(i-1, j, matrix) #above
            dfs(i+1, j, matrix) #below
            dfs(i, j-1, matrix) #left
            dfs(i, j+1, matrix) #right

    
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '1':
                dfs(i, j, matrix)
                count += 1 # After checking/marking all the neighbors with the dfs function, increment the island count by 1
    
    return count

grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(count_islands(grid1))
print(count_islands(grid2))

#==== Solution 1B - slightly different way to unpack recursion ====
# Count islands
def count_islands2(matrix):

  count = 0
  
  for r in range(len(matrix)):
    for c in range(len(matrix[r])):
      if matrix[r][c] == "1":
        dfs(r,c, matrix)
        count += 1
  
  return count

# DFS
def dfs(r, c, matrix):

  if r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[0]): # End the current dfs if the r & c are out of bounds
    return
  
  if matrix[r][c] == "X" or matrix[r][c] == "0": # End the current dfs if the cell is either 0 or has been checked before
    return
  
  matrix[r][c] = "X"
  
  dfs(r, c-1, matrix) #left
  dfs(r, c+1, matrix) #right
  dfs(r-1, c, matrix) #up
  dfs(r+1, c, matrix) #down