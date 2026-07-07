class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # tracks freq inside window
        count = {}
        left = 0
        # highest freq char
        max_count = 0
        # longest window size
        result = 0

        for right in range(len(s)):
            # store each char count in dict (0 if new, count + 1 if seen)     
            count[s[right]] = count.get(s[right], 0) + 1
            # always track the max char count
            max_count = max(max_count, count[s[right]])

            window_size = right - left + 1
        
            while window_size - max_count > k:
                count[s[left]] -= 1  
                left += 1           
                window_size = right - left + 1

            result = max(result, window_size)

        return result
