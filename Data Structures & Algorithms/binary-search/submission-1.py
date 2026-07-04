class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        # return half since it wants index
        while left <= right:
            half = (left + right) // 2
            if nums[half] == target:
                return half
            elif nums[half] > target:
                right = half - 1
            else:
                left = half + 1

        return -1
