class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for idx, num in enumerate(nums):
            
            if target - num in table:
                return [table[target-num], idx]
            else:
                table[num] = idx
        