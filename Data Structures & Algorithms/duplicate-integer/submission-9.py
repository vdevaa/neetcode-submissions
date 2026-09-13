class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        seen = set() # declare a set

        for num in nums:

            if num in seen:
                return True
                
            seen.add(num)#add to set

        return False