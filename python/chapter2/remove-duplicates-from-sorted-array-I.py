class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return -1
        index, length = 0, len(nums)
        
        while index + 1 < length:
            if nums[index] == nums[index + 1]:
                length -= 1
                for i in range(index, len(nums)-1):
                    nums[i] = nums[i + 1]
                index += 1
        
        for j in range(0, length):
            print(nums[j])
         #Question! why this doesn't work?? why have to return an integer????? let Frank see my code and give suggestions.  
