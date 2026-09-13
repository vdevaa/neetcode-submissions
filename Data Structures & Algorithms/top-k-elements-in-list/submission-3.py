class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        freqMapper = [[] for i in range(len(nums) + 1)]

        result = []

        for num in nums:
            count[num] += 1

        for num in count:
            freqMapper[count[num]].append(num)

        
        for i in range(len(freqMapper) - 1, 0, -1):
            for num in freqMapper[i]:
                result.append(num)
                if len(result) == k:
                    return result


    