class Solution:
    def removeElement(self, A: List[int], elem: int) -> int:
# not workable solution using two pointers: problem is index goes out of bound. difficult to cover all edge cases. 
#         if not A:
#             return 0

#         i, j = 0, len(A) - 1
#         while i <= j:
#             while A[j] == elem:
#                 j -= 1
#                 if j < 0:
#                     return 0
                
#             if A[i] == elem:
#                 A[i], A[j] = A[j],A[i]
#             i += 1
        
#         if A[i] == elem:
#             return i
#         else:
#             return i + 1

# less ideal solution using dynamic length
#         i  = 0
#         l = len(A)
#         if not A:
#             return 0
        
#         while i != l:
#             while A[-1] == elem:
#                 A.pop()
#                 l -= 1
#                 if i == l:
#                     i -= 1
#                 if l == 0:
#                     return 0
#             if A[i] == elem:
#                 A[i], A[-1] = A[-1], A[i]
#             i += 1
        
#         return l
    
#workable solution using dynamic length    
        i  = 0
        l = len(A)
        if not A:
            return 0
        
        while i != l:
            while A[-1] == elem:
                A.pop()
                l -= 1
 #this line is very important. avoid the situation where the set has been popped to empty but i still stay there
 #then the next command will get index out of range.
                if l == i:  
                    return l
            if A[i] == elem:
                A[i], A[-1] = A[-1], A[i]
            i += 1
        
        return l
