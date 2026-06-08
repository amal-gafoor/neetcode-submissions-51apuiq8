class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None
        minVal = nums[0]
        for n in nums:
            minVal = min(minVal,n)
        
        return minVal

