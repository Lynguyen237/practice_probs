# https://www.pramp.com/challenge/XdMZJgZoAnFXqwjJwnpZ
# Pairs with Specific Difference
# Given an array arr of distinct integers and a nonnegative integer k, write a function findPairsWithGivenDifference that returns an array of all pairs [x,y] in arr, such that x - y = k. If no such pairs exist, return an empty array.

# Note: the order of the pairs in the output array should maintain the order of the y element in the original array.

# Examples:

# input:  arr = [0, -1, -2, 2, 1], k = 1
# output: [[1, 0], [0, -1], [-1, -2], [2, 1]]

def find_pairs_with_given_difference(arr, k):

  result = []
  
  
  for i in arr:
   if i-k in arr:
      result.append([i,i-k])
    
  
 return result



# SOLUTION
def find_pairs_with_given_difference(arr, k):

    if k == 0:
    return []
        
    map = {}
    answer = []
        
    for x in arr:
        map[x - k] = x

    for y in arr:
        if y in map:
            answer.append([map[y], y]) 

    return answer