class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        maxArea = 0

        while l < r:
            # calcualte the area
            tempArea = (r - l) * min(heights[l], heights[r])
            # compare that with max Area
            if tempArea > maxArea:
                maxArea = tempArea


            # mvoe left or right pointer (whichever is the smallest)
            if heights[l] < heights[r]:
                l = l + 1
            else:
                r = r - 1
        
        return maxArea