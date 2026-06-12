class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l = 0
        r = len(people)-1
        people = sorted(people)
        ans = 0
        while l <= r:
            weight_sum = people[l] + people[r]
            if weight_sum <= limit:
                ans += 1
                l += 1
                r -= 1
            else:
                ans += 1
                r -= 1
        
        return ans


