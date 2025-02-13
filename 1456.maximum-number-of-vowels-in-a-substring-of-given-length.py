#
# @lc app=leetcode id=1456 lang=python3
#
# [1456] Maximum Number of Vowels in a Substring of Given Length
#
# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/
#
# algorithms
# Medium (59.69%)
# Likes:    3632
# Dislikes: 140
# Total Accepted:    467K
# Total Submissions: 782.3K
# Testcase Example:  '"abciiidef"\n3'
#
# Given a string s and an integer k, return the maximum number of vowel letters
# in any substring of s with length k.
#
# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
#
#
# Example 1:
#
#
# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.
#
#
# Example 2:
#
#
# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.
#
#
# Example 3:
#
#
# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^5
# s consists of lowercase English letters.
# 1 <= k <= s.length
#
#
#

# @lc code=start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        current_count = sum(1 for char in s[:k] if char in vowels)  # 초기 윈도우의 모음 개수
        max_count = current_count

        for i in range(k, len(s)):
            # 윈도우 오른쪽으로 이동
            if s[i] in vowels:
                current_count += 1  # 새로 추가된 문자가 모음이면 +1
            if s[i - k] in vowels:
                current_count -= 1  # 윈도우를 벗어난 문자가 모음이면 -1

            max_count = max(max_count, current_count)

            # 최적화: 최대 모음 개수(k)에 도달하면 조기 종료
            if max_count == k:
                return k

        return max_count


# @lc code=end
