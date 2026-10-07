class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max_product = nums[0]
        min_product = nums[0]
        answer = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                max_product, min_product = min_product, max_product

            max_product = max(nums[i], max_product * nums[i])
            min_product = min(nums[i], min_product * nums[i])

            answer = max(answer, max_product)
        return answer
        
        