class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        start, end = 0, len(A)- 1  #to get the length of python list, use len(list) instead of list.size(). 
                                   #len() is python's built-in function and can take a sequence like tuple, string, list etc. 
        if len(A) == 0:
            return [-1, -1]
            
        while start + 1 < end:     
            mid = start + (end - start) / 2
            if A[mid] < target:
                start = mid
            else:
                end = mid
        
        if A[start] == target:
            lowerBound = start
        elif A[end] == target:   #python uses elif, not else if....
            lowerBound = end
        else:
            lowerBound = -1
            
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if A[mid] <= target:
                start = mid
            else:
                end = mid
        
        if A[end] == target:
            upperBound = end
        elif A[start] == target:
            upperBound = start
        else:
            upperBound = -1
        
        return [lowerBound, upperBound]
