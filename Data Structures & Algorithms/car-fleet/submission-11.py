class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = sorted([[p,v] for p, v in zip(position, speed)], reverse=True)
        stack = []
        for car in cars:
            
            p, v = car
            t = (target - p )/v

            if stack and t <= stack[-1]:
                continue
            else:
                stack.append(t)
            
        return len(stack)
            

