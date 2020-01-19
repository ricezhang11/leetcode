class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return s
        
        s = s.strip()
        l = s.split()
        i, j = 0, len(l) - 1
        
        while i < j:
            # temp = l[i]
            # l[i] = l[j]
            # l[j] = temp
            l[i], l[j] = l[j], l[i]
            i += 1
            j -= 1
            
        result = " ".join(l)
        return result
