#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#
# https://leetcode.com/problems/decode-string/description/
#
# algorithms
# Medium (60.55%)
# Likes:    13165
# Dislikes: 644
# Total Accepted:    955.9K
# Total Submissions: 1.6M
# Testcase Example:  '"3[a]2[bc]"'
#
# Given an encoded string, return its decoded string.
#
# The encoding rule is: k[encoded_string], where the encoded_string inside the
# square brackets is being repeated exactly k times. Note that k is guaranteed
# to be a positive integer.
#
# You may assume that the input string is always valid; there are no extra
# white spaces, square brackets are well-formed, etc. Furthermore, you may
# assume that the original data does not contain any digits and that digits are
# only for those repeat numbers, k. For example, there will not be input like
# 3a or 2[4].
#
# The test cases are generated so that the length of the output will never
# exceed 10^5.
#
#
# Example 1:
#
#
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
#
#
# Example 2:
#
#
# Input: s = "3[a2[c]]"
# Output: "accaccacc"
#
#
# Example 3:
#
#
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 30
# s consists of lowercase English letters, digits, and square brackets
# '[]'.
# s is guaranteed to be a valid input.
# All the integers in s are in the range [1, 300].
#
#
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []  # 스택을 사용하여 문자 저장
        num = 0     # 현재 반복할 숫자 저장
        current_str = ""  # 현재 문자열 저장

        for char in s:
            if char.isdigit():
                # 숫자인 경우, num을 업데이트 (2자리 이상 숫자도 처리 가능)
                num = num * 10 + int(char)
            elif char == '[':
                # '['가 나오면 현재까지의 문자열과 숫자를 스택에 저장
                stack.append((current_str, num))
                # 초기화
                current_str = ""
                num = 0
            elif char == ']':
                # ']'가 나오면, 스택에서 이전 문자열과 반복 횟수를 가져와 복원
                prev_str, repeat_num = stack.pop()
                current_str = prev_str + current_str * repeat_num
            else:
                # 일반 문자이면 현재 문자열에 추가
                current_str += char

        return current_str


# @lc code=end
