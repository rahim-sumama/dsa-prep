class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # intuition
        """
        take one element from nums1 and compare it with all
        of nums2 elements if matched then store it in new array
        and if already in element then skip it.

        e.g

        1 compare it with 2, 2 -> skip it
        2 compare it with 2 -> matched so store in res[]
        2 compare it with 2 -> already selected so skip it.
        1 compare it with 2, 2 -> no match so skip it.


        using TWO POINTERS approach

        """

        # Approach one: brute force
        result = []
        
        # for i in nums1:
        #     for j in nums2:
        #         if i == j:
        #             result.append(i)
        #             i += 1
        #             break
        
        # i = 0
        # # j = 0
        # while i <= len(nums1)-1:
        #     for j in nums2:
        #         if nums1[i] == j:
        #             result.append(i)
        #             # i += 1
        #             break
        #     i += 1

        # return result

        return list(set(nums1) & set(nums2))
