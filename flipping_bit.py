# [Hackerrank] https://www.hackerrank.com/challenges/flipping-bits/problem
# XOR operator tutorial: https://www.youtube.com/watch?v=0zWiugtOMd4

# You will be given a list of 32 bits unsigned integers. 
# You are required to output the list of the unsigned integers you get by flipping bits in its binary representation 
# (i.e. unset bits must be set, and set bits must be unset).
# Example:
# n  = 9 
# bin(9) = 1001
# we are working with 32 bit so:
# 00000000000000000000000000001001 = 9 (base 10)
# 11111111111111111111111111110110 = 4294967286 (base 2)

def flippingBits(n):
    
    binary_n = "{:032b}".format(n) # Turn n into a binary representation of 32 bits
    ans='' # Create an empty string holding the answer in the binary format
    
    # Loop through the digit in the string, flip it, and add to the ans string
    for i in binary_n: 
        if i == '0':
            ans += '1'
        else:
            ans += '0'
    
    # Convert the binary (base 2) number into decimal
    return int(ans, 2)


def flippingBits_xor(n):
    #Binary number of 2**31 - 1 (4294967295) is all ones
    #Hence we can xor each bit of the binary representation of n
    #with the binary representation of 2**31 - 1
    return n ^ (2**32-1)


def test_flippingBits_xor():

    #assert raises AssertionError if expression is False, otherwise the test finishes running
    assert flippingBits_xor(2147483647) == 2147483648
    assert flippingBits_xor(1) == 4294967294
    assert flippingBits_xor(0) == 4294967295


test_flippingBits_xor()

# test with assert method: https://www.tryexponent.com/courses/algorithms/number-finder