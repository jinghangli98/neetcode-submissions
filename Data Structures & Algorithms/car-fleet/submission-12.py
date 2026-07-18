class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = []
        cars = sorted([[p,s] for p, s in zip(position, speed)], reverse=True)
        
        for i in range(len(cars)):
            p = cars[i][0]
            s = cars[i][1]
            val = (target - p)/s

            if stack and val <= stack[-1]:
                continue
                
            else:
                stack.append(val)
                
                    
        return len(stack)



