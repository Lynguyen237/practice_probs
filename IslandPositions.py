'''
You are given an m x n binary matrix grid. An island is a group of 1's (representing land)
connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid 
are surrounded by water. The area of an island is the number of cells with a value 1 in the island.

Return a list of lists, each of which is an array of tuples containing the positions of 
all the cells forming the island.

Example:
1 0 0
1 0 1
-> [[(0,0),(1,0)],[(1,2)]]
'''

matrix1 = [
            [1,0,0],
            [1,0,1]
          ]

def IslandPositions(grid):

    def storePositions(grid, r, c, lst):

        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            return
        
        if grid[r][c] != 1:
            return
        
        elif grid[r][c] == 1:
            lst.append((r,c))
            grid[r][c] = "x"
            storePositions(grid, r-1, c, lst) #above
            storePositions(grid, r+1, c, lst) #below
            storePositions(grid, r, c-1, lst) #left
            storePositions(grid, r, c+1, lst) #above

    ans = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                lst = []
                storePositions(grid, r, c, lst)
                ans.append(lst)

    return ans


a = IslandPositions(matrix1)

assert a == [[(0,0),(1,0)],[(1,2)]]


