#
# @lc app=leetcode id=1372 lang=python3
#
# [1372] Longest ZigZag Path in a Binary Tree
#
# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/description/
#
# algorithms
# Medium (66.27%)
# Likes:    3576
# Dislikes: 78
# Total Accepted:    220.4K
# Total Submissions: 332.5K
# Testcase Example:  '[1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]'
#
# You are given the root of a binary tree.
#
# A ZigZag path for a binary tree is defined as follow:
#
#
# Choose any node in the binary tree and a direction (right or left).
# If the current direction is right, move to the right child of the current
# node; otherwise, move to the left child.
# Change the direction from right to left or from left to right.
# Repeat the second and third steps until you can't move in the tree.
#
#
# Zigzag length is defined as the number of nodes visited - 1. (A single node
# has a length of 0).
#
# Return the longest ZigZag path contained in that tree.
#
#
# Example 1:
#
#
# Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
# Output: 3
# Explanation: Longest ZigZag path in blue nodes (right -> left -> right).
#
#
# Example 2:
#
#
# Input: root = [1,1,1,null,1,null,null,1,1,null,1]
# Output: 4
# Explanation: Longest ZigZag path in blue nodes (left -> right -> left ->
# right).
#
#
# Example 3:
#
#
# Input: root = [1]
# Output: 0
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 5 * 10^4].
# 1 <= Node.val <= 100
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
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_value = 0  # 최대 ZigZag 길이 저장

        def dfs(node, direction, length):
            if not node:
                return

            # 최대 길이 갱신
            self.max_value = max(self.max_value, length)

            # 왼쪽 이동 (현재 방향이 오른쪽일 때)
            if direction == 'r':
                dfs(node.left, 'l', length + 1)
                dfs(node.right, 'r', 1)  # 새로운 시작점 설정
            # 오른쪽 이동 (현재 방향이 왼쪽일 때)
            else:
                dfs(node.right, 'r', length + 1)
                dfs(node.left, 'l', 1)  # 새로운 시작점 설정

        # 루트의 왼쪽, 오른쪽 각각 탐색 시작
        dfs(root.left, 'l', 1)
        dfs(root.right, 'r', 1)

        return self.max_value


# @lc code=end
