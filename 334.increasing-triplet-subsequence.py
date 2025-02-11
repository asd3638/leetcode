#
# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
#
# https://leetcode.com/problems/increasing-triplet-subsequence/description/
#
# algorithms
# Medium (39.19%)
# Likes:    8386
# Dislikes: 612
# Total Accepted:    730.7K
# Total Submissions: 1.9M
# Testcase Example:  '[1,2,3,4,5]'
#
# Given an integer array nums, return true if there exists a triple of indices
# (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such
# indices exists, return false.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.
#
#
# Example 2:
#
#
# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.
#
#
# Example 3:
#
#
# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] ==
# 4 < nums[5] == 6.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 5 * 10^5
# -2^31 <= nums[i] <= 2^31 - 1
#
#
#
# Follow up: Could you implement a solution that runs in O(n) time complexity
# and O(1) space complexity?
#

# @lc code=start
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')   # 가장 작은 값
        second = float('inf')  # 두 번째로 작은 값

        for n in nums:
            if n <= first:
                first = n  # 첫 번째 최소값 업데이트
            elif n <= second:
                second = n  # 두 번째 최소값 업데이트
            else:
                # n > second를 만족하면 부분 수열 존재
                return True

        return False
# @lc code=end
