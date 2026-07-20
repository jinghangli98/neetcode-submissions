class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        seen_table = {}
        for num in nums:
            if num in seen_table:
                return True
            else:
                seen_table[num] = 1
        return False