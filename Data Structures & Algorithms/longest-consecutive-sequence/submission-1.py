class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        # def 0
        longest = 0
        # check if num - 1 is in set if so add to the seq length
        # and check consec
        # longest is whatever ends up being bigger after comparison
        for num in num_set:
            if num - 1 not in num_set:
                length = 1
                while num + length in num_set:
                    length += 1
                longest = max(longest, length)

        return longest