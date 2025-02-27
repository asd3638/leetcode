#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#
# https://leetcode.com/problems/maximum-average-subarray-i/description/
#
# algorithms
# Easy (44.54%)
# Likes:    3753
# Dislikes: 346
# Total Accepted:    713.7K
# Total Submissions: 1.6M
# Testcase Example:  '[1,12,-5,-6,50,3]\n4'
#
# You are given an integer array nums consisting of n elements, and an integer
# k.
#
# Find a contiguous subarray whose length is equal to k that has the maximum
# average value and return this value. Any answer with a calculation error less
# than 10^-5 will be accepted.
#
#
# Example 1:
#
#
# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
#
#
# Example 2:
#
#
# Input: nums = [5], k = 1
# Output: 5.00000
#
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= k <= n <= 10^5
# -10^4 <= nums[i] <= 10^4
#
#
#

# @lc code=start
from cmath import inf
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # 초기 윈도우 합 계산
        window_sum = sum(nums[:k])
        max_sum = window_sum

        # 윈도우를 오른쪽으로 슬라이드
        for i in range(k, len(nums)):
            # 윈도우에서 왼쪽 값 빼고, 오른쪽 값 더하기
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)

        return max_sum / k
# @lc code=end
