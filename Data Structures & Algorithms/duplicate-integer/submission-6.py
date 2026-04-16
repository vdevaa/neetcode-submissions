class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        seen = set()

        for num in nums:

            if num in seen:# check to see if its in set

                return True
            
            seen.add(num)# logic (adding to the set)
        
        return False
            
