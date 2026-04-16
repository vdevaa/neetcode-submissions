class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # set a hash map (mapping char -> frequency of char (integer))

        sMap = defaultdict(int)
        tMap = defaultdict(int)

        for c in s:
            sMap[c] += 1

        for c in t:
            tMap[c] += 1
        
        if sMap == tMap:
            return True
        return False