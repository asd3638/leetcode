#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
#
# algorithms
# Medium (65.55%)
# Likes:    17301
# Dislikes: 450
# Total Accepted:    2M
# Total Submissions: 3.1M
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n1'
#
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes
# in the tree.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes p and q as the lowest node in T that has both p
# and q as descendants (where we allow a node to be a descendant of
# itself).”
#
#
# Example 1:
#
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
#
#
# Example 2:
#
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant
# of itself according to the LCA definition.
#
#
# Example 3:
#
#
# Input: root = [1,2], p = 1, q = 2
# Output: 1
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [2, 10^5].
# -10^9 <= Node.val <= 10^9
# All Node.val are unique.
# p != q
# p and q will exist in the tree.
#
#
#

# @lc code=start
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p_anc = []
        self.q_anc = []

        def dfs(node, path):
            if not node:
                return

            # 현재 경로를 새로운 리스트로 전달 (복사)
            new_path = path + [node.val]
            print(new_path)

            if node == p:
                self.p_anc = new_path  # p의 경로 저장
            if node == q:
                self.q_anc = new_path  # q의 경로 저장

            dfs(node.left, new_path)
            dfs(node.right, new_path)

        dfs(root, [])

        print("p의 조상 노드들:", [node.val for node in self.p_anc])
        print("q의 조상 노드들:", [node.val for node in self.q_anc])

        # 뒤에서부터 공통된 조상을 찾음
        for i in self.p_anc[::-1]:  # 뒤에서부터 순회
            if i in self.q_anc:
                return i  # 최저 공통 조상 반환


# @lc code=end
