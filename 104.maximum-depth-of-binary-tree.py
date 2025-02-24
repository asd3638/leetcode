#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (76.70%)
# Likes:    13340
# Dislikes: 254
# Total Accepted:    3.8M
# Total Submissions: 4.9M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given the root of a binary tree, return its maximum depth.
#
# A binary tree's maximum depth is the number of nodes along the longest path
# from the root node down to the farthest leaf node.
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: 3
#
#
# Example 2:
#
#
# Input: root = [1,null,2]
# Output: 2
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 10^4].
# -100 <= Node.val <= 100
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 재귀
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#         l_depth = self.maxDepth(root.left)
#         r_depth = self.maxDepth(root.right)

#         return max(l_depth, r_depth) + 1


# 스택
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#         stack = [(root, 1)]
#         max_num = 0
#         while stack:
#             node, depth = stack.pop()
#             if node:
#                 max_num = max(max_num, depth)
#                 stack.append((node.right, depth + 1))
#                 stack.append((node.left, depth + 1))
#         return max_num

# 큐
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([(root, 1)])
        max_num = 0
        while q:
            node, depth = q.popleft()
            if node:
                max_num = max(max_num, depth)
                q.append((node.right, depth + 1))
                q.append((node.left, depth + 1))
        return max_num


# @lc code=end
