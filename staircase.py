'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

https://leetcode.com/problems/climbing-stairs/discuss/?currentPage=1&orderBy=hot&query= 
'''

class Stairs:

    def __init__(self):
        self.stairs = {}
    
    def find_unique_way(self, n):

        if n in self.stairs:
            return self.stairs[n]

        elif n == 1 or n == 0:
            return 1

        elif n < 0:
            return 0
        
        total = self.find_unique_way(n-1) + self.find_unique_way(n-2)
        self.stairs[n] = total

        return total

stair1 = Stairs()
stair1.find_unique_way(5)

