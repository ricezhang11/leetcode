class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = dict()
        if s == None or t == None and s != t:
            return False
        for ch_s in s:
            if ch_s not in d.keys():
                d[ch_s] = 0
                d[ch_s] += 1
            else:
                d[ch_s] += 1
        
        for ch_t in t:
            if ch_t not in d.keys():
                return False
            else:
                d[ch_t] -= 1
        
        for val in d.values():
            if val != 0:
                return False
        
        return True
