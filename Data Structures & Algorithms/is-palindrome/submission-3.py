class Solution:
    def isPalindrome(self, s: str) -> bool:

        left = 0

        right = len(s) - 1

        while left <= right:
            if s[left].isalnum() != True: #check valid pointer (is alnum)
                left = left + 1
                continue
                
            if s[right].isalnum() != True: 
                right = right - 1
                continue
                
            if s[right].lower() != s[left].lower(): # compare pointer
                return False
            else:
                left = left + 1
                right = right - 1 #move pointers accordingly
        
        return True
        