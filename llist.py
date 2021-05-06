class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_llist(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

    def append(self, data):
        new_node = ListNode(data)
        curr = self.head
        
        # If the llist is empty, the new node is the head
        if not curr:
            self.head = new_node
            return
        
        # While the next node after the current node is not Null
        # Assign the current node ad the next node
        while curr.next:
            curr = curr.next
        
        # The last node in the llist won't have any next node so we assign the new node
        curr.next = new_node


    def prepend(self, data):
        new_node = ListNode(data)

        # Don't need to check if head exist because the next node to the new node can point to None
        new_node.next = self.head 
        self.head = new_node


    def insert_a_node(self, prev_node, data):
        new_node = ListNode(data)

        if not prev_node:
            return ("Previous node does not exist")
        
        if prev_node:
            new_node.next = prev_node.next # Point the new node to the next node of the previous node
            prev_node.next = new_node # Point the previous node to the new node


    def rotate_llist(self):
        pass

# ===========================================
# https://www.youtube.com/watch?v=FSsriWQ0qYE
# First example
llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.prepend("Z")
llist.insert_a_node(llist.head.next, "insertion")

llist.print_llist()

# Second example
llist2 = LinkedList()
llist2.prepend("Amazing Start")
llist2.print_llist()
