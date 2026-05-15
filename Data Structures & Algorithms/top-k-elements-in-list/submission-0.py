class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        res = []
        c = Counter(nums).most_common(k)

        for ch in c:
            res.append(ch[0])


        return res