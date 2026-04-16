class Solution:
    def maxArea(self, heights: List[int]) -> int:

        currMax = 0

        left = 0

        right = len(heights) - 1

        while left < right:

            tempArea = (right - left) * min(heights[left],heights[right]) #compute area

            if tempArea > currMax: #compare w currMax
                currMax = tempArea

            if heights[left] < heights[right]:#move left or right
                left = left + 1
            
            else:
                right = right - 1
        
        return currMax
        