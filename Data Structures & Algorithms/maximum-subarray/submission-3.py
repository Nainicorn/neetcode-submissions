class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = 0
        best = nums[0]
        # keep track of max with max func
        for num in nums:
            maxSum += num
            best = max(maxSum, best)
            if maxSum <= 0:
                maxSum = 0
        
        return best