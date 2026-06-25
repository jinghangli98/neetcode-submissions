class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:        
        i = 0

        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            j = i + 1
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    ans[i] = j - i
                    break
                
        
        return ans