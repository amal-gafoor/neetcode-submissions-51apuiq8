class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count=dict()
        l=0
        res=0
        val=0
        for r in range(len(s)):
            count[s[r]]=1+count.get(s[r],0)
            for key,v in count.items():
                val=max(val,v)
            if r-l+1 - val <=k:
                res=max(res,r-l+1)
            else:
                count[s[l]]=count.get(s[l],0)-1
                l+=1

        return res

