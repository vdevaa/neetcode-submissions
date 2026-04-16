class Solution:
    def trap(self, height: List[int]) -> int:

        maxRain = 0

        leftMax = [0] * len(height)
        rightMax = [0] * len(height)

        

        n = len(height)

        rightMax[n-1] = height[n-1]
        leftMax[0] = height[0]
        

        for i in range(1, len(height)):
            
            leftMax[i] = max(leftMax[i-1],height[i])

        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        print(rightMax)
        print(leftMax)

        for i in range(len(height)):
            maxRain = maxRain + min(rightMax[i],leftMax[i]) - height[i]
        return maxRain
   
        #print(leftMax)
        #print(rightMax)

        #for i in range(1, len(height)):

        #    l = height[i]
        #   r = height[i]

            # look for max on left
        #    for x in range(i):
        #        l = max(l, height[x])
             

            # look for max on right
         #   for j in range(i + 1, len(height)):
         #       r = max(r,height[j])
            

        #    maxRain = maxRain + (min(l,r) - height[i])

       # return maxRain
 
            

            
            








            
        
        