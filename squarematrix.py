# Feedback: https://docs.google.com/document/d/1_lF43Zxua-XRhCTZLwEx7X2ayg2-wViqWzNBMqMCyyY/edit

# This is already psuedo code:
# - identify the number to start
# - identify the surrounding numbers
# - find the max value of all the surrounding number
# - Set that max value to 0
# - This 0 value is now the new center
# - identify the surrounding numbers of new center and repeat
# - if all surrounding numbers are 0, stop the function

even = [[1,0,8,20],[7,4,9,21],[2,3,7,11],[4,6,8,14]]
odd = [[1,0,8],[7,4,9],[2,3,7]]

def squarematrix(lst):
    # Find the center number
    # center = 0
    nums = []

    center_row = 0
    center_index = 0
    if len(lst) % 2 ==1:
        center_row = len(lst)//2 #int division
        center_index = int(len(lst)/2)
        # center = lst[int(len(lst)/2)][int(len(lst)/2)]
    else:
        center_row = int(len(lst)/2-1)
        center_index = int(len(lst)/2-1)
        # center = lst[int(len(lst)/2-1)][int(len(lst)/2-1)]
    
    # Find surrounding numbers
    # FB: index out of range issue, use dictionary is better
    # FB: enum review
    num_1 = lst[center_row - 1][center_index-1]
    num_2 = lst[center_row - 1][center_index]
    num_3 = lst[center_row - 1][center_index+1]
    num_4 = lst[center_row][center_index + 1]
    num_5 = lst[center_row +1][center_index+1]
    num_6 = lst[center_row +1][center_index]
    num_7 = lst[center_row +1][center_index - 1]
    num_8 = lst[center_row][center_index - 1]
    
    nums.append(lst[center_row][center_index - 1])
    nums.append(lst[center_row][center_index + 1])
    nums.extend(lst[center_row - 1][center_index-1:center_index+2])
    nums.extend(lst[center_row + 1][center_index-1:center_index+2])
    
    max_index = nums.index(max(nums))
    
    return nums

squarematrix(even)
