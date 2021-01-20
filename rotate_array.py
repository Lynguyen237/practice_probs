# https://leetcode.com/problems/search-in-rotated-sorted-array/

def search(nums, target):

    #Method 1
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

#find the pivot (O(log n)) => binary search on one of the half => MEMEORIZE
    for i in range(len(nums)):
        if nums[i]>nums[i+1]:
            pivot_idx=i+1


# [4,5,6,7,0,1,2] #2nd half always smaller
search([0,1,2,4,5,6,7],2) #2
search([4,5,6,7,0,1,2],2) #6
search([4,5,6,7,0,1,2],3) #-1
search([4,5,6,7,0,1,2],8) #-1
