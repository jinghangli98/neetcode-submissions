class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        table = {}
        for num in nums:
            if num in table:
                table[num] += 1
            else:
                table[num] = 1
        
        
        freq_table = {}
        for val, freq in table.items():
            if freq in freq_table:
                freq_table[freq].append(val)
            else:
                freq_table[freq] = [val]

        ans = []
        for i in range(len(nums), 0, -1):
            if len(ans) == k:
                return ans
            
            if i in freq_table:
                ans.extend(freq_table[i])

        return ans
            