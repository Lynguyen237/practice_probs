# https://leetcode.com/problems/symmetric-tree/
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
# Input: root = [1,2,2,3,4,4,3]
# Output: true
# Input: root = [1,2,2,null,3,null,3]
# Output: false


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return (f'value: {self.val}, left: {self.left.val}, right: {self.right.val}')

# Instantiate a tree for testing
n6 = TreeNode(3, None, None)
n5 = TreeNode(4, None, None)
n4 = TreeNode(4, None, None)
n3 = TreeNode(3, None, None)
n2 = TreeNode(2, n5, n6)
n1 = TreeNode(2, n3, n4)
root = TreeNode(1, n1, n2)


#==== Solution using recursion (O(n) time and space complexity)====
def isSymmetric(root: TreeNode) -> bool:
    if root is None:
        return True
    
    return isMirror(root.left, root.right)

def isMirror(n1, n2):
    if n1 is None and n2 is None:
        return True
    if n1 is None or n2 is None or n1.val != n2.val:
        return False
    else:
        return isMirror(n1.left, n2.right) and\
               isMirror(n1.right, n2.left)


#==== Solution2 (no recursion) ====
def isSymmetric2(root: TreeNode) -> bool:
    if root is None:
        return True
    
    stack = []
    stack.append(root.left)
    stack.append(root.right)

    while stack:
        left, right = stack.pop(), stack.pop()
        
        if left is None and right is None:
            continue

        if left is None or right is None or left.val != right.val:
            return False
        
        stack.append(left.left)
        stack.append(right.right)

        stack.append(left.right)
        stack.append(right.left)
    
    return True

print(isSymmetric2(root))
# Reference https://github.com/kamyu104/LeetCode-Solutions/blob/master/Python/symmetric-tree.py