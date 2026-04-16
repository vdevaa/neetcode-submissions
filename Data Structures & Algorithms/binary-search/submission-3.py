class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0

        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            print(mid)

            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                right -= 1
            if nums[mid] < target:
                left += 1
            
        return -1
        