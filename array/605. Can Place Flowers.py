from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)

        for i in range(length):
            print(i)
            print(flowerbed)

            if flowerbed[i] == 0:
                # 왼쪽과 오른쪽 확인

                empty_left = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right = (i == length - 1) or (flowerbed[i + 1] == 0)

                if empty_left and empty_right:
                    # 꽃 심기
                    flowerbed[i] = 1
                    n -= 1

                    # 필요한 만큼 꽃을 다 심었으면 True 반환
                    if n == 0:
                        return True

        # 끝까지 확인 후 아직 꽃을 더 심어야 하면 False 반환
        return n <= 0


s = Solution()
print(s.canPlaceFlowers([1, 0, 0, 0, 1], 2))
