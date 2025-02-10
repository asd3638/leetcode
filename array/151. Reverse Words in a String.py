class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        word = ''
        for i in s:
            if i != ' ':
                word += i
            elif word:
                stack.append(word)
                word =
        if word:
            stack.append(word)
        print(stack)
        return ''.join(stack[::-1])


s = Solution()
print(s.reverseWords("aa  bb"))
