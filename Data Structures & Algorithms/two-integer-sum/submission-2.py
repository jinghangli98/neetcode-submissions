class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen_table = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in seen_table:
                return [seen_table[diff], idx]
            else:
                seen_table[num] = idx
