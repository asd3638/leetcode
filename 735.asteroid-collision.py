#
# @lc app=leetcode id=735 lang=python3
#
# [735] Asteroid Collision
#
# https://leetcode.com/problems/asteroid-collision/description/
#
# algorithms
# Medium (45.03%)
# Likes:    8464
# Dislikes: 1192
# Total Accepted:    703.2K
# Total Submissions: 1.6M
# Testcase Example:  '[5,10,-5]'
#
# We are given an array asteroids of integers representing asteroids in a row.
# The indices of the asteriod in the array represent their relative position in
# space.
#
# For each asteroid, the absolute value represents its size, and the sign
# represents its direction (positive meaning right, negative meaning left).
# Each asteroid moves at the same speed.
#
# Find out the state of the asteroids after all collisions. If two asteroids
# meet, the smaller one will explode. If both are the same size, both will
# explode. Two asteroids moving in the same direction will never meet.
#
#
# Example 1:
#
#
# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never
# collide.
#
#
# Example 2:
#
#
# Input: asteroids = [8,-8]
# Output: []
# Explanation: The 8 and -8 collide exploding each other.
#
#
# Example 3:
#
#
# Input: asteroids = [10,2,-5]
# Output: [10]
# Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide
# resulting in 10.
#
#
#
# Constraints:
#
#
# 2 <= asteroids.length <= 10^4
# -1000 <= asteroids[i] <= 1000
# asteroids[i] != 0
#
#
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            # 현재 소행성이 음수(-)이고, 스택이 비어있지 않으며 마지막 소행성이 양수(→)라면 충돌 가능
            while stack and asteroid < 0 and stack[-1] > 0:
                # 충돌 결과 계산
                if abs(stack[-1]) < abs(asteroid):
                    stack.pop()  # 작은 소행성이 폭발하고 계속 충돌 진행
                    continue
                elif abs(stack[-1]) == abs(asteroid):
                    stack.pop()  # 같은 크기면 둘 다 폭발
                break  # stack[-1]이 더 크면 그대로 유지되므로 루프 종료
            else:
                stack.append(asteroid)  # 충돌이 없으면 스택에 추가

        return stack

# @lc code=end
