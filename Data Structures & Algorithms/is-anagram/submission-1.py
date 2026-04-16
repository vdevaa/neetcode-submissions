class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        freqS = defaultdict(int)
        freqT = defaultdict(int)

        #count up s
        for c in s:
            freqS[c] += 1

        #count up t
        for c in t:
            freqT[c] += 1

        if freqS != freqT: #if they are not the same return false
            return False

        return True
        