class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        ans = r

        while l <= r:
            mid = l + (r - l) // 2

            total_time = sum((pile + mid - 1) // mid for pile in piles)

            if total_time <= h:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans