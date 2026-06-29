class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)
        ans = r

        import math 
        while l <= r:
            mid = l + (r-l)//2

            total_time = sum([math.ceil(pile/mid) for pile in piles])
            if total_time <= h:

                ans = mid
                r = mid - 1

            elif total_time > h:
                #needs to eat faster
                l = mid + 1
        
        return ans

            