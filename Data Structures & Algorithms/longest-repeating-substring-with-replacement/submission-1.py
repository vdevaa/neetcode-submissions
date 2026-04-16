class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        result = 0

        defaultCount = defaultdict(int)
       

        while (right < len(s)):
            defaultCount[s[right]] += 1 # add right to set

            # see what is most frequent letter in defaultCount
            currMax = max(defaultCount, key = defaultCount.get) 
            
            
            tempResult = min(defaultCount[currMax] + k, (right - left + 1))
            result = max(result, tempResult)
            
            if ((right - left + 1) - defaultCount[currMax] <= k): # if we can still replace characters 
                
                right = right + 1 # move right pointer (window is still valid)
            
            else: 
                defaultCount[s[left]] -= 1

                left = left + 1 
                right = right + 1
                

            print(left, right, currMax, defaultCount, tempResult)

        return result


        