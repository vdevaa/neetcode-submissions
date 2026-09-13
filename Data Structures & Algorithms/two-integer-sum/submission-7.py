class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        seen = defaultdict(int)


        for i in range(len(nums)):

            compliment = target - nums[i] # cal compliment

            if compliment in seen:# se if target in seen

                return [seen[compliment], i]# return indeces

            seen[nums[i]] += i

        
        return False
        