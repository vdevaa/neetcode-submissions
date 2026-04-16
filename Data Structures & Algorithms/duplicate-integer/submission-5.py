class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenInts = set()

        for num in nums:

            if num in seenInts:
                return True
            
            seenInts.add(num)
        

        return False

        