class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        ## map number -> index (in list)

        sumMap = {}
        compliment = 0

        for i in range(len(nums)):

            compliment = target - nums[i] #eval compliment (number we are looking for)

            if compliment in sumMap:

                return [sumMap[compliment], i]

            sumMap[nums[i]] = i
            
        return 0
