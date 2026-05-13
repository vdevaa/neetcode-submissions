class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        sMap = defaultdict(int)
        tMap = defaultdict(int)

        # base cases

        if len(s) != len(t):
            return False


        for ch in s:
            sMap[ch] += 1
        
        for ch in t:
            tMap[ch] += 1

        if sMap != tMap:
            return False
        
        return True


        