class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.append(n)
        cuts.insert(0, 0)
        cuts.sort()
        c = len(cuts)
        dp = [[0 for _ in range(len(cuts))] for _ in range(len(cuts))]

        for gap in range(2, len(cuts)):
            i, j = 0, gap
            while i < len(cuts) and j < len(cuts):

                # To store the cost.
                totalCost = float('inf')

                # Try cuts.
                for k in range(i + 1, j):

                    # Find minimum.
                    totalCost = min(totalCost, dp[i][k] + dp[k][j])

                # Update cost.
                dp[i][j] = totalCost + (cuts[j] - cuts[i])
                i += 1
                j += 1

        return dp[0][len(cuts) - 1]