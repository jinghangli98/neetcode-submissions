class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency_table = {}
        for num in nums:
            if num in frequency_table:
                frequency_table[num] += 1
            else:
                frequency_table[num] = 1
        
        table = {}
        for num, freq in frequency_table.items():
            if freq in table:
                table[freq].append(num)
            else:
                table[freq] = [num]
                
        ans = []
        for i in range(len(nums), 0, -1):
            
            if i in table:
                ans.extend(table[i])
            
            if len(ans) >= k:
                return ans
        
        


        
