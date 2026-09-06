class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # intuition

        """

        1. left and right
        2. Which loop??? Why while loop?
        3. Left pointer -> next
        right pointer -> prev
        then swap Left and Right element
        """

        #  o e l l h
        #  L       R

         
        #  o l l e h
        #      LR

        
        left = 0
        right = len(s) - 1
        
        # code by student
      
        # while left < right:
        #     temp = s[right]
        #     s[right] = s[left]
        #     s[left] = s[temp]

        #     left += 1
        #     right -= 1



        
        while left < right:
            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1
