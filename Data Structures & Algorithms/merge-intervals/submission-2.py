class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for interval in intervals[1:]:
            last = merged[-1]

            if interval[0] <= last[1]:
                # overlap to merge
                last[1] = max(last[1], interval[1])
            else:
                # new separate interval
                merged.append(interval)

        return merged