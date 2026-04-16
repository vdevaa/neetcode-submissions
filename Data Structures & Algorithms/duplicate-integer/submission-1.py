class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Create a set
        numSet = set()
        # Iterate through list
        for num in nums:
            # Check to see if iteration is in set
            if num in numSet:

                return True

            # if not add to set

            else:

                numSet.add(num)



         
         # return false if out of loop
        return False