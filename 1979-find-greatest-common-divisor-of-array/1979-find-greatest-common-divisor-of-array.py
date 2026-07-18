class Solution:
    def findGCD(self, nums):
        # Step 1: Find the smallest and largest numbers
        smallest = min(nums)
        largest = max(nums)

        # Step 2: Find GCD using Euclidean Algorithm
        while largest != 0:
            smallest, largest = largest, smallest % largest

        return smallest