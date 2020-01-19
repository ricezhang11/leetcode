class Solution:
    """
    @param str: a string
    @return: return a string
    """
    def reverseWords(self, str):
        # write your code here
        # if not str:
        #     return str
        
        i = 0
        pre = 0
        res = ""
        while i < len(str):
            if str[i] == " ":
                res = res + str[pre:i][::-1] + " "
                pre = i + 1
            if i == len(str) - 1:
                res = res + str[pre:][::-1]
            i += 1
                
        return res[::-1]     
