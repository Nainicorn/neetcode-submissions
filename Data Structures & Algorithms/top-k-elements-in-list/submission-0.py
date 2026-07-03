from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        top_k = [val for val, _ in counts.most_common(k)]
        return top_k