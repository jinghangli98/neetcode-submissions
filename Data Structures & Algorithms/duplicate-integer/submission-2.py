class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_table = {}
        for idx, num in enumerate(nums):
            if num in seen_table: 
                seen_table[num] += 1
                return True
            else:
                seen_table[num] = 1
        
        return False