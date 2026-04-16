class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0

        right = len(numbers) - 1

        

        while left < right:
            #compute sum of left and right
            lrSum = numbers[left] + numbers[right]

            if lrSum > target:#if sum is too big,

                right = right - 1#move right pointer

            if lrSum < target:#if sum is too small

                left = left + 1#move left pointer

            if lrSum == target:#if sum is equal to 
                return [left + 1, right + 1]

        return []
     
        