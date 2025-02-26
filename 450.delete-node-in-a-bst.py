#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
#
# https://leetcode.com/problems/delete-node-in-a-bst/description/
#
# algorithms
# Medium (52.50%)
# Likes:    9584
# Dislikes: 326
# Total Accepted:    643.6K
# Total Submissions: 1.2M
# Testcase Example:  '[5,3,6,2,4,null,7]\n3'
#
# Given a root node reference of a BST and a key, delete the node with the
# given key in the BST. Return the root node reference (possibly updated) of
# the BST.
#
# Basically, the deletion can be divided into two stages:
#
#
# Search for a node to remove.
# If the node is found, delete the node.
#
#
#
# Example 1:
#
#
# Input: root = [5,3,6,2,4,null,7], key = 3
# Output: [5,4,6,2,null,null,7]
# Explanation: Given key to delete is 3. So we find the node with value 3 and
# delete it.
# One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
# Please notice that another valid answer is [5,2,6,null,4,null,7] and it's
# also accepted.
#
#
#
# Example 2:
#
#
# Input: root = [5,3,6,2,4,null,7], key = 0
# Output: [5,3,6,2,4,null,7]
# Explanation: The tree does not contain a node with value = 0.
#
#
# Example 3:
#
#
# Input: root = [], key = 0
# Output: []
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 10^4].
# -10^5 <= Node.val <= 10^5
# Each node has a unique value.
# root is a valid binary search tree.
# -10^5 <= key <= 10^5
#
#
#
# Follow up: Could you solve it with time complexity O(height of tree)?
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


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None  # 삭제할 노드가 없음

        # 1️⃣ 삭제할 값 찾기
        if key < root.val:
            root.left = self.deleteNode(root.left, key)  # ✅ 재귀 결과를 반영해야 함
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)  # ✅ 재귀 결과 반영
        else:
            # 2️⃣ 리프 노드 (자식 없음)
            if not root.left and not root.right:
                return None

            # 3️⃣ 자식이 하나만 있는 경우
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # 4️⃣ 자식이 둘 있는 경우: "후계자(successor)" 찾기
            successor = self.findMin(root.right)  # 오른쪽 서브트리에서 가장 작은 값
            root.val = successor.val  # 값 교체
            root.right = self.deleteNode(root.right, successor.val)  # ✅ 후계자 삭제

        return root

    def findMin(self, node: TreeNode) -> TreeNode:
        while node.left:
            node = node.left
        return node


# @lc code=end
