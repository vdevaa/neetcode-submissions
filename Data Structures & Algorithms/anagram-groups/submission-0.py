class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        freqDict = defaultdict(list)

        for wrd in strs:

            mapper = [0] * 26

            for c in wrd:
                mapper[ord(c) - ord("a")] += 1
            
            freqDict[tuple(mapper)].append(wrd)
        
        return list(freqDict.values())


        