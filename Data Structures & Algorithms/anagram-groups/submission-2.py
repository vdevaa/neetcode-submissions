class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagMap = defaultdict(list)

        for wrd in strs:

            mapper = [0] * 26

            for ch in wrd:
                mapper[ord(ch) - ord('a')] += 1 # key (freq of all chars)

            anagMap[tuple(mapper)].append(wrd) # add value

        return list(anagMap.values())
