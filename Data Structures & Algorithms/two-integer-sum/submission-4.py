class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = dict()
        for key,val in enumerate(nums):
            if (target-val) in numMap:
                return [numMap[target-val],key]
            numMap[val] = key

        return []