from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
         
        # car cannot passs car ahead
        # - aka its capped by the car speed ahead of it
        
        # if car a catches up to car b then car A will merge and become car b fleet

        # given car speed and position
        # process them
        # and return the number of car fleet we will end up having

        # process their speed

        # time = distance/speed

        # target = 10
        # position = [4, 1, 0, 7]       # sorted position [0, 1, 4, 7]
        # speed    = [2, 2, 1, 1]


        # 10-7 = 3
        # 3/1 = 3

        # 10-0 = 10
        # 10/1 = 10

        # 10-1 = 9
        # 9/2 = 4.5

        # 10-4 = 6
        # 6/2 = 3

        # car A   car B

        # if car A time is lower than car B then car A will join car B fleet

       
        pos_and_speed = []

        for i in range(len(speed)):
            pos_and_speed.append([position[i], speed[i]])

        pos_and_speed.sort()

        time = [0] * len(speed)
        
        for i in range(len(speed)):
            # (target - position[i]) / speed[i]
            time[i] = (target - pos_and_speed[i][0]) / pos_and_speed[i][1]
        

        stack = []
        for i in range(len(speed)-1, -1, -1):
            # if lower or equal -> combine the fleet
            # combine aka we dont append to the stack
            if stack and time[i] <= stack[-1]:
                continue
            
            stack.append(time[i])
            
        return len(stack)