class Solution:
    def trap(self, height: List[int]) -> int:
        
        max_L = [0] * len(height)
        max_R = [0] * len(height)
        
        lwall = 0
        rwall = 0
        for i in range(len(height)):
            j = - i - 1
            max_L[i] = lwall
            max_R[j] = rwall
            lwall = max(lwall, height[i])
            rwall = max(rwall, height[j])
        
        ans = 0
        for i in range(len(max_L)):
            pot = min(max_L[i], max_R[i])
            water = max(0, pot - height[i])
            ans += water

        return ans
