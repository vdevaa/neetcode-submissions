class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left <= right:
            
            if s[left].isalnum() != True:#check to see if characyer is valid
                
                left += 1 #if not valid move pointer depending on which character
                continue
            if s[right].isalnum() != True:
                right -= 1
                continue
            if s[left].lower() != s[right].lower():#check to see if they are same after two valid characyers
                return False

            else: #increment pointers
                left += 1
                right -= 1

        
        return True
        