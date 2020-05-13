# solve the problem using monotonous stack
# Monotonous stack is great for finding the values in the left and right side in an array
# that are larger than current value

import sys

# Definition for a binary tree node.


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        root = TreeNode(sys.maxsize)
        stack = [root]
        for num in nums:
            node = TreeNode(num)
            if node.val < stack[-1].val:
                stack.append(node)
            else:
                while node.val > stack[-1].val:
                    n = stack.pop()
                    if stack[-1].val < node.val:
                        stack[-1].right = n
                    else:
                        node.left = n
                stack.append(node)
        while stack:
            node = stack.pop()
            if stack:
                stack[-1].right = node
        return root.right
    
    
# solve by DFS

# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        return self.max_helper(nums)
        
    def max_helper(self, ls):
        if not ls:
            return None
        if len(ls) == 1:
            return TreeNode(ls[0])
        
        index = self.findMax(ls)
        node = TreeNode(ls[index])
        
        left = self.max_helper(ls[:index])
        right = self.max_helper(ls[index + 1:])
        
        node.left = left
        node.right = right
        
        return node
        
    def findMax(self, ls):
        m = (0, ls[0])
        
        for i, v in enumerate(ls):
            if v > m[1]:
                m = (i, v)
        return m[0]
