class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # write your code here
        if len(matrix) == 0:
            return False
        elif len(matrix[0]) == 0:
            return False
        
        start = 0
        m = len(matrix)
        n = len(matrix[0])
        end = m * n - 1
        
        
        while start + 1 < end:
            mid = start + (end - start) / 2
            if matrix[int(mid / n)][int(mid % n)] < target:  #mid can be float, therefore here needs to be converted to integers
                start = mid
            elif matrix[int(mid / n)][int(mid % n)] < target:
                return True
            else:
                end = mid
                
        if matrix[int(start / n)][int(start % n)] == target or matrix[int(end / n)][int(end % n)] == target:
            return True
        else:
            return False
