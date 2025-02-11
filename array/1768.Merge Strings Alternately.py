from collections import deque


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        q1 = deque(word1)
        q2 = deque(word2)
        result = []
        while q1 or q2:
            if q1:
                result.append(q1.popleft())
            if q2:
                result.append(q2.popleft())
        print(result)
        
solution = Solution()
solution.mergeAlternately("ab", "cd")