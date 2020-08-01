class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 0:
            return False
        
        i = 0
        while i < len(nums):
            if nums[i] == target:
                return True
            i += 1
        
        return False
