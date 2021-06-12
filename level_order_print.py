#              1
#        /     \     \
#       2       3     10 
#     /   \       \
#    4     5       6
#         /  \     /
#        7    8   9
# Output for above tree should be. Print to the terminal
# 1
# 2 3 9
# 4 5 6
# 7 8 9


from collections import deque


class Node:
    def __init__(self, val, children=[]):
        self.val = val
        self.children = children
        
    def __repr__(self):
        return f"<Node value={self.val}>"

    
class Tree:
    def __init__(self, root=None):
        self.root = root
        
    def __str__(self):
        arr = self._level_order()
        return "\n".join([' '.join([str(node.val) for node in level]) for level in arr]) 

    def _level_order(self): # private method, you don't need to call it

        if not self.root:
            return None

        ans = []

        q = deque([(self.root,0)])

        while q:
            (node, level) = q.popleft()


            if len(ans) <= level:
                ans.append([node])

            else:
                ans[level].append(node)

            for child_node in node.children:
                q.append((child_node, level+1))

        return ans
                    
    
    def print_level_order(self):
        arr = self._level_order()

        for level in arr:
            print(' '.join([str(node.val) for node in level]))
            
    
    
root = Node(1)
r2 = Node(2)
r3 = Node(3)
r9 = Node(9)
r4 = Node(4)
r5 = Node(5)
r6 = Node(6)
r7 = Node(7)
r8 = Node(8)
r9 = Node(9)
r10 = Node(10)

tree = Tree(root)
root.children = [r2,r3,r10]
r2.children = [r4, r5]
r5.children = [r7, r8]
r3.children = [r6]
r6.children = [r9]
tree.print_level_order()
