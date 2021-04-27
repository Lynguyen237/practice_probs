# https://www.geeksforgeeks.org/find-next-greater-number-set-digits/
# Given a number n, find the smallest number that has same set of digits as n and is greater than n. 
# If n is the greatest possible number with its set of digits, then print “not possible”.

# Examples: 
# For simplicity of implementation, we have considered input number as a string. 

# Input:  n = "218765"
# Output: "251678"

# Input:  n = "1234"
# Output: "1243"

# Input: n = "4321"
# Output: "Not Possible"

# Input: n = "534976"
# Output: "536479"

def next_greater_num(n):

    lst = list(n)

    for digit in lst:
        int(digit)
    
    # Start from the right most digit and find the first
    # digit that is smaller than the digit next to it
    for i in range(len(n)-1, 0, -1):
        if lst[i] > lst[i-1]:
            break
    
    # If no such digit found,then all numbers are in descending order, 
    # we can't find a greater number using the same set of digits
    if i == 1 and lst[i] < lst[i-1]:
        return "Impossible"

    # If such a digit is found, we find the smallest digit to the right of (i-1)th digit
    # that is still greater than the (i-1)th digit. 
    smallest_idx = i 
    smallest_digit = lst[smallest_idx]
    for j in range(i+1, len(n)):
        if lst[j] > lst[i-1] and lst[j] < smallest_digit:
            smallest_idx = j
    
    # Swapping the above found smallest digit with (i-1)'th
    lst[i-1], lst[smallest_idx] = lst[smallest_idx], lst[i-1]

    # Sort the rest of the digits to the right of (i-1)th digit in ascending order
    lst[i:] = sorted(lst[i:])
    return "".join(lst)
                

print(next_greater_num("4321")) #Impossible
print(next_greater_num("1234")) #1243
print(next_greater_num("534976")) #536479

