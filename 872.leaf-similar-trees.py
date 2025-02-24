#
# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
#
# https://leetcode.com/problems/leaf-similar-trees/description/
#
# algorithms
# Easy (70.06%)
# Likes:    4219
# Dislikes: 121
# Total Accepted:    571.9K
# Total Submissions: 816.3K
# Testcase Example:  '[3,5,1,6,2,9,8,null,null,7,4]\n' +
# '[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]'
#
# Consider all the leaves of a binary tree, from left to right order, the
# values of those leaves form a leaf value sequence.
#
#
#
# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9,
# 8).
#
# Two binary trees are considered leaf-similar if their leaf value sequence is
# the same.
#
# Return true if and only if the two given trees with head nodes root1 and
# root2 are leaf-similar.
#
#
# Example 1:
#
#
# Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 =
# [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
# Output: true
#
#
# Example 2:
#
#
# Input: root1 = [1,2,3], root2 = [1,3,2]
# Output: false
#
#
#
# Constraints:
#
#
# The number of nodes in each tree will be in the range [1, 200].
# Both of the given trees will have values in the range [0, 200].
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
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        s1 = [root1]
        s1_result = []
        s2 = [root2]
        s2_result = []
        while s1:
            n1 = s1.pop()
            if n1.left:
                s1.append(n1.left)
            if n1.right:
                s1.append(n1.right)
            if not n1.left and not n1.right:
                s1_result.append(n1.val)
        while s2:
            n2 = s2.pop()
            if n2.left:
                s2.append(n2.left)
            if n2.right:
                s2.append(n2.right)
            if not n2.left and not n2.right:
                s2_result.append(n2.val)
        print(s1_result)
        print(s2_result)
        if s1_result != s2_result:
            return False
        return True


# @lc code=end
