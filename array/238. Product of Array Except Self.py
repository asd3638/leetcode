import math
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        s = math.prod(nums)
        r = [int(s) if i == 0 else int(s / i) for i in nums]
        return r


s = Solution()
print(s.productExceptSelf([1, 2, 0, 4, 5]))
