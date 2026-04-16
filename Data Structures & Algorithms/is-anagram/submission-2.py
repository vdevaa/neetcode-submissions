class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # set a hash map (mapping char -> frequency of char (integer))

        sMap = {}
        tMap = {}

        for c in s:
            sMap[c] = sMap.get(c,0) + 1

        for c in t:
            tMap[c] = tMap.get(c,0) + 1
        
        if sMap == tMap:
            return True
        return False