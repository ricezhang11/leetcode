class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        combinations = []
        if nums:  #if nums is not empty
            self.dfsHelper(nums, 0, [], combinations)
        return combinations
        
    def dfsHelper(self, nums, index, combination, combinations):
        combinations.append(list(combination))
        for i in range(index, len(nums)):
            combination.append(nums[i])
            self.dfsHelper(nums, i + 1, combination, combinations)
            combination.pop()  
