class Solution:
    def helper(self, nums: List[int]) -> int:
        twoBack = 0
        oneBack = 0
        for num in nums:
            current = max(oneBack, twoBack + num)
            twoBack = oneBack
            oneBack = current
        return oneBack

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        withoutFirst = nums[1:]
        withoutLast = nums[:-1]

        return max(self.helper(withoutFirst), self.helper(withoutLast))