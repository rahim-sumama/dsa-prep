class Solution:
    def reverseVowels(self, s: str) -> str:
        # intuition

        """
        1. take two pointers: left and right
            move them towards each other.
        2. Stop at vowel on left and then move the right one if found any vowel then swap both.
        3. else keep it same as it is.
        """


        left = 0
        right = len(s) -1
        w = list(s)
        # for i in range(left, right):
        #     if 
        v = "aeiouAEIOU"
        i = 0
        while left < right:
            while left < right and v.find(w[left]) == -1:
                left += 1
            while left < right and v.find(w[right]) == -1:
                right -= 1

            # if w[left] == v[i] and w[right] == v[i]:
            w[left], w[right] = w[right], w[left]
            
            left += 1
            right -= 1
        return "".join(w)
