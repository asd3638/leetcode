#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#
# https://leetcode.com/problems/4sum/description/
#
# algorithms
# Medium (37.52%)
# Likes:    11827
# Dislikes: 1443
# Total Accepted:    1.2M
# Total Submissions: 3.2M
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# Given an array nums of n integers, return an array of all the unique
# quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
#
#
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
#
#
# You may return the answer in any order.
#
#
# Example 1:
#
#
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
#
#
# Example 2:
#
#
# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 200
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
#
#
#

# @lc code=start
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()  # 1️⃣ 정렬
        n = len(nums)
        result = []

        for i in range(n - 3):  # 첫 번째 숫자 선택
            if i > 0 and nums[i] == nums[i - 1]:  # 중복 스킵
                continue

            for j in range(i + 1, n - 2):  # 두 번째 숫자 선택
                if j > i + 1 and nums[j] == nums[j - 1]:  # 중복 스킵
                    continue

                left, right = j + 1, n - 1  # 투 포인터 설정
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])

                        # 중복 제거
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1

                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return result


# @lc code=end
