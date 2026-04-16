class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        result = []


        # logic is a + l + r = 0

        for i, a in enumerate(nums): 
            if i > 0 and a == nums[i-1]: #if we ran into a duplicate or already seen a 
                continue
            
            l = i + 1
            r = len(nums) - 1

            while l < r:
                resSum = nums[l] + nums[r] + a
                if resSum > 0: # if sum is greater than target, we need to move right pointer
                    r = r - 1

                elif resSum < 0: # if sum is less than zero, we need to move the left pointer
                    l = l + 1
                    
                else:
                    result.append([nums[l], nums[r], a]) # found result
                    l = l + 1
                    while nums[l] == nums[l-1] and l < r:
                        l = l + 1
                
        
        return result







                


        