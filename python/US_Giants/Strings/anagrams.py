class Solution:
    """
    @param strs: A list of strings
    @return: A list of strings
    """
    def anagrams(self, strs):
        # write your code here
        d = dict()
        if not strs:
            return strs
        for st in strs:
            res = ''.join(sorted(st))
            if res not in d.keys():
                d[res] = [st]
            else:
                d[res] = d[res] + [st]
        result = []
        for item in d.values():
            if len(item) >= 2:
                result = result + item
        
        return result
