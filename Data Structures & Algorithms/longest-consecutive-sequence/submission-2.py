class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        
        seen = set()

        curMax = 0

        for i in range(len(nums)): #count up list into set
            
            seen.add(nums[i])
        
    
        for num in seen:
            if num - 1 not in seen:
                length = 1 # reset length
                current = num 
        
                while current + 1 in seen:
                    length = length + 1
                    current = current + 1
            
                curMax = max(curMax, length)
        
            
        return curMax



        