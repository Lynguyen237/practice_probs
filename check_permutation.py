# Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.

# god, dog => permutation
# god, odg => permutation
# the, cat # not permutation
# good dog # not a permutation

def check_permutation(string1, string2):
    # check for length:
        # if not equal, return false
        # if equal:
            
            # turn string1 into a list
            # loop through each character in string2:
                # if character in the list, pop the character from the list
            # if the string1 list is empty:
                # return true
    
    if len(string1) != len(string2):
        return False
    
    
    string1_dict = {}
    for letter in string1:
        if letter not in string1_dict:
            string1_dict[letter] = 1
        else:
            string1_dict[letter] += 1

    # string1_lst = list(string1)
    # for letter in string2:
    #     if letter in string1_lst:
    #         string1_lst.pop(string1_lst.index(letter))
    
    # if len(string1_lst) == 0:
    #     return True

    for letter in string2:
        print(letter)
        if letter not in string1_dict:
            return False
        
        if letter in string1_dict:
            string1_dict[letter] -= 1
    
    if set(string1_dict.values()) == {0}:
        return True
            
    
    return False

print(check_permutation("god", "dogo")) # false
print(check_permutation("god", "dog")) # true
print(check_permutation("god", "cat")) # false
print(check_permutation("", "")) # true