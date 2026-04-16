class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0

        right = len(numbers) - 1

        while left < right:

            lrSum = numbers[left] + numbers[right]#compute the target sum

            if lrSum == target: #see if its the target
                return [left + 1, right + 1]

            if lrSum > target:#move right pointer down if computation is larger than target
                right = right - 1
            
            if lrSum < target:#move the left pointer up if the computation is smaller than the target
                left = left + 1
        
        return 0