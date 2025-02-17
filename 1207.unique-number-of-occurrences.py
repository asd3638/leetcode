#
# @lc app=leetcode id=1207 lang=python3
#
# [1207] Unique Number of Occurrences
#
# https://leetcode.com/problems/unique-number-of-occurrences/description/
#
# algorithms
# Easy (77.95%)
# Likes:    5254
# Dislikes: 145
# Total Accepted:    785.1K
# Total Submissions: 1M
# Testcase Example:  '[1,2,2,1,1,3]'
#
# Given an array of integers arr, return true if the number of occurrences of
# each value in the array is unique or false otherwise.
#
#
# Example 1:
#
#
# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two
# values have the same number of occurrences.
#
# Example 2:
#
#
# Input: arr = [1,2]
# Output: false
#
#
# Example 3:
#
#
# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true
#
#
#
# Constraints:
#
#
# 1 <= arr.length <= 1000
# -1000 <= arr[i] <= 1000
#
#
#

# @lc code=start
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict = {}
        for i in arr:
            if dict.get(i, -1001) == -1001:
                dict[i] = 1
            else:
                dict[i] += 1
        if len(dict.values()) == len(set(dict.values())):
            return True
        else:
            return False

# @lc code=end
