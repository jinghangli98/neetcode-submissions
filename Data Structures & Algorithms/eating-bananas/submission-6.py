class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)

        ans = r
        while l <= r:
            mid = (l + r)//2
            
            total_time = sum([-int(-pile//mid) for pile in piles])
            if total_time <= h:
                #eat slower
                ans = mid
                r = mid - 1
            elif total_time > h:
                #eat faster
                l = mid + 1

        return ans   
