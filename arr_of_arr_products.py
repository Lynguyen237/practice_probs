# Given an array of integers arr, you are asked to calculate for each index i the product of all integers 
# except the integer at that index (i.e. except arr[i]). Implement a function arrayOfArrayProducts 
# that takes an array of integers and returns an array of the products.
# Solve without using division and analyze your solution time and space complexities.

# Examples:
# input:  arr = [8, 10, 2]
# output: [20, 16, 80] # by calculating: [10*2, 8*2, 8*10]

# input:  arr = [2, 7, 3, 4]
# output: [84, 24, 56, 42] 

#==== Solution (Optimized V2 (O(n) time & space complexity) ====
def array_of_array_products(arr):

    if len(arr) <= 1: #return an empty array if the list length is 0 or 1
        return []

    product_arr = []
    product = 1

    for i in range(len(arr)):
        product_arr.append(product) # or product_arr[i] =
        product *= arr[i]
    
    product = 1
    for i in reversed(range(len(arr))):
        product_arr[i] *= product
        product *= arr[i]
        
    return product_arr

print(array_of_array_products([8, 10, 2]))
# print(array_of_array_products([2, 7, 3, 4]))
# print(array_of_array_products([9]))
# print(array_of_array_products([]))
# print(array_of_array_products([0,1,1]))


#==== Solution (Optimized V1 (O(n) time complexity) ====
def array_of_array_products1(arr):
  
  if len(arr) <= 1:
    return []
  
  products = []
  
  left_products = [1]
  right_products = []
  left_product = 1
  right_product = 1
  
  for i in arr[:-1]: # calculate the array of left products
    left_product = left_product * i
    left_products.append(left_product)
  for i in reversed(arr[1:]): # calculate the array of right products
    right_product = right_product * i
    right_products.insert(0,right_product)
  
  right_products.append(1)
  
  for i in range(len(left_products)): # multiply the left products and the right products
    products.append(left_products[i]*right_products[i])
    
  return products

#==== Initial solution (O(n^2) time complexity, O(n) space complexity) ====
def array_of_array_products0(arr):
    if len(arr) <= 1:
        return []
    
    products = []

    for i in range(len(arr)):
        product = 1
        for j in arr[:i]:
            product = product * j
        for k in arr[i+1:]:
            product = product * k
            products.append(product)
    
    return products
    

