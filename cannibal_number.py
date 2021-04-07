# In an array of “cannibal numbers,” a number can “eat” the next number in the sequence if it is 
# greater than that number. When numbers “eat” each other, they are added together. 
# Given an array of numbers, return the resulting array after the numbers are allowed to “eat” each other, 
# for example, [3, 2, 6] becomes [5, 6]; [6, 9, 4, 12] becomes [6, 25]; [2, 1, 1] becomes [4].

#==== Solution 1 (time complexity O(n), space complexity O(n)) ====
def cannibal_number(arr):

    if len(arr) <= 1:
        return arr

    ans = []

    for i in range(len(arr)-1):
        print(i, arr[i], arr[i+1])
        if arr[i] < arr[i+1]:
            ans.append(arr[i])
        else:
            arr[i+1] += arr[i]
    ans.append(arr[i+1])
    
    return ans

# print(cannibal_number([6, 9, 4, 12])) # [6, 25]
# print(cannibal_number([3,2,6])) #[5, 6]
# print(cannibal_number([2,1,1])) #[4]
# print(cannibal_number([2,1])) #[3]
# print(cannibal_number([i for i in range(9,0,-1)]))#[45]
# print(cannibal_number([2])) #[2]
# print(cannibal_number([])) #[]
# print(cannibal_number([-2,1])) #[-2,1]

