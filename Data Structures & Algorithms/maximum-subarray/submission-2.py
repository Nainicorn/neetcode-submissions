class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 1 element return element
        if len(nums) == 1:
            return nums[0]
        # if no elements return 0?
        if len(nums) == 0:
            return 0
        
        maxSum = 0
        best = nums[0]
        # keep track of max with max func
        for num in nums:
            maxSum += num
            best = max(maxSum, best)
            if maxSum <= 0:
                maxSum = 0
        
        return best