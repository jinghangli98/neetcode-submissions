class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        table = {}
        for num in nums:
            if num in table:
                table[num] += 1
            else:
                table[num] = 1
        
        freq_table = {}
        for num, freq in table.items():
            if freq in freq_table:
                freq_table[freq].append(num)
            else:
                freq_table[freq] = [num]
        
        ans = []
        for i in range(len(nums), 0, -1):
            if len(ans) == k:
                return ans

            if i in freq_table:
                ans.extend(freq_table[i])
        
        return ans

