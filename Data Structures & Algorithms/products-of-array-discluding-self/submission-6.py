class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tempnum = 1
        output = nums.copy()
        for i in range(len(nums)):
            output[i] = tempnum
            tempnum = nums[i] * tempnum
        tempnum2 = 1
        for i in range(len(nums)-1,-1,-1):
            output[i] = output[i] * tempnum2
            tempnum2 = nums[i] * tempnum2

        return output