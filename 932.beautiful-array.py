#
# @lc app=leetcode id=932 lang=python3
#
# [932] Beautiful Array
#
# https://leetcode.com/problems/beautiful-array/description/
#
# algorithms
# Medium (66.47%)
# Likes:    1095
# Dislikes: 1545
# Total Accepted:    48.6K
# Total Submissions: 72.9K
# Testcase Example:  '4'
#
# An array nums of length n is beautiful if:
# 
# 
# nums is a permutation of the integers in the range [1, n].
# For every 0 <= i < j < n, there is no index k with i < k < j where 2 *
# nums[k] == nums[i] + nums[j].
# 
# 
# Given the integer n, return any beautiful array nums of length n. There will
# be at least one valid answer for the given n.
# 
# 
# Example 1:
# Input: n = 4
# Output: [2,1,4,3]
# Example 2:
# Input: n = 5
# Output: [3,1,2,5,4]
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 1000
# 
# 
#

# @lc code=start
class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        
# @lc code=end

