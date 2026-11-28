class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        minlen = 0
        array = set()
        l = 0
        for i in range(len(s)):
            while s[i] in array:
                array.remove(s[l])
                l += 1
            array.add(s[i])
            minlen = max(minlen, len(array))
        return minlen
