class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return nums.index(max(nums[0], nums[1]))
        if nums[0] > nums[1]:  #this problem is different from Lintcode so I modified the answer. If a sorted array counts as "having peak", then I think it's OK to add these conditions, the rest of the code would cover all other conditions. 
            return 0
        if nums[-1] > nums[-2]:
            return len(nums) - 1
        
        start, end = 0, len(nums) - 1
        
        while start + 1 < end:
            mid = int(start + (end - start) / 2)
            
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid
            elif nums[mid] < nums[mid + 1] and nums[mid] > nums[mid - 1]:
                start = mid
            elif nums[mid] > nums[mid + 1] and nums[mid] < nums[mid - 1]:
                end = mid
            else:
                start = mid #I forgot this condition!!! 
                
#         if start - 1 >=0 and start + 1 < len(nums) and nums[start] > nums[start - 1] and nums[start] > nums[start + 1]:
#             return start
#         mid should be able to cover the minimum???? discuss with Frank!
#         if end - 1 >=0 and end + 1 < len(nums) and nums[end] > nums[end - 1] and nums[end] > nums[end + 1]:
#             return end
        
        return -1
                
