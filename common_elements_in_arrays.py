# Given three arrays sorted in non-decreasing order, print all common elements in these arrays.
# Input: 
# ar1[] = {1, 5, 10, 20, 40, 80} 
# ar2[] = {6, 7, 20, 80, 100} 
# ar3[] = {3, 4, 15, 20, 30, 70, 80, 120} 
# Output: 20, 80

# Input: 
# ar1[] = {1, 5, 5} 
# ar2[] = {3, 4, 5, 5, 10} 
# ar3[] = {5, 5, 10, 20} 
# Output: 5, 5

# https://www.geeksforgeeks.org/find-common-elements-three-sorted-arrays/

#==== Solution 1 - Brute force ====
def find_common(arr1, arr2, arr3):

    # Create a dictionary for each array with numbers as key and freq as value
    def create_dict(arr):
        arr_dict = {}
        for i in arr:
            arr_dict[i] = arr_dict.get(i,0) + 1
        return arr_dict

    arr2_dict = create_dict(arr2)
    arr3_dict = create_dict(arr3)

    ans = []

    # loop through arr1, if a number is in other dictionaries, reduce the freq by 1 and add the number to the answer
    for i in arr1:
        if i in arr2_dict and i in arr3_dict:
            ans.append(i)
            arr2_dict[i] -= 1
            arr3_dict[i] -= 1
            if arr2_dict[i] == 0:
                arr2_dict.pop(i)
            if arr3_dict[i] == 0:
                arr3_dict.pop(i)
    
    return ans

# arr1 = [1, 5, 10, 20, 40, 80]
# arr2 = [6, 7, 20, 80, 100]
# arr3 = [3, 4, 15, 20, 30, 70, 80, 120]

arr1 = [1,2]
arr2 = [3,4]
arr3 = [4,5]

print(find_common(arr1, arr2, arr3)) #[20, 80]