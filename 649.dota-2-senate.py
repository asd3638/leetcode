#
# @lc app=leetcode id=649 lang=python3
#
# [649] Dota2 Senate
#
# https://leetcode.com/problems/dota2-senate/description/
#
# algorithms
# Medium (48.42%)
# Likes:    2550
# Dislikes: 1950
# Total Accepted:    208.3K
# Total Submissions: 430.1K
# Testcase Example:  '"RD"'
#
# In the world of Dota2, there are two parties: the Radiant and the Dire.
#
# The Dota2 senate consists of senators coming from two parties. Now the Senate
# wants to decide on a change in the Dota2 game. The voting for this change is
# a round-based procedure. In each round, each senator can exercise one of the
# two rights:
#
#
# Ban one senator's right: A senator can make another senator lose all his
# rights in this and all the following rounds.
# Announce the victory: If this senator found the senators who still have
# rights to vote are all from the same party, he can announce the victory and
# decide on the change in the game.
#
#
# Given a string senate representing each senator's party belonging. The
# character 'R' and 'D' represent the Radiant party and the Dire party. Then if
# there are n senators, the size of the given string will be n.
#
# The round-based procedure starts from the first senator to the last senator
# in the given order. This procedure will last until the end of voting. All the
# senators who have lost their rights will be skipped during the procedure.
#
# Suppose every senator is smart enough and will play the best strategy for his
# own party. Predict which party will finally announce the victory and change
# the Dota2 game. The output should be "Radiant" or "Dire".
#
#
# Example 1:
#
#
# Input: senate = "RD"
# Output: "Radiant"
# Explanation:
# The first senator comes from Radiant and he can just ban the next senator's
# right in round 1.
# And the second senator can't exercise any rights anymore since his right has
# been banned.
# And in round 2, the first senator can just announce the victory since he is
# the only guy in the senate who can vote.
#
#
# Example 2:
#
#
# Input: senate = "RDD"
# Output: "Dire"
# Explanation:
# The first senator comes from Radiant and he can just ban the next senator's
# right in round 1.
# And the second senator can't exercise any rights anymore since his right has
# been banned.
# And the third senator comes from Dire and he can ban the first senator's
# right in round 1.
# And in round 2, the third senator can just announce the victory since he is
# the only guy in the senate who can vote.
#
#
#
# Constraints:
#
#
# n == senate.length
# 1 <= n <= 10^4
# senate[i] is either 'R' or 'D'.
#
#
#

# @lc code=start
from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue_R = deque()  # Radiant (R)의 위치 저장
        queue_D = deque()  # Dire (D)의 위치 저장
        n = len(senate)

        # 1️⃣ 각 의원들의 초기 위치를 큐에 저장
        for i, s in enumerate(senate):
            if s == 'R':
                queue_R.append(i)
            else:
                queue_D.append(i)

        # 2️⃣ 투표 진행 (큐가 비어질 때까지)
        while queue_R and queue_D:
            r_idx = queue_R.popleft()
            d_idx = queue_D.popleft()

            # 3️⃣ 작은 인덱스가 먼저 투표 -> 상대방 제거
            if r_idx < d_idx:
                queue_R.append(r_idx + n)  # R이 D를 제거하고 다시 참여
            else:
                queue_D.append(d_idx + n)  # D가 R을 제거하고 다시 참여

        # 4️⃣ 승리 당 결정
        return "Radiant" if queue_R else "Dire"


# @lc code=end
