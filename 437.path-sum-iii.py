#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#
# https://leetcode.com/problems/path-sum-iii/description/
#
# algorithms
# Medium (46.04%)
# Likes:    11348
# Dislikes: 544
# Total Accepted:    661.2K
# Total Submissions: 1.4M
# Testcase Example:  '[10,5,-3,3,2,null,11,3,-2,null,1]\n8'
#
# Given the root of a binary tree and an integer targetSum, return the number
# of paths where the sum of the values along the path equals targetSum.
#
# The path does not need to start or end at the root or a leaf, but it must go
# downwards (i.e., traveling only from parent nodes to child nodes).
#
#
# Example 1:
#
#
# Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# Output: 3
# Explanation: The paths that sum to 8 are shown.
#
#
# Example 2:
#
#
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: 3
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 1000].
# -10^9 <= Node.val <= 10^9
# -1000 <= targetSum <= 1000
#
#
#

# @lc code=start
# Definition for a binary tree node.

from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

#         def countSum(node, currentSum):
#             count = 0
#             if not node:
#                 return 0
#             # print(node.val)
#             currentSum += node.val
#             if currentSum == targetSum:
#                 count += 1
#             count += countSum(node.left, currentSum)
#             count += countSum(node.right, currentSum)
#             return count
#         if not root:
#             return 0
#         return countSum(root, 0) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)


# dfs + prefixsum
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def dfs(node, currentSum, prefixSum):
            if not node:
                return 0

            currentSum += node.val  # 누적 합 갱신
            # `currentSum - targetSum`이 존재하는 개수 더하기
            count = prefixSum[currentSum - targetSum]

            prefixSum[currentSum] += 1  # 현재 누적 합 개수 증가

            # 왼쪽과 오른쪽으로 탐색하면서 결과 합산
            count += dfs(node.left, currentSum, prefixSum)
            count += dfs(node.right, currentSum, prefixSum)

            prefixSum[currentSum] -= 1  # 백트래킹 (현재 노드에서 나올 때 개수 감소)

            return count

        prefixSum = defaultdict(int)
        prefixSum[0] = 1  # 기본적으로 0을 하나 포함 (루트에서 시작하는 경로 고려)
        return dfs(root, 0, prefixSum)


# @lc code=end
