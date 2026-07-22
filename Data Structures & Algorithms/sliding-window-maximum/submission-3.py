class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        l = 0
        q = collections.deque()
        ans = []
        for r in range(len(nums)):

            while q and q[-1] < nums[r]:
                q.pop()

            q.append(nums[r])
            
            if r >= k -1:
                ans.append(q[0])

                if q[0] == nums[l]:
                    q.popleft()
                
                l += 1
        
        return ans