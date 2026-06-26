class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        for rock in asteroids:
            alive = True
            #if rock is going left check if stack[-1] is going right
            #if going right then decide if we need to pop the stack or append the rock (not only once)

            while stack and rock < 0 and stack[-1] > 0:
                if abs(stack[-1]) > abs(rock):
                    #no need to append, the incoming rock is crushed 
                    alive = False
                    break
                elif  abs(stack[-1]) < abs(rock):
                    #last stack is crushed and the incoming rock gets append
                    stack.pop()
                    continue
                elif abs(stack[-1]) == abs(rock):
                    stack.pop()
                    alive = False
                    break
                    
            if alive:
                stack.append(rock)

        return stack