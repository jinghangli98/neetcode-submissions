class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)

        while l <= r:
            mid = (l + r)//2

            time = sum([-(pile//-mid) for pile in piles])

            if time <= h:
                ans = mid
                r = mid - 1

            elif time > h:
                l = mid + 1
        
        return ans
