class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        intMap = defaultdict(int)
        compliment = 0

        for i in range(len(nums)):
            compliment = target - nums[i]

            if compliment in intMap:
                return [intMap[compliment],i]
            else:
                intMap[nums[i]] = i


        