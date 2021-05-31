# https://www.tutorialspoint.com/remove-all-adjacent-duplicates-in-string-in-python
# Advanced: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
# Suppose we have a string S of lowercase letters; a duplicate removal operation will be performed. 
# This will be done by choosing two adjacent and equal letters, and removing them.

# We will repeatedly remove duplicates from S until no duplicates are remaining.

# Return the string after all such duplicate removals have been completed. 
# It is guaranteed that the answer is unique.

# Suppose the string is “abbacaca”, then answer will be “caca”. 
# At first delete duplicates bb, then string is “aacaca”, then remove aa, then string is “caca”, 
# then no such duplicates are there.

def remove_adjacent_duplicates(s):
    if len(s) == 1:
            return s
        
    stack = []
    
    for char in s: 
        if not stack:
            stack.append(char)
        
        elif char == stack[-1]:
            stack.pop()
        
        elif char != stack[-1]:
            stack.append(char)
    
    return "".join(stack)

# Test
assert remove_adjacent_duplicates("abbaca") == "ca"