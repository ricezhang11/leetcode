# 78. Longest Common Prefix
# 中文English
# Given k strings, find the longest common prefix (LCP).

# Example
# Example 1:
# 	Input:  "ABCD", "ABEF", "ACEF"
# 	Output:  "A"
	

# Example 2:
# 	Input: "ABCDEFG", "ABCEFG" and "ABCEFA"
# 	Output:  "ABC"
class Solution:
    """
    @param strs: A list of strings
    @return: The longest common prefix
    """
    def longestCommonPrefix(self, strs):
        # write your code here
                # write your code here
        if not strs:
            return ''
        res = ''
        b = True
        min_leng = sys.maxsize
        for st in strs:
            if len(st) <= min_leng:
                min_leng = len(st)
        for i in range(min_leng):
            for j in range(len(strs)):
                if strs[0][0:i+1] != strs[j][0:i+1]:
                    b = False
            if b == True:
                res = strs[0][0:i+1]
            else:
                return res
        return res

#find the shortest element. Then start from 0, get all prefix, compare witht the rest of the elements in the string list. If other elements share the same prefix, then continue with the next prefix. If not, return the last prefix the elements all share. 
