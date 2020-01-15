def searchMatrix(self, matrix, target):
        # write your code here
        m = len(matrix)
        n = len(matrix[0])
        i = m - 1
        j = 0
        count = 0
        
        while i >= 0 and j <= n - 1:
            if matrix[i][j] > target:
                i - = 1. #BUG!!! this is one whole operator: -=
            elif matrix[i][j] < target:
                j + = 1. #should be +=
            elif matrix[i][j] == target: 
                i - = 1 #should be ==
                j + = 1 #should be +=
                count + = 1 #should be +=
        
        return count
