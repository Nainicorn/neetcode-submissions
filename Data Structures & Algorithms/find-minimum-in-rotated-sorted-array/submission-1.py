class Solution:
    def findMin(self, nums: List[int]) -> int:
        # O(n)
        # return min(nums)

        # O(lgn) binary search
        res = nums[0]
        # storing index of pointers not val
        l, r = 0, len(nums) - 1
        # while default
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            mid = (l + r) // 2
            res = min(res, nums[mid])

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        
        return res



