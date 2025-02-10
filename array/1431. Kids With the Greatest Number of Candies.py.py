from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [ candy + extraCandies >= candy for candy in candies]
            
s = Solution()
print(s.kidsWithCandies([1, 2, 3], 3))      