class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        q = collections.deque()
        ans = []
        l = 0
        for r in range(len(nums)):

            while q and nums[r] > q[-1]:
                q.pop()
            
            q.append(nums[r])

            if r + 1 >= k :
                ans.append(q[0])

                if q[0] == nums[l]:
                    q.popleft()
                l += 1
        
        return ans