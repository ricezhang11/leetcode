def compareStrings(self, A, B):
        # write your code here
        d = dict()
        if A == None and A != B:
            return False
            
        if A != None and B == None:
            return True
            
        for ch_A in A:
            if ch_A not in d.keys():
                d[ch_A] = 0
                d[ch_A] += 1
            else:
                d[ch_A] += 1
        
        for ch_B in B:
            if ch_B not in d.keys():
                return False
            else:
                d[ch_B] -= 1
        
        for val in d.values():
            if val < 0:
                return False
        
        return True
