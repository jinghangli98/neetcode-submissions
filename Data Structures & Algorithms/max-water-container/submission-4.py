class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0
        r = len(heights) - 1
        max_area = 0
        
        while l < r:
            area = (r - l) * min(heights[r], heights[l])
            
            if heights[l] <= heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            
            print(max_area)
            max_area = max(area, max_area)
        
        return max_area