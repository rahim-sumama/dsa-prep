class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        # Intuition

        # approach 1
        # j = 1
        # k = 0
        # missing
        # lastElement = len(nums) - 1
        # while j < len(nums):
        #     for i in range (1, len(nums) - 1):
        #         if i != nums[j]:
        #             missing[k] = i
        #             k += 1
        # return missing






        # approach 2
        # - sort first and then compare the curElem and sorted array elements


        nums.sort()
        result = []

        for i, j in pairwise(nums):
            result.extend(range(i + 1, j))
        return result
