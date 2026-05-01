class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # read input
        # add value to stack
        # read input
        # if next value is greater than top of stack pop from stack and compute days
        # else add next value to stack

        result = [0] * len(temperatures)
        stack = [] 


        for day, temp in enumerate(temperatures):

            

            while stack and temp > stack[-1][0]:
                currTemp, currDay = stack.pop() # pop
                result[currDay] = day - currDay # compute days
            
            stack.append((temp,day)) # add day

        return result

