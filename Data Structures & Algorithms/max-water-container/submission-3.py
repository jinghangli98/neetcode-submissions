class Solution:
    def maxArea(self, heights: List[int]) -> int:
        areamax = 0 
        
        l, r = 0, len(heights)-1
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            areamax = max(areamax, area)

            if heights[l] <= heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
        
        return areamax
                