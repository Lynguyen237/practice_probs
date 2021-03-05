# A palindrome is a sequence that reads the same backwards as forwards
# example: "n u r s e s r u n" "madam"
# Given an array of numbers representing different flower types, return a bouquet (an array) that is a palindrome. Assume that the given array will always return a palindrome.

# [1, 1, 2, 2, 3] => [1,2,3,2,1] or  [2, 1, 3, 1, 2]
# [1, 1, 2] => [1, 2, 1] 
# [2, 3, 2, 3] => [2, 3, 3, 2]
# [2, 2, 2, 3, 2] => [2, 2, 3, 2, 2]

#==== LEVEL 1, create a palindrome from an array of different flower types

def arrange_bouquet(flower_bunch):
    
    if len(flower_bunch) == 0:
        return flower_bunch
    
    if len(set(flower_bunch)) == 1:
        return flower_bunch

    flower_dict = {}
    palindrome_arr = []
    
    # Loop through the array to create dictionary with flower type and the quantity
    for flower in flower_bunch:
         if flower not in flower_dict:
            flower_dict[flower] = 1
         else:
            flower_dict[flower] += 1
    
    # Create the palindrome array by looping through the flower dictionary
    for flower in flower_dict:
       
        if flower_dict[flower] % 2 == 0:
            
            added_quantity = int(flower_dict[flower] / 2)
            
            for i in range(added_quantity):
                palindrome_arr.insert(0, flower)
                palindrome_arr.append(flower)
            
        else:
            mid_idx = int(len(palindrome_arr)/2)
            for i in range(flower_dict[flower]):
                palindrome_arr.insert(mid_idx, flower)
                mid_idx +=1
    
                   
    return palindrome_arr


print(arrange_bouquet([1, 1, 2, 2, 3]))   
print(arrange_bouquet([1, 1, 2, 2, 3, 3, 3]))   
print(arrange_bouquet([])) 
print(arrange_bouquet([1, 1, 2, 2])) 


#==== LEVEL 2
# A flower can have multiple colors & size
# [Rose1, Rose2, Lily, sunflower, sunflower]
# Rose1 => small, red
# Rose2 => small, pink
# Lily => big, pink
# Sunflower => big, yellow

# Find a way to represent flowers & their colors + sizes
# Then create a palindrome by color for [rose1, rose2, lily, sunflower, sunflower]
# = > [rose2, sunflower, rose1, sunflower, lily] ([pink, yellow, red, yellow, pink])

class Flower:
        
    def __init__(self, name, size, color):
        self.name = name
        self.size = size
        self.color = color
    
    def __repr__(self):
        rep = self.name + '_' + self.size + '_' + self.color
        return rep
    
rose1 = Flower('rose','small', 'red')
rose2 = Flower('rose','small', 'pink')
lily = Flower('lily','big','pink')
sunflower = Flower('sunflower', 'big', 'yellow')

flower_bunch = [rose1, rose2, lily, sunflower, sunflower]


def arrange_bouquet2(flower_bunch):
    
    if len(flower_bunch) == 0:
        return flower_bunch
    
    flower_dict = {}
    palindrome_arr = []
    
    # Loop through the given array to create a flower dictionary with keys = colors
    # values = nested dictionary with 2 keys:
        # 'count' = number of instances of that color
        # 'flower_lst' = array of flowers with that color
    for flower in flower_bunch:
        if flower.color not in flower_dict:
            flower_dict[flower.color] = {} # create the key and an empty nested dictionary as value
            flower_dict[flower.color]['count'] = 1
            flower_dict[flower.color]['flower_lst'] = [flower]
        else:
            flower_dict[flower.color]['count'] += 1
            flower_dict[flower.color]['flower_lst'].append(flower)

            
    # Create the palindrome array by looping through the flower dictionary
    for color in flower_dict:
        
        # If the color count is even, add flowers to 2 ends of the palindrome array
        if flower_dict[color]['count'] % 2 == 0:
            
            # Find the middle index of the flower list 
            mid_idx = int(len(flower_dict[color]['flower_lst']) / 2)
           
            for flower in flower_dict[color]['flower_lst'][:mid_idx]:
                palindrome_arr.insert(0, flower) # Add one flower to the beginning
                
            for flower in flower_dict[color]['flower_lst'][mid_idx:]:
                palindrome_arr.append(flower) # Add one flower to the end
                
                
        # If the color count is odd, add the flowers to the middle of the array
        else:
            mid_idx = int(len(palindrome_arr)/2)
            for flower in flower_dict[color]['flower_lst']:
                palindrome_arr.insert(mid_idx, flower)
                mid_idx +=1
            
                   
    return palindrome_arr

print(arrange_bouquet2(flower_bunch)) 
# [rose2, sunflower, rose1, sunflower, lily] or [sunflower, rose2, rose1, lily, sunflower]


#====Level 2B
# Create a palindrome in a specific order [pink, yellow, red, yellow, pink]
# For this to work, we have to assume that the number or pink and yellow flowers are always even 
# and red will always be odd.

def arrange_bouquet2b(flower_bunch):
    
    if len(flower_bunch) == 0:
        return flower_bunch
    
    flower_dict = {}
    palindrome_arr = []
    
    # Loop through the given array to create a flower dictionary with keys = colors
    # values = nested dictionary with 2 keys:
        # 'count' = number of instances of that color
        # 'flower_lst' = array of flowers with that color
    for flower in flower_bunch:
        if flower.color not in flower_dict:
            flower_dict[flower.color] = {} # create the key and an empty nested dictionary as value
            flower_dict[flower.color]['count'] = 1
            flower_dict[flower.color]['flower_lst'] = [flower]
        else:
            flower_dict[flower.color]['count'] += 1
            flower_dict[flower.color]['flower_lst'].append(flower)

    color_order = ['pink', 'yellow', 'red', 'yellow', 'pink']
    # Create the palindrome array by looping through the flower dictionary
    for color in color_order[int(len(color_order)/2):]:
        
        # If the color count is even, add flowers to 2 ends of the palindrome array
        if flower_dict[color]['count'] % 2 == 0:
            
            # Find the middle index of the flower list 
            mid_idx = int(len(flower_dict[color]['flower_lst']) / 2)
           
            for flower in flower_dict[color]['flower_lst'][:mid_idx]:
                palindrome_arr.insert(0, flower) # Add one flower to the beginning
                
            for flower in flower_dict[color]['flower_lst'][mid_idx:]:
                palindrome_arr.append(flower) # Add one flower to the end
                
                
        # If the color count is odd, add the flowers to the middle of the array
        else:
            mid_idx = int(len(palindrome_arr)/2)
            for flower in flower_dict[color]['flower_lst']:
                palindrome_arr.insert(mid_idx, flower)
                mid_idx +=1
            
                   
    return palindrome_arr

print(arrange_bouquet2b(flower_bunch)) 
# [sunflower, rose2, rose1, lily, sunflower]
# or [sunflower, lily, rose1, roses2, sunflower]


