class Solution:
    def rob(self, nums: List[int]) -> int:  
        twoBack = nums[0]
        if len(nums) >= 2:
            oneBack = max(nums[0], nums[1])
        else:
            return twoBack

        for i in range(2, len(nums)):
            current = max(oneBack, twoBack + nums[i])
            twoBack = oneBack
            oneBack = current
        
        return oneBack