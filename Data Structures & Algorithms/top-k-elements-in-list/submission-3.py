class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums) + 1)]
        hashmap=dict()

        for n in nums:
            hashmap[n] = 1 + hashmap.get(n,0)
        
        for key,v in hashmap.items():
            bucket[v].append(key)

        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res
