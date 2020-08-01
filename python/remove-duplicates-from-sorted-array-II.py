class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return -1
        
        i, length = 0, len(nums)
        j = i + 1
        
        while j <= length - 1:
            if nums[i] == nums[j]:

                if j - i == 2:
                    length = length - 1
                    for k in range(j, len(nums) - 1):
                        nums[k] = nums[k + 1]
                        j -= 1
                j += 1
            else:
                i = j
                j = i + 1
        
        # print (length)
        
        for l in range(0, length):
            print(nums[l])
        
        #same question! how to do the output?
        
