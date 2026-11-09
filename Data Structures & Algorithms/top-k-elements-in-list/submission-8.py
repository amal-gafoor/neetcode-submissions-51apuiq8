class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for n in nums:
            hashmap[n] = 1 + hashmap.get(n,0)

        arr = [[] for i in range(len(nums)+1)]
        for key,v in hashmap.items():
            arr[v].append(key)

        res = []
        for n in range(len(arr) -1, 0 ,-1):
            for val in arr[n]:
                res.append(val)
                if len(res) == k:
                    return res

        




