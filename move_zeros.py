# Given an integer array nums, move all 0's to the end of it while maintaining the relative order 
# of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]


#==== Solution 1 (Brute force, O(n) time complexity, O(n) space complexity)====
def moveZeroes(nums):

    for i in range(len(nums)-2,-1,-1): #loop through the list in reverse
        if nums[i] == 0:
            nums[i:-1] = nums[i+1:] #update the array from the zero index to the 2nd to last element
            nums[-1] = 0 #update the last element to be 0


#==== Solution 2 (2 pointers, O(n) time complexity, O(1) space complexity)
def moveZeroes2(nums):

    lastNonZeroFound = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[lastNonZeroFound], nums[i] = nums[i], nums[lastNonZeroFound]
            lastNonZeroFound += 1

#moveZero([1,0,0,2,4]) #[1,2,4,0,0]