# https://leetcode.com/problems/coin-change-ii/description/

class Solution(object):
    def change(self, amount, coins):
        """
        Calculate the number of combinations to make up the given amount using the provided coins.

        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # Create a dp array to store the number of combinations for each amount
        # this line of code initializes the dynamic programming array dp with (amount + 1) elements,
        # where each element represents the number of combinations for a specific amount.
        # Initially, all elements are set to 0. As we iterate through the coins and update the combinations,
        # we'll populate this array with the correct values representing the number of combinations for each amount.
        dp = [0] * (amount + 1)
        # There's only one combination to make amount 0, i.e., by not choosing any coin
        dp[0] = 1

        # Iterate through each coin
        for coin in coins:
            # Update dp array for each amount starting from the current coin value
            for i in range(coin, amount + 1):
                # The number of combinations for amount i is the sum of the number of combinations for (i - coin) and current amount i
                dp[i] += dp[i - coin]

        # Return the number of combinations for the given amount
        return dp[amount]

#####################

# COIN CHANGE II
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.
# You may assume that you have an infinite number of each kind of coin.
# The answer is guaranteed to fit into a signed 32-bit integer.

# Time Complexity: O(n * m), where n is the amount and m is the number of coins
# Space Complexity: O(n), where n is the amount

# Constraints:
#
# 1 <= coins.length <= 300
# 1 <= coins[i] <= 5000
# All the values of coins are unique.
# 0 <= amount <= 5000


if __name__ == "__main__":
    # Example 1:
    #
    # Input: amount = 5, coins = [1,2,5]
    # Output: 4
    amount = 5
    coins = [1, 2, 5]
    sol = Solution()
    print(sol.change(amount, coins))  # Output: 4
    # Explanation: there are four ways to make up the amount:
    # 5=5
    # 5=2+2+1
    # 5=2+1+1+1
    # 5=1+1+1+1+1

    # Example 2:
    #
    # Input: amount = 3, coins = [2]
    # Output: 0
    amount = 3
    coins = [2]
    print(sol.change(amount, coins))  # Output: 0
    # Explanation: the amount of 3 cannot be made up just with coins of 2.

    # Example 3:
    #
    # Input: amount = 10, coins = [10]
    # Output: 1
    amount = 10
    coins = [10]
    print(sol.change(amount, coins))  # Output: 1
