class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            # sort each str which becomes key
            # if key exists in dict add the s into [vals] for that key
            # if key doesnt exist, create as new key and empty [vals]
            key = ''.join(sorted(s))
            if key not in d:
                d[key] = []
            d[key].append(s)
        # to return as 2d list use list. on the values only
        return list(d.values())

