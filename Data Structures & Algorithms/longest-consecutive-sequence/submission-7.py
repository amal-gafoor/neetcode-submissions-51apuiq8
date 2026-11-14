class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numset = set(nums)
        for val in numset:
            if (val - 1) not in numset:
                length = 1
                while (val+length) in numset:
                    length += 1
                longest = max(length, longest)

        return longest
        

