# print("Hello")
# Lonely pixel problem.
#
# 0 0 0 1 0
# 0 1 0 0 0
# 1 0 0 0 0
# 1 0 0 0 0
# 0 0 0 0 1
#
#
# A pixel is "lonely" if it is the only pixel activated in its row and column. 
# Find the lonely pixels.

grid0 = [[0, 1],
         [0, 0]]
grid1 = [[0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0],
         [1, 0, 0, 0, 0],
         [1, 0, 0, 0, 0],
         [0, 0, 0, 0, 1]]

def pixelLonely(grid):
  rowMap = {}
  colMap = {}
  
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if grid[r][c] == 1:
        rowMap[r] = rowMap.get(r, 0) + 1
        colMap[c] = colMap.get(c, 0) + 1
  
  ans = []
  for row, count in rowMap.items(): #0
    if count == 1: #1
      for col in range(len(grid[0])):
        if grid[row][col] == 1 and colMap[col] == 1:
            ans.append((row,col))
  
  return ans

assert pixelLonely(grid0) == [(0,1)]
assert pixelLonely(grid1) == [(0, 3), (1, 1), (4, 4)]
