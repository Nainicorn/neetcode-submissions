class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # length of nums to iterate through
        n = len(nums)
        # prefix/suffix approach def start 1 bc mult
        # prefix to the left
        # suffix to the right
        prefix, suffix, result = [1] * n, [1] * n, [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        for i in range(n):
            result[i] = prefix[i] * suffix[i]

        # drawn out one ex

        return result