class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        maximum_area=0
        while left<right:
            width=right-left
            h=min(heights[left],heights[right])
            area =width*h
            maximum_area=max(maximum_area,area)
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return maximum_area

        