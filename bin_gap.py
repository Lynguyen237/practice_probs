# A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

# For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

# Write a function:

# def solution(N)

# that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

# For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..2,147,483,647].


#### Method 1 - Create a list to store the indices of one

def solution(N) -> int:
    # Get the binary representation of integer N
    N_bin = list(bin(N))[2:]

    # Create an empty list to store the indices of ones
    one_lst = []

    for i in range(len(N_bin)):
        if N_bin[i] == '1':
            one_lst.append(i)
    
    max_bin_gap = 0

    # If the gap between the 2 consecutive indices is greater than the max max_bin_gap, 
    # reassign the max value
    for i in range(len(one_lst)-1):
        current_gap = one_lst[i+1] - one_lst[i] -1
        if current_gap > max_bin_gap:
            max_bin_gap = current_gap
    
    return max_bin_gap


print(solution(9)) #2



#### Method 2 - Use rstrip and split

def bin_gap(N) -> int:
    
    # Get the binary representation of integer N
    # Alternative method: N_bin = format(N, 'b')
    N_bin = bin(N)[2:] #string
    
    # List of the substrings split by 1 and stripped off zeroes on the right handside
    gap_lst = N_bin.strip('0').split('1')

    return len(max(gap_lst))


print(bin_gap(9)) #2
print(bin_gap(805306373)) #25
