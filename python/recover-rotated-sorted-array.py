class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        if not nums:
            return -1
        if len(nums) == 1:
            return nums
        
        index = -1
        
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                index = i
                break
        
        if index != -1:
            nums[:index] = nums[:index][::-1]
            nums[index:] = nums[index:][::-1]
            nums[:] = nums[::-1]
        
        return
   
