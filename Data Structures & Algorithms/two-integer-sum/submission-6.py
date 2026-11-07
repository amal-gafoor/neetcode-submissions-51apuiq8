class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        library = dict()

        for i,k in enumerate(nums):
            if k in library:
                return [library[k],i]
            diff = target - k
            library[diff] = i
        return []
