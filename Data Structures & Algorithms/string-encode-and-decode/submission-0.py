class Solution:

    def encode(self, strs: List[str]) -> str:
        # for each str make it encoded
        # cat becomes 3#cat
        # add these encoded strs into encoded arr and 
        # then join that arr for the final encoded str
        encoded = []

        for s in strs:
            e = str(len(s)).zfill(4) + s
            encoded.append(e)

        result = "".join(encoded)

        return result

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            length = int(s[i:i+4])
            start = i + 4
            end = start + length
            decoded.append(s[start:end])
            i = end

        return decoded

