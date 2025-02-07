# brute force
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        len_list = len(nums)
        for i, num in enumerate(nums):
            # i - 0 1 2 3
            # num - 2 7 11 15
            for j in range(i + 1, len_list):
                # print(i, j)
                if num + nums[j] == target:
                    return [i, j]
            #print(i)
        return [] 
    
# hash map
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            vo = target - num
            if vo in num_map:
                return [num_map[vo], i]
            num_map[num] = i