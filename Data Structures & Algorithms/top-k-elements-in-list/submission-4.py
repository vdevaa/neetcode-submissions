class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freqMap = [[] for i in range (len(nums) + 1)]

        count = defaultdict(int)

        result = []

        for num in nums:
            count[num] += 1

        
        for num in count:
            freqMap[count[num]].append(num)

        for i in range(len(freqMap) - 1, 0, -1):
            for num in freqMap[i]:
                result.append(num)
                if len(result) == k:
                    return result

    

        return []

        