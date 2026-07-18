class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        ans = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            
            while stack and temp > stack[-1][1]:
                pos, pos_temp = stack.pop()
                ans[pos] = idx - pos

            stack.append([idx, temp])
        
        return ans

