class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = [(p, s) for p, s in zip(position, speed)]
        cars = sorted(cars, reverse=True)
        ans = []

        for car in cars:
            p, s = car[0], car[1]
            t = (target - p)/s

            if ans and t <= ans[-1]:
                pass
            else:
                ans.append(t)
        
        return len(ans)


        
        # cars = sorted([(p, s) for p, s in zip(position, speed)], reverse = True)
        
        # stack = []

        # for idx, car in enumerate(cars):
        #     t = (target - car[0])/car[1]
        #     if stack and t <= stack[-1]:
        #         pass
        #     else:
        #         stack.append(t)
        
        # return len(stack)
