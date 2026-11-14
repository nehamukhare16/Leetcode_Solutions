
class Solution:
    def minimumSumSubarray(self, nums, l, r):

        minimum = float('inf')
        n = len(nums)

        for i in range(n):

            total = 0

            for j in range(i, n):

                total += nums[j]

                length = j - i + 1

                if l <= length <= r and total > 0:
                    minimum = min(minimum, total)

        if minimum == float('inf'):
            return -1

        return minimum
