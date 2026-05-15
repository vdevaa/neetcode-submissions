class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagMap = defaultdict(list)
        
        for wrd in strs:

            mapper = [0] * 26 # set as our key

            for ch in wrd:

                mapper[ord(ch) - ord('a')] += 1

            anagMap[tuple(mapper)].append(wrd)

        
        return list(anagMap.values())

