class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1

        while left < right:
            if s[left] != s[right]:
              L = s[left+1:right+1]
              R = s[left:right]
              return L == L[::-1] or R == R[::-1]  
            
            left += 1
            right -= 1
        return True