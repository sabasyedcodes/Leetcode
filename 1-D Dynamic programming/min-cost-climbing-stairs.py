https://leetcode.com/problems/min-cost-climbing-stairs/description/

# theory and explanation is from leetcode soln section I have saved it as fav

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        # we jumping in reverse order that is top to bottom
        for i in range(len(cost)-4,-1,-1):
            cost[i] += min(cost[i+1],cost[i+2])
        return min(cost[0],cost[1])
    