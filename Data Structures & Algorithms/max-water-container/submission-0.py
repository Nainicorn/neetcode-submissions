class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointer again wah
        left = 0
        right = len(heights) - 1
        max_water = 0
        # always left right while just the inner loop logic changes
        # height is always min of the 2
        # inc or dec based on which is smaller
        while left < right:
            width = right - left
            current_height = min(heights[left], heights[right])
            current_water = width * current_height

            max_water = max(max_water, current_water)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_water