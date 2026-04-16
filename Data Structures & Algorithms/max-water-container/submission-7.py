class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxArea = 0
        while left < right:

            #compute area
            tempArea = (right - left) * min(heights[left],heights[right])

            #compare with max
            if tempArea >= maxArea:
                maxArea = tempArea

            #move pointers (smallest)
            if heights[right] < heights[left]:
                right = right - 1

            else:
                left = left + 1
        
        return maxArea




