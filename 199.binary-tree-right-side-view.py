#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#
# https://leetcode.com/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (65.47%)
# Likes:    12521
# Dislikes: 1053
# Total Accepted:    1.7M
# Total Submissions: 2.6M
# Testcase Example:  '[1,2,3,null,5,null,4]'
#
# Given the root of a binary tree, imagine yourself standing on the right side
# of it, return the values of the nodes you can see ordered from top to
# bottom.
#
#
# Example 1:
#
#
# Input: root = [1,2,3,null,5,null,4]
#
# Output: [1,3,4]
#
# Explanation:
#
#
#
#
# Example 2:
#
#
# Input: root = [1,2,3,4,null,null,null,5]
#
# Output: [1,3,4,5]
#
# Explanation:
#
#
#
#
# Example 3:
#
#
# Input: root = [1,null,3]
#
# Output: [1,3]
#
#
# Example 4:
#
#
# Input: root = []
#
# Output: []
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
#
#
#

# @lc code=start
# Definition for a binary tree node.


from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            node_depth = len(queue)
            right_most = None
            for i in range(node_depth):
                node = queue.popleft()
                right_most = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(node.val)
        return result

# @lc code=end
