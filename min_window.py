# https://leetcode.com/problems/minimum-window-substring/solution/
# Given two strings s and t, return the minimum window in s
# which will contain all the characters in t. 
# If there is no such window in s that covers all characters in t, 
# return the empty string "".

# Note that If there is such a window, 
# it is guaranteed that there will always
# be only one unique minimum window in s.

# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"

# Example 2:
# Input: s = "a", t = "a"
# Output: "a"

# Pseudocode:
# a: 1, b: 1, c: 1
# a:10, b:9, c:12, min_len = 6

# s = "ADOBECODEBANC", t = "ABC"

def min_window(s, k)

  # create a a dictionary of the substring
  k_dict = {}
  for char in k:
    k_dict[char] = k_dict.get(char, 0) + 1


  # Create a dictionary for each window
  def make_dict(window):
    window_dict = {}
    for char in window:
      if char in k_dict:
        window_dict[char] = window_dict.get(char, 0) + 1
    return window_dict

    
  # Determine of a window is a valid window
  def valid_window(window_dict):
    if len(window_dict) != len(k_dict):
      return False

    for key in window_dict:
      if window_dict[key] < k_dict[key]:
        return False
    return True


  min_len = len(s)+1 # Max length, if exists, will be the length of the string
  ans = "No minimum window found"

  # Loop through the string and examine possible windows
  for i in range(len(s)):
    for j in range(i,len(s)+1):
      window = s[i:j]
      # Proceed to examine the window if its length is at list the length of k
      if len(window) >= len(k):
        window_dict = make_dict(window) # Create a dictionary for the window
        if valid_window(window_dict): # If the window is valid
          if len(window) < min_len: # Check if the len of the window is smaller than min_len
            min_len = len(window)
            ans = window
    
  return ans

# keep this function call here 
print(MinWindowSubstring(input()))

'''
1. For input ["aaabaaddae", "aed"] the output was incorrect. The correct output is dae

2. For input ["aaffsfsfasfasfasfasfasfacasfafe", "fafe"] the output was incorrect. The correct output is fafe

3. For input ["caae", "cae"] the output was incorrect. The correct output is caae
'''