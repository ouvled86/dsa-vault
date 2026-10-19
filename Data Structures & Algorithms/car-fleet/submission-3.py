class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        cars = len(position)
        # arrived = set()
        arrival = [tuple()] * cars
        fleets = []


        for c in range(0, cars):
            arrival[c] = (position[c], (target - position[c]) / speed[c])
        arrival.sort()
        
        for c in range(cars - 1, -1, -1):
            fleets.append(arrival[c])
            if len(fleets) > 1:
                if fleets[-1][1] <= fleets[-2][1]:
                    fleets.pop()
                    
        res = len(fleets)
        # while cars > 0:
        #     added = 0
        #     for c in range(0, len(position)):
        #         if c not in arrived:
        #             position[c] += speed[c]
        #             if position[c] >= target:
        #                 arrived.add(c)
        #                 added += 1
        #     if added > 0:
        #         cars -= added
        #         print(cars)
        #         res += 1

        return res

