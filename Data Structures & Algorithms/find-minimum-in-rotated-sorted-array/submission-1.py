class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = nums[0]
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] < nums[right]: # if left is less than right then we know we are in sorted window,
                                         # so return result (current mid) or left
                result = min(nums[left],result)
                break

            mid = (left + right) // 2
            print(f"Left: {nums[left]} Right: {nums[right]} Mid: {nums[mid]}")
            result = min(result, nums[mid])

            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        
        
        return result