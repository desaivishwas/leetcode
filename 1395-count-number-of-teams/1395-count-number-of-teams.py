class Solution:
    def numTeams(self, rating: List[int]) -> int:
        # O(n2)
        u_dp = [0 for _ in range(len(rating))]
        l_dp = [0 for _ in range(len(rating))]
        count = 0
        for i in range(len(rating)):
            for j in range(i):
                if rating[j] < rating[i]:
                    count += u_dp[j]
                    u_dp[i] += 1
                else:
                    count += l_dp[j]
                    l_dp[i] += 1
        return count