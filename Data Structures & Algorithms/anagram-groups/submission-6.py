class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        for s in strs:
            letters = [0] * 26
            for a in s:
                letters[ord(a) - ord("a")] += 1
            anagram[tuple(letters)].append(s)
           


        return list(v for k,v in anagram.items())