class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        maxArea = 0

        while l < r: # if left and right are the same then area = 0

            #compute temp area
            tempArea = (r - l) * (min(heights[l],heights[r]))

            #check if it is max
            if tempArea > maxArea:
                maxArea = tempArea

            # move left or right (which ever one is less)
            if heights[l] < heights[r]:
                l = l + 1
            else:
                r = r - 1
        return maxArea
