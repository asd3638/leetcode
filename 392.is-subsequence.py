#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#
# https://leetcode.com/problems/is-subsequence/description/
#
# algorithms
# Easy (48.18%)
# Likes:    10053
# Dislikes: 570
# Total Accepted:    1.9M
# Total Submissions: 3.9M
# Testcase Example:  '"abc"\n"ahbgdc"'
#
# Given two strings s and t, return true if s is a subsequence of t, or false
# otherwise.
#
# A subsequence of a string is a new string that is formed from the original
# string by deleting some (can be none) of the characters without disturbing
# the relative positions of the remaining characters. (i.e., "ace" is a
# subsequence of "abcde" while "aec" is not).
#
#
# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false
#
#
# Constraints:
#
#
# 0 <= s.length <= 100
# 0 <= t.length <= 10^4
# s and t consist only of lowercase English letters.
#
#
#
# Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k
# >= 10^9, and you want to check one by one to see if t has its subsequence. In
# this scenario, how would you change your code?
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        start_index = 0
        finish_index = len(s)
        for i, char in enumerate(t):
            if finish_index == 0:
                return True
            if char == s[start_index]:
                start_index += 1
                finish_index -= 1
        # print(start_index)
        if start_index == len(s):
            return True
        else:
            return False

# @lc code=end
