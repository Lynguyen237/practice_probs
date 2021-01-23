# https://leetcode.com/problems/search-in-rotated-sorted-array/
# You are given an integer array nums sorted in ascending order (with distinct values), and an integer target.

# Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# If target is found in the array return its index, otherwise, return -1.

# Method 1
def search1(nums, target):

    if target >= nums[0]:
        for i in nums:
            if target == i:
                return nums.index(i)
    
    if target <= nums[0]:
        i = len(nums)-1
        while i >=0:
            if target == nums[i]:
                return i
            i -= 1
    
    return (-1)


# Method 2: Find the pivot (O(log n)) => binary search on one of the half

def search(nums, target):

    # Find the index of the pivot number
    for i in range(len(nums)-1):
        if nums[i]>nums[i+1]:
            pivot_idx = i+1
            return pivot_idx

    # if target >= nums[0]:
    #     # binary search on the first half - nums[0:pivot_idx]
    #     mid_idx = len(nums[0:pivot_idx])/2
    #     if target == nums[mid_idx]:
    #         return mid_idx
    #     # elif target > nums[mid_idx]:
            
    #     # binary search on the second half - nums[pivot_idx:]

def binarysearch(lst, target):
    mid_idx = 0
    
    if len(lst)>1:
        mid_idx = len(lst)//2
     
    print(mid_idx, lst[mid_idx], target)
    if target == lst[mid_idx]:
        return mid_idx
    elif target > lst[mid_idx]:
        binarysearch(lst[mid_idx:], target)
    elif target < lst[mid_idx]:
        binarysearch(lst[:mid_idx], target)

# [4,5,6,7,0,1,2] #2nd half always smaller
print(search([0,1,2,4,5,6,7],2)) #2
print(search([4,5,6,7,0,1,2],2)) #6
print(search([4,5,6,7,0,1,2],3)) #-1
print(search([4,5,6,7,0,1,2],8)) #-1
print(binarysearch([0,1,2],2))
