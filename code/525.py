# -*- Encoding:UTF-8 -*-

# 525. Contiguous Array

# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
#
# Example 1:
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
# Example 2:
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
# Note: The length of the given binary array will not exceed 50,000.


class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1

        ans = 0
        sum = 0
        d = {0: -1}

        for i in range(len(nums)):
            sum += nums[i]
            if sum in d:
                ans = max(ans, i-d[sum])
            else:
                d[sum] = i
        return ans
