# Given an unsorted array and a number n, find if there exists a pair of elements 
# in the array whose difference is n.

# Input: arr[] = {5, 20, 3, 2, 50, 80}, n = 78
# Output: Pair Found: (2, 80)

# Input: arr[] = {90, 70, 20, 80, 50}, n = 45
# Output: No Such Pair

arr1 = [5, 20, 3, 2, 50, 80]
arr2 = [90, 70, 20, 80, 50]
arr3 = [1, 8, 30, 40, 100]

def find_pair(arr, n):

    arr.sort()

    l = 0
    r = len(arr) - 1

    while l < r:
        if arr[r] - arr[l] == n:
            return (arr[l], arr[r])
        elif arr[r] - arr[l] > n:
            l += 1
        else:
            r -= 1

    return None

assert find_pair(arr1, 78) == (2,80)
assert find_pair(arr2, 45) == None
assert find_pair(arr3, 60) == (40, 100)


