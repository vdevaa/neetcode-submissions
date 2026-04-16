class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0
        r = len(heights) - 1

        maxArea = 0

        while l < r:

            tempArea = (r - l) * (min(heights[l],heights[r])) #compute the area

            if tempArea > maxArea:#set to maxArea if max
                maxArea = tempArea
        
            if heights[r] <= heights[l]:
                r = r - 1
            else:
                l = l + 1

        
        return maxArea
        