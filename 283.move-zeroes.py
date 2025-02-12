#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
# https://leetcode.com/problems/move-zeroes/description/
#
# algorithms
# Easy (62.47%)
# Likes:    17496
# Dislikes: 504
# Total Accepted:    3.7M
# Total Submissions: 6M
# Testcase Example:  '[0,1,0,3,12]'
#
# Given an integer array nums, move all 0's to the end of it while maintaining
# the relative order of the non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.
#
#
# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:
# Input: nums = [0]
# Output: [0]
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^4
# -2^31 <= nums[i] <= 2^31 - 1
#
#
#
# Follow up: Could you minimize the total number of operations done?
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[non_zero] = num
                non_zero += 1
        # print(non_zero)
        # print(nums)
        for i in range(non_zero, len(nums)):
            # print(i)
            nums[i] = 0
        # print(nums)


# @lc code=end
