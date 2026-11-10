class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#"  + s

        return encoded

    def decode(self, s: str) -> List[str]:
        output = []
        if len(s) == 0:
            return output
        l = 0
        r = 0
        while r < len(s):
            if s[r] == "#":
                wlen = int(s[l:r])
                output.append(s[r+1: r+1 + wlen])
                
                r = r+1 + wlen
                l = r
            
            else:
                r += 1

                

        return output

