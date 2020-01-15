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
    #below is the ninechapter answer. It's much more concise. 
    class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if len(nums) == 0:
            return -1
        
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = int(start + (end - start) / 2)
            if nums[mid] >= nums[start]:
                if nums[start] <= target <= nums[mid]:
                    end = mid 
                else:
                    start = mid
                    
            else:
                if nums[mid] <= target <= nums[end]:
                    start = mid
                else:
                    end = mid #The cases where target is between nums[start] and nums[end] will be covered by this else sentence. In my program, my conditions are too restricted, therefore I have to use else: return -1 to cover all the other situations. also no need to restrict conditions to nums[start]<nums[end], vice versa. The case where the array is not rotated can be integrated into the rotated situation so the entire program is more succinct.  
        
        if nums[start] == target:
                return start
            
        if nums[end] == target:
                return end
           
        return -1
