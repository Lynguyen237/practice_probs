# Return the index of the first occurrence of an anagram of needed in a haystack, or -1 if needle is not part of haystack.
# "actor", "cat" => return 0
# "act" is an anagram of "cat"

#==== Solution using a helper function comparing two dictionaries each time
def anagrammedIndexOf_helper(haystack, needle):
    
    if len(needle) > len(haystack):
        return -1 
    
    if not needle or not haystack:
        return -1
        
    # Create a needle dictionary
    nDict = {}
    
    for c in needle:
        nDict[c] = nDict.get(c, 0) + 1

    
    for i in range(len(haystack)-len(needle)+1):
        if haystack[i] in nDict:
            subStr = haystack[i:i+len(needle)]
            if helper(subStr, nDict):
                return i 
    
    return -1

            
def helper (subStr, nDict):
        
    for c in subStr:
        if c not in nDict:
            return False
        else:
            nDict[c] -= 1
        if nDict[c] == 0:
            nDict.pop(c)
        
    
    if not nDict:
        return True
    
    return False


#==== Solutions using 2 pointers and have a rolling dictionary. However, it still requires comparing the dictionaries
def anagrammedIndexOf(haystack, needle):
    
    if len(needle) > len(haystack):
        return -1 
    
    if not needle or not haystack:
        return -1
        
    # Create a needle dictionary
    nDict = {}
    
    for c in needle:
        nDict[c] = nDict.get(c, 0) + 1
    

    l = 0
    r = len(needle)-1

    rollingWindow = {}
    for c in haystack[l:r+1]:
        rollingWindow[c] = rollingWindow.get(c, 0) + 1

    while r < len(haystack):
        if rollingWindow == nDict:
            return l

        else:
            rollingWindow.pop(haystack[l])
            l += 1
            r += 1
            if r < len(haystack):
                rollingWindow[haystack[r]] = rollingWindow.get(haystack[r], 0) + 1
    
    return -1
            

print(anagrammedIndexOf("actor", "cate")) #-1
print(anagrammedIndexOf("actor", "cat")) #0
print(anagrammedIndexOf("hell", "ll")) #2
print(anagrammedIndexOf("cbaebabacd", "abc")) #0
assert anagrammedIndexOf("actor", "cat") == 0

