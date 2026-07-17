class Solution:
    def trap(self, height: List[int]) -> int:
        
        leftmax = [0] * len(height)
        rightmax = [0] * len(height)
        
        lrunning = 0
        rrunning = 0
        for i in range(len(height)):
            j = -i -1
            leftmax[i] = lrunning
            rightmax[j] = rrunning

            lrunning = max(lrunning, height[i])
            rrunning = max(rrunning, height[j])
        
        water = 0
        for i in range(len(height)):
            pot = min(leftmax[i], rightmax[i])
            water += max(0, pot - height[i])
        
        return water