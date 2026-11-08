class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        output = []
        for s in strs:
            letters = [0] * 26
            for a in s:
                val = ord(a) - ord("a")
                letters[val] += 1
            
            anagram[tuple(letters)].append(s)

        for k,v in anagram.items():
            output.append(v)

        return output