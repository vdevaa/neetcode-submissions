class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            
            if num in seen:#check to see if number is in set

                return True

            #if not in set add it to
            else:
                seen.add(num)

        return False

        