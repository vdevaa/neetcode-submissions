class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groupMap = defaultdict(list)
        


        for wrd in strs:

            mapper = [0] * 26

            for ch in wrd:

                mapper[ord(ch) - ord('a')] += 1

            groupMap[tuple(mapper)].append(wrd)


        

        
        return list(groupMap.values())