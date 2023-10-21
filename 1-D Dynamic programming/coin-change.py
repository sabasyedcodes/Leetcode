class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1


# Initialize an array to store the minimum number of coins needed for each amount from 0 to the target amount.
        dp = [float('inf')] * (amount + 1)
        
        # The fewest number of coins needed to make change for 0 is 0.
        dp[0] = 0
        
        # Iterate through each coin denomination and update the dp array.
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # If the dp[amount] is still float('inf'), it means it's not possible to make the amount with the given coins.
        return dp[amount] if dp[amount] != float('inf') else -1
