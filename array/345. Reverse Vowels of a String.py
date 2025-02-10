# two pointer
class Solution:
    def reverseVowels(self, s: str) -> str:
        v = set('aeiouAEIOU')
        l_list = list(s)
        left_i = 0
        right_i = len(s) - 1
        while left_i < right_i:
            while left_i < right_i and l_list[left_i] not in v:
                left_i += 1
            while left_i < right_i and l_list[right_i] not in v:
                right_i -= 1
            l_list[left_i], l_list[right_i] = l_list[right_i], l_list[left_i]
            left_i += 1
            right_i -= 1
        return ''.join(l_list)
