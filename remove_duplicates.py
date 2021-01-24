# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2]
# Explanation: Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the returned length.

# Example 2:
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4]
# Explanation: Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively. It doesn't matter what values are set beyond the returned length.

# METHOD 1
# Runtime 88 ms, memory 16 MB
def removeDuplicates(nums):

    index_to_change = 1

    for i in range(len(nums)-1):
        if nums[i] != nums[i+1]:
            nums[index_to_change] = nums[i+1]
            index_to_change += 1
    return index_to_change

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
print(removeDuplicates([1,1,2]))


# Pseudocode
    # Set the first index to change the value to j=1
    # Loop through range that is the length of the array
    # If the next number is not the same as the previous number, 
        # then replace slot index j with the next number. 
        # j+=1
    # Return j, which is the length of the array of only nonduplicated values.

    # 0,0 [0,0,1,1,1,2,2,3,3,4]
    # 0,1 [0,1,1,1,1,2,2,3,3,4] #1
    # 1,1 [0,1,1,1,1,2,2,3,3,4]
    # 1,1 [0,1,1,1,1,2,2,3,3,4]
    # 1,2 [0,1,2,1,1,2,2,3,3,4] #2


# Variation of method 1
# Runtime 92 ms, memory 16.1 MB
def removeDuplicates2(nums):

    if len(nums) == 0:
        return 0

    i = 0

    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i+1

print(removeDuplicates2([0,0,1,1,1,2,2,3,3,4]))
print(removeDuplicates2([1,1,2]))