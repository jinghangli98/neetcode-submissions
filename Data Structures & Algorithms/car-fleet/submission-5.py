class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = sorted([(p, s) for p, s in zip(position, speed)], reverse = True)
        
        stack = []

        for idx, car in enumerate(cars):
            t = (target - car[0])/car[1]
            if stack and t <= stack[-1]:
                continue
            
            stack.append(t)
        
        return len(stack)
