class Solution:
    def rob(self, nums: list[int]) -> int:
        prev2 = 0
        prev1 = 0

        for money in nums:
            rob_current = money + prev2
            skip_current = prev1

            curr = max(rob_current, skip_current)

            prev2 = prev1
            prev1 = curr
        return prev1