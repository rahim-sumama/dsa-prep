class Solution:
    def isPalindrome(self, x: int) -> bool:
        # my approach : just applied the palindrome (125) technique
        """
        sx = str(x)
        left = 0
        right = len(sx) - 1

        while left <= right:
            if sx[left] == sx[right]:
                left += 1
                right -= 1             
            if sx[left] != sx[right]:
                return False
            else:
                left += 1
                right -= 1    

            left += 1
            right -= 1
        """
        if x < 0:
            return False
        reverse = 0
        number = x

        while number != 0:
            reverse = reverse * 10 + number % 10
            number = number // 10

        return reverse == x
