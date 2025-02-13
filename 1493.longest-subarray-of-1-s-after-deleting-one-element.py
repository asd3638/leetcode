#
# @lc app=leetcode id=1493 lang=python3
#
# [1493] Longest Subarray of 1's After Deleting One Element
#
# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/
#
# algorithms
# Medium (68.66%)
# Likes:    4139
# Dislikes: 88
# Total Accepted:    378.4K
# Total Submissions: 551K
# Testcase Example:  '[1,1,0,1]'
#
# Given a binary array nums, you should delete one element from it.
#
# Return the size of the longest non-empty subarray containing only 1's in the
# resulting array. Return 0 if there is no such subarray.
#
#
# Example 1:
#
#
# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3
# numbers with value of 1's.
#
#
# Example 2:
#
#
# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1]
# longest subarray with value of 1's is [1,1,1,1,1].
#
#
# Example 3:
#
#
# Input: nums = [1,1,1]
# Output: 2
# Explanation: You must delete one element.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# nums[i] is either 0 or 1.
#
#
#

# @lc code=start
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        max_len = 0
        zero_count = 0
        for right in range(len(nums)):
            # right 가 0을 만났을 때 (윈도우 축소)
            if nums[right] == 0:
                zero_count += 1
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len - 1


# @lc code=end
