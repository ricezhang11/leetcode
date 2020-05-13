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
