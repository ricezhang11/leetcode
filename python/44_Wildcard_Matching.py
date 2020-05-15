# solved using dynamic programming

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        l_s = len(s)
        l_p = len(p)
        
        dp = [[False] * (l_p + 1) for i in range(l_s + 1)]
        dp[0][0] = True
        for j in range(1, l_p + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
    
        for i in range(1, l_s + 1):
            for j in range(1, l_p + 1):
                if s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    if p[j - 1] == '?':
                        dp[i][j] = dp[i - 1][j - 1]
                    elif p[j - 1] == '*':
                        dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        return dp[l_s][l_p]
