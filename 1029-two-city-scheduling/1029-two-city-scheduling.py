class Solution:
    def twoCitySchedCost(self, costs: list[list[int]]) -> int:
        costs.sort(key = lambda x : x[0] - x[1])

        n = len(costs) // 2
        total = 0

        # first n people go to city A
        for i in range(n):
            total += costs[i][0]

        # Remaining n people go to city B
        for i in range(n, len(costs)):
            total += costs[i][1]

        return total
        