class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        table = {}
        for num in nums:
            if num in table:
                table[num] += 1
            else:
                table[num] = 1
        
        sorted_table = sorted(table.items(), key=lambda x:x[1], reverse=True)
        
        return sorted_table[0][0]
