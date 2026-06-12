class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        seen_table = {}
        for idx, num in enumerate(numbers):
            diff = target - num
            if diff in seen_table:
                return [seen_table[diff]+1, idx+1]
            else:
                seen_table[num] = idx