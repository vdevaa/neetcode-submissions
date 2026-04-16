class Solution:
    def trap(self, height: List[int]) -> int:

        maxRain = 0

        array = []


        for i in range(1, len(height)):

            l = height[i]
            r = height[i]

            # look for max on left
            for x in range(i):
                l = max(l, height[x])
             

            # look for max on right
            for j in range(i + 1, len(height)):
                r = max(r,height[j])
            

            maxRain = maxRain + (min(l,r) - height[i])

        return maxRain

            

            
            








            
        
        