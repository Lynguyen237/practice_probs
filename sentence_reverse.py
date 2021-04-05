# You are given an array of characters arr that consists of sequences of characters separated by 
# space characters. Each space-delimited sequence of characters defines a word.

# Implement a function reverseWords that reverses the order of the words in the array in the 
# most efficient manner. Explain your solution and analyze its time and space complexities.

# Example:

# input:  arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
#                 'm', 'a', 'k', 'e', 's', '  ',
#                 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]

# output: [ 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', '  ',
#           'm', 'a', 'k', 'e', 's', '  ',
#           'p', 'e', 'r', 'f', 'e', 'c', 't' ]

# 0 ≤ arr.length ≤ 100

#==== Solution ====
# O(n) time complexity, O(1) space complexity

# @ word is a list of letters
def reverseChar(word, i, j):
    while i < j:
        word[i], word[j] = word[j], word[i]
        i += 1
        j -= 1

    return word

def reverseWords(arr):
    
    if ' ' not in arr or len(arr) <= 1:
        return arr

    arr = reverseChar(arr, 0, len(arr)-1) #reverse the whole array

    #reverse the letters in each word
    start_idx = 0
    end_idx = start_idx - 1
    for i in range(len(arr)):
        if arr[i] != " ":
            end_idx += 1 
        else:
            reverseChar(arr, start_idx, end_idx)
            start_idx = i+1
            end_idx += 1
        if i == len(arr) -1:
            reverseChar(arr, start_idx, end_idx) #reverse the last word in the array
    
    return arr


#==== Solution B (small tweak to reverseWords function) ====
def reverseWords2(arr):

    if ' ' not in arr or len(arr) <= 1:
        return arr

    arr = reverseChar(arr, 0, len(arr)-1) #reverse the whole array

    #reverse the letters in each word
    word_start_idx = None

    for i in range(len(arr)):
        if word_start_idx == None:
            word_start_idx = i
        if arr[i] == " ":
            reverseChar(arr, word_start_idx, i-1)
            word_start_idx = None
        elif i == len(arr) - 1:
            reverseChar(arr, word_start_idx, i)
    
    return arr

#==== Solution C (small tweak to reverseWords function) ====
def reverseWords3(arr):

    if ' ' not in arr or len(arr) <= 1:
        return arr

    arr = reverseChar(arr, 0, len(arr)-1) #reverse the whole array

    #reverse the letters in each word
    word_start_idx = None

    for i in range(len(arr)):
        if arr[i] == " ":
            if word_start_idx != None:
                reverseChar(arr, word_start_idx, i-1)
                word_start_idx = None
        elif i == len(arr) - 1:
            if word_start_idx != None:
                reverseChar(arr, word_start_idx, i)
        else:
            if word_start_idx == None:
                word_start_idx = i
    
    return arr

#==== Testing ====
arr0 = []
arr1 = [' ']
arr2 = ['j']
arr3 = ['h',' ',' ','H']
arr4 = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', ' ',' ',
        'm', 'a', 'k', 'e', 's', ' ',
        'p', 'r', 'a', 'c', 't', 'i', 'c', 'e']

test = [arr0, arr1, arr2, arr3, arr4]

for arr in test:
    print(arr)
    print(reverseWords(arr))

