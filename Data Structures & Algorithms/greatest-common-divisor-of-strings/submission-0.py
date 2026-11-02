class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) >= len(str2):
            basestr = str2
        else:
            basestr = str1
        
        x = ""
        i = 1
        while i <= len(basestr):
            factor = basestr[:i]

            if len(str1)%len(factor) != 0 and len(str2)%len(factor) != 0:
                i +=1
                continue
            elif len(str1)//len(factor) * factor != str1 or len(str2)//len(factor) * factor != str2:
                i+=1
                continue
            else:
                x = factor
                i += 1

        return x