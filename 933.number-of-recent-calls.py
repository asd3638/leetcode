#
# @lc app=leetcode id=933 lang=python3
#
# [933] Number of Recent Calls
#
# https://leetcode.com/problems/number-of-recent-calls/description/
#
# algorithms
# Easy (76.96%)
# Likes:    655
# Dislikes: 1015
# Total Accepted:    364.5K
# Total Submissions: 473.2K
# Testcase Example:  '["RecentCounter","ping","ping","ping","ping"]\n[[],[1],[100],[3001],[3002]]'
#
# You have a RecentCounter class which counts the number of recent requests
# within a certain time frame.
#
# Implement the RecentCounter class:
#
#
# RecentCounter() Initializes the counter with zero recent requests.
# int ping(int t) Adds a new request at time t, where t represents some time in
# milliseconds, and returns the number of requests that has happened in the
# past 3000 milliseconds (including the new request). Specifically, return the
# number of requests that have happened in the inclusive range [t - 3000, t].
#
#
# It is guaranteed that every call to ping uses a strictly larger value of t
# than the previous call.
#
#
# Example 1:
#
#
# Input
# ["RecentCounter", "ping", "ping", "ping", "ping"]
# [[], [1], [100], [3001], [3002]]
# Output
# [null, 1, 2, 3, 3]
#
# Explanation
# RecentCounter recentCounter = new RecentCounter();
# recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
# recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100],
# return 2
# recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001],
# return 3
# recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is
# [2,3002], return 3
#
#
#
# Constraints:
#
#
# 1 <= t <= 10^9
# Each test case will call ping with strictly increasing values of t.
# At most 10^4 calls will be made to ping.
#
#
#

# @lc code=start
from collections import deque


class RecentCounter:
    def __init__(self):
        self.requests = deque()  # 요청을 저장할 큐

    def ping(self, t: int) -> int:
        self.requests.append(t)  # 새로운 요청 추가

        # 3000ms(3초)보다 오래된 요청을 제거
        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()

        return len(self.requests)  # 현재 남아 있는 요청 수 반환
        # Your RecentCounter object will be instantiated and called as such:
        # obj = RecentCounter()
        # param_1 = obj.ping(t)
        # @lc code=end
