class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])  # sort by start value

        result = [intervals[0]]

        for interval in intervals[1:]:
            last = result[-1]  # the most recent interval we've added

            if interval[0] <= last[1]:
                # overlap (or touching) — merge into the last one
                last[1] = max(last[1], interval[1])
            else:
                # no overlap — this is a new, separate interval
                result.append(interval)

        return result