class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count_table = {}
        for idx, num in enumerate(nums):
            if num not in count_table:
                count_table[num] = 1
            else:
                count_table[num] += 1
        
        reverselist = [[freq, num] for num, freq in count_table.items()]
        freq_table = {}
        for i in range(len(reverselist)):
            freq, num = reverselist[i]
            if freq in freq_table:
                freq_table[freq].append(num)
            else:
                freq_table[freq] = [num]
            
        ans = []
        for i in range(len(nums), 0, -1):
            if i in freq_table:
                ans.extend(freq_table[i])

                if len(ans) >= k:
                    return ans

