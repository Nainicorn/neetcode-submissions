class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # in place sort
        result = []

        for i in range(len(nums)):
            # skip duplicate "first numbers" so we don't get repeat triplets
            # edge check
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # skip duplicates for left and right too
                    # dupe handling is hard because you cant remove
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1

        return result