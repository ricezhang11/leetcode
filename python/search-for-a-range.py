class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        start, end = 0, len(A)- 1
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
        elif A[end] == target:
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
