class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = set()

        for num in nums:

            if num in seen:#check if in set

                return True

            seen.add(num)
        
        return False