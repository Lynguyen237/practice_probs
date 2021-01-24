# https://www.interviewcake.com/question/java/find-unique-int-among-duplicates
# Your company delivers breakfast via autonomous quadcopter drones. And something mysterious has happened.

# Each breakfast delivery is assigned a unique ID, a positive integer. When one of the company's 100 drones takes off with a delivery, the delivery's ID is added to a list, delivery_id_confirmations. When the drone comes back and lands, the ID is again added to the same list.

# After breakfast this morning there were only 99 drones on the tarmac. One of the drones never made it back from a delivery. We suspect a secret agent from Amazon placed an order and stole one of our patented drones. To track them down, we need to find their delivery ID.

# Given the list of IDs, which contains many duplicate integers and one unique integer, find the unique integer.

# Example [1,3,2,2,1,4,3] # Answer: 4

def find_unique_delivery_id(delivery_ids):
    # Loop through the list of IDs
    # Add each item to a new set
        #  if the item being iterated is already in the set, pop it.
    # Return the remain (unique) ID in the set
    unique_set = set()

    for i in delivery_ids:
        if i not in unique_set:
            unique_set.add(i)
        else:
            unique_set.remove(i)
    
    for i in unique_set:
        return i

print(find_unique_delivery_id([1,3,2,2,1,4,3]))