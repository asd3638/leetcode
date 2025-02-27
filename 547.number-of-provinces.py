#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#
# https://leetcode.com/problems/number-of-provinces/description/
#
# algorithms
# Medium (67.96%)
# Likes:    10219
# Dislikes: 384
# Total Accepted:    1.1M
# Total Submissions: 1.7M
# Testcase Example:  '[[1,1,0],[1,1,0],[0,0,1]]'
#
# There are n cities. Some of them are connected, while some are not. If city a
# is connected directly with city b, and city b is connected directly with city
# c, then city a is connected indirectly with city c.
#
# A province is a group of directly or indirectly connected cities and no other
# cities outside of the group.
#
# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the
# i^th city and the j^th city are directly connected, and isConnected[i][j] = 0
# otherwise.
#
# Return the total number of provinces.
#
#
# Example 1:
#
#
# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2
#
#
# Example 2:
#
#
# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
#
#
#
# Constraints:
#
#
# 1 <= n <= 200
# n == isConnected.length
# n == isConnected[i].length
# isConnected[i][j] is 1 or 0.
# isConnected[i][i] == 1
# isConnected[i][j] == isConnected[j][i]
#
#
#

# @lc code=start
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()  # 방문한 도시 저장
        provinces = 0

        def dfs(city):
            for neighbor in range(len(isConnected[city])):
                if isConnected[city][neighbor] == 1 and neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        for city in range(n):
            if city not in visited:
                provinces += 1  # 새로운 Province 발견
                visited.add(city)
                dfs(city)  # 해당 도시와 연결된 모든 도시 방문

        return provinces


# @lc code=end
