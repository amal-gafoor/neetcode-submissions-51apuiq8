class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxl = 0
        water = 0
        maxr = 0
        while l < r:
            maxl = max(height[l], maxl)
            maxr = max(height[r], maxr)

            if height[l] < height[r]:
                l += 1
                waterat = min(maxl,maxr) - height[l]
                water = water + max(waterat,0)

            else:
                r -= 1
                waterat = min(maxl,maxr) - height[r]
                water = water + max(waterat,0)

        return water

