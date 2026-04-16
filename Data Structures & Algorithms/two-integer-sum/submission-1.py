class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        intMap = {}
        compliment = 0

        for i in range(len(nums)):
            #calculate compliment
            compliment = target - nums[i]

            if compliment in intMap:
                return [intMap[compliment],i]
            # if complement in set
                #return indeces
            
            # if not in set
            else:
                intMap[nums[i]] = i
                #add to set
        

        return 0
        