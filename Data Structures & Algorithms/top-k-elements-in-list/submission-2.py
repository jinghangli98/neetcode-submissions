class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        table = {}
        for num in nums:
            if num in table:
                table[num] += 1
            else:
                table[num] = 1
        
        reverse_table = {}
        for num, freq in table.items():
            if freq in reverse_table:
                reverse_table[freq].append(num)
            else:
                reverse_table[freq] = [num]

        ans = []
        for i in range(len(nums), 0, -1):
            if i in reverse_table:
                for num in reverse_table[i]:
                    ans.append(num)
                    if len(ans) == k:
                        return ans

                        

        # sorted_table = sorted(table.items(), key=lambda x:x[1], reverse=True)
        # return [item[0] for item in sorted_table[:k]]
        