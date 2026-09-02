class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        
        # intuition
        """
        first I will have to remove one character
        but which one should have to remove?

        -- I think if there is any one character which is repeated that should be removed, so the remaing can make a palinedrome if it is.
        -- To do this, I need to skip 1 char from left or right and need to check palinedrome validation

        then just apply two pointers approach to find, it is palinedrome or not?

        """

        # solution

        def isPalinedrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return isPalinedrome(left + 1, right) or isPalinedrome(left, right - 1)
            left += 1
            right -= 1
        return True
