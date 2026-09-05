class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # intuition
        """
        use two pointers approach to and compare the array element with the target value if matched, remove it else ignore it and return the end array.
        """
        
        # student approach - Ali
        # left = 0
        # right = len(nums) - 1
        # newIndex = 0
        # while left <= right:
        #     if nums[left] != val:
        #         nums[newIndex] = nums[left]
        #         newIndex += 1
        #     if nums[right] != val:
        #         nums[newIndex] = nums[right]
        #         newIndex -= 1
        #     left += 1
        #     right -= 1
        # return newIndex
        
        
        # my approach
        curr = 0 # current position

        for i in range(len(nums)):
            if nums[i] != val:
                nums[curr] = nums[i]
                curr += 1
        
        return curr
