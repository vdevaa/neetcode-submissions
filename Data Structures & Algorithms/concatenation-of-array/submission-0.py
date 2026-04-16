class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(2):
            for x in nums:
                result.append(x)
        
        return result
        