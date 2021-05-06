"""
Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"
 
Your task is to process a string with "#" symbols.
 
Examples
"abc#d##c"      ==>  "ac"
"abc##d######"  ==>  ""
"#######"       ==>  ""
""              ==>  ""
"#abc#d#efgh##" ==>  "abef"
"""
s1 = "abc#d##c"
s2 = "abc##d######"
s3 = "#######"
s4 = "#abc#d#efgh##" 

# ==== Solution 1 - Using Stack ====

def backspace(s):

    stack = []

    for i in range(len(s)):
        if s[i] != "#":
            stack.append(s[i])
        else:
            if stack:
                stack.pop()
    
    return "".join(stack)

assert backspace("abc#d##c") == "ac", "Expected output: 'ac'"
assert backspace("#abc#d#efgh##") == "abef", "Expected output: 'ac'"
assert backspace("#a######") == "", "Expected output: '' "


# ==== Solution 2 - Looping backward ====
def backspace2(s):

    pound_count = 0
    ans = ''

    for i in range(len(s)-1, -1, -1):
        print(i)
        if s[i] != "#":
            if pound_count == 0:
                ans = s[i] + ans[0:]
            elif pound_count > 0:
                pound_count -= 1
        elif s[i] == "#":
            pound_count += 1
    
    return ans

assert backspace2("abc#d##c") == "ac", "Expected output: 'ac'"
