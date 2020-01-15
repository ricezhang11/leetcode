class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        if len(nums) == 2:
            if nums[0] == target:
                return 0
            elif nums[1] == target:
                return 1
     
        start, end = 0, len(nums) - 1
        
        while start + 1 < end:
            mid = int(start + (end - start) / 2)
                
            if nums[end] < nums[start] and nums[mid] > nums[start]: 
                if target > nums[mid]:
                    start = mid
                elif target < nums[mid] and target >= nums[start]:
                    end = mid
                elif target < nums[mid] and target <= nums[end]:
                    start = mid
                elif target == nums[mid]:
                    return mid
                else:
                    return -1
            
            elif nums[end] < nums[start] and nums[mid] < nums[end]:
                if target < nums[mid]:
                    end = mid
                elif target > nums[mid] and target >= nums[start]:
                    end = mid
                elif target > nums[mid] and target <= nums[end]:
                    start = mid
                elif target == nums[mid]:
                    return mid
                else: 
                    return -1
                     
            elif nums[end] > nums[start]:
                if target < nums[mid]:
                    end = mid
                elif target > nums[mid]:
                    start = mid
                elif target == nums[mid]:
                    return mid
            
            if nums[start] == target:
                return start
            
            if nums[end] == target:
                return end
           
        return -1
