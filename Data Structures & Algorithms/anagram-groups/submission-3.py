class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordDict = defaultdict(list)

        for word in strs:
            key = [0] * 26
            
            for ch in word:
                key[ord(ch) - ord("a")] += 1
            
            wordDict[tuple(key)].append(word)
        
        return list(wordDict.values())