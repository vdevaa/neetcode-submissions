class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        currMax = 0

        while left < right:
            tempArea = (right - left) * min(heights[right],heights[left])

            if tempArea > currMax:
                currMax = tempArea
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            
        return currMax
            
        