class Solution:
    def rob(self, nums: List[int]) -> int:  
        twoBack = 0
        oneBack = 0

        for num in nums:
            current = max(oneBack, twoBack + num)
            twoBack = oneBack
            oneBack = current
        
        return oneBack