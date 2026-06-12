class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        l = 0
        sub_sum = 0
        tracker = 0
        for r in range(len(arr)):
            sub_sum += arr[r]
            if r - l + 1 == k:
                sub_ave = sub_sum/k
                if sub_ave >= threshold:
                    tracker += 1
                sub_sum -= arr[l]
                l += 1
        
        return tracker

