class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        l = 0
        seen = {}
        for r in range(len(nums)):
            if r-l >k:
                seen[nums[l]] -= 1
                if seen[nums[l]] == 0:
                    del seen[nums[l]]
                l += 1

            if nums[r] in seen:
                return True                

            else:
                seen[nums[r]] = 1

        return False

        




























        # l = 0 
        # seen_table = {}
        # for r in range(len(nums)):
        #     if r-l > k:
        #         seen_table[nums[l]] = seen_table[nums[l]] - 1
        #         if seen_table[nums[l]] == 0 :
        #             del seen_table[nums[l]]
        #         l += 1

        #     if nums[r] in seen_table:
        #         return True
        #     else:
        #         seen_table[nums[r]] = 1

        # return False
        

            
