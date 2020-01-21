class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        if len(nums) == 1:
            return
        elif k % len(nums) == 0:
            return
        else:
            nums[:((len(nums)-k)%len(nums))] = nums[:((len(nums)-k)%len(nums))][::-1]
            nums[((len(nums)-k)%len(nums)):] = nums[((len(nums)-k)%len(nums)):][::-1] . #interesting thing is that the index can go above the length of array
            nums[:] = nums[::-1]
