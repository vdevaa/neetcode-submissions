class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        intMap = {}

        compliment = 0

        for i in range(len(nums)):
            #find compliment
            compliment = target - nums[i]

            if compliment in intMap:#if compliment is in map
                return [intMap[compliment],i]#return indexes

            else:#if it is not map
                intMap[nums[i]] = i#add nuber to map and assing to index

            
        