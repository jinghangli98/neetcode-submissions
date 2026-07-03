class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        ans = [0] * len(temperatures)
        for idx, temp in enumerate(temperatures):

            while stack and temp > stack[-1][0]:
                temperature, day = stack.pop()
                ans[day] = idx - day
            else:
                stack.append([temp, idx])
        
        return ans

