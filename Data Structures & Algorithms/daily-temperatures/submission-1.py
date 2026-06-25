class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:        
        # i = 0

        # ans = [0] * len(temperatures)
        # for i in range(len(temperatures)):
        #     j = i + 1
        #     for j in range(i + 1, len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             ans[i] = j - i
        #             break
                
        
        # return ans
        stack = []
        ans = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):

            while stack and stack[-1][0] < temp:

                stack_t, stack_i = stack.pop()
                ans[stack_i] = i - stack_i
            
            stack.append((temp, i))
        
        return ans

