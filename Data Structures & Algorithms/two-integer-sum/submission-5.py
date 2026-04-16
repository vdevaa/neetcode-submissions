class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # number -> index in list

        sumDict = defaultdict(int)

        for i in range(len(nums)):
            compliment = target - nums[i]# calcualte compliment

            if compliment in sumDict:# see if compliment in list
                return [sumDict[compliment],i]
            sumDict[nums[i]] = i
            # add to dict
        return nums