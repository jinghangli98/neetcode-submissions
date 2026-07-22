class Solution:
    def trap(self, height: List[int]) -> int:
        
        lmax = [0] * len(height)
        rmax = [0] * len(height)
        lrunning = 0
        rrunning = 0
        for i in range(len(height)):
            j = -i -1
            lmax[i] = lrunning
            lrunning = max(lrunning, height[i])

            rmax[j] = rrunning
            rrunning = max(rrunning, height[j])
        
        water = 0
        for i in range(len(height)):

            pot = min(lmax[i], rmax[i])
            water += max(pot - height[i], 0)
        
        return water



