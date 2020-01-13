class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        elif target < nums[0]:
            return 0
        elif target > nums[len(nums) - 1]:
            return len(nums)
        
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = int(start + (end - start) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid
        
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        else:
            return start + 1
        
