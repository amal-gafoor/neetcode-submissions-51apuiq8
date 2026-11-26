class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxl = height[l]
        water = 0
        maxr = height[r]
        while l < r:
            if height[l] < height[r]:
                l += 1
                maxl = max(height[l], maxl)
                water += maxl - height[l]
                

            else:
                r -= 1
                maxr = max(height[r], maxr)
                water += maxr - height[r]
                

        return water

