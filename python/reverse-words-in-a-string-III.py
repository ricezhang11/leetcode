class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return s
        words = s.split()
        res = ""
        for j in range(0, len(words)):
            i = len(words[j]) - 1
            while i >= 0:
                res = res + words[j][i]
                i -= 1
            if j == len(words) - 1:
                continue
            res = res + " "
                                 
        return res
