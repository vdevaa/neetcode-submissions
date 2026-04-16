class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create a set

        seen = set()
        for num in nums:
            if num in seen: # see if number is in set
                return True # if number in set return True

            else: 
                seen.add(num)# add to set

        return False