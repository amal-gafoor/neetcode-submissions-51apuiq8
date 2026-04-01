class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # a=len(nums)
        # nums=set(nums)
        # b=len(nums)
        # if a==b:
        #     return False
        # else:
        #     return True
        hashset=set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False