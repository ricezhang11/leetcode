class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = int(start + (end - start) / 2)
            if nums[mid] < nums[end]:
                end = mid
            elif nums[mid] > nums[end]:
                start = mid
        
        return min(nums[start], nums[end])
