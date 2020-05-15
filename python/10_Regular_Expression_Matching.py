# solved using dynamic programming

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        l_s = len(s)
        l_p = len(p)

        dp = [[False] * (l_p + 1) for i in range(l_s + 1)]
        dp[0][0] = True
        for j in range(1, l_p + 1):
             if p[j - 1] == '*' and j >= 2 and dp[0][j - 2] == True:
                dp[0][j] = True

        for i in range(1, l_s + 1):
            for j in range(1, l_p + 1):
                if s[i - 1] == p[j - 1]: # if s at i - 1 position and p at j - 1 position are equal
                    dp[i][j] = dp[i - 1][j - 1]
                else: # when s at i - 1 position and p at j - 1 position are not equal
                    if p[j - 1] == '.':
                        dp[i][j] = dp[i - 1][j - 1]
                    elif p[j - 1] == '*':
                        if j >= 2 and dp[i][j - 2] == True:
                            dp[i][j] = True
                        elif dp[i - 1][j] == True and (s[i - 1] == p[j - 2] or p[j - 2] == '.'):
                            dp[i][j] = True

        return dp[l_s][l_p]   
