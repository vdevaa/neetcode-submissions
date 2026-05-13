class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        sumMap = defaultdict(int)

        for i in range(len(nums)):

            compliment = target - nums[i] # calc the compliment

            if compliment in sumMap: # seach if compliment is in map
                return [sumMap[compliment], i]
            
            sumMap[nums[i]] += i

            # add to map
        
        return False
        