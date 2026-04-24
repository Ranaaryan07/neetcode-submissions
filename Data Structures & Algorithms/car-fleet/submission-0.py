class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=list(zip(position,speed))
        stacks=[]
        cars.sort(reverse=True)
        for pos,spd in cars:
            time=(target-pos)/spd
            if not stacks or time>stacks[-1]:
                stacks.append(time)
        return len(stacks)