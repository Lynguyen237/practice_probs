# https://leetcode.com/problems/single-number/
# Given a non-empty array of integers nums, every element appears twice except for one. 
# Find that single one.

# Follow up: Could you implement a solution with a linear runtime complexity and 
# without using extra memory?

# Input: nums = [2,2,1]
# Output: 1

# Input: nums = [1]
# Output: 1


#==== SOLUTION 1 - Use dictionary ====
def singleNumber(nums):
    
    if len(nums) == 1:
        return nums[0]
    
        # build a dictionary {array_element: count}
        count_dict = {}
    
        for i in nums:
            if i not in count_dict:
                count_dict[i] = 1
            else:
                count_dict[i] += 1
    
        for key,value in count_dict.items():
            if value == 1:
                return key


#==== SOLUTION 2 - Math ====
def singleNumber(nums):

    if len(nums) == 1:
        return nums[0]

    nums_set = set(nums) # create a set of from the array
    nums_set_sum = sum(nums_set) # calculate the sum of the set

    nums_arr_sum = sum(nums) # calculate the sum of the array

    # the difference between 2x the sum of the set and the the sum of the array is the answer
    ans = nums_set_sum*2 - nums_arr_sum 

    return ans


#==== SOLUTION 3 - Using set ====
def singleNumber(nums):

    if len(nums) == 1:
        return nums[0]
    
    tracking_set = set()

    for i in nums:
        if i not in tracking_set:
            tracking_set.add(i)
        else:
            tracking_set.remove(i)
    
    return tracking_set.pop()