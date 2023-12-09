# E1: Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/

# **********************************************************
# DESCRIPTION:
# **********************************************************

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 
# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
 

# Constraints:

# 1 <= n <= 45


# **********************************************************
# PROVIDED CODE:
# **********************************************************
class Solution:
    def climbStairs(self, n: int) -> int:
        pass


# **********************************************************
# CHAT GPT ANSWER:
# **********************************************************

# GEN 1

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2

        # Initialize an array to store the number of ways to reach each step
        dp = [0] * n

        # Base cases
        dp[0] = 1
        dp[1] = 2

        # Build up to the top using dynamic programming
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[-1]

# Example usage:
sol = Solution()
print(sol.climbStairs(2))  # Output: 2
print(sol.climbStairs(3))  # Output: 3

# GEN 2

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        # Initialize an array to store the number of ways to climb for each step
        dp = [0] * (n + 1)

        # Base cases
        dp[1] = 1
        dp[2] = 2

        # Populate the array using dynamic programming
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

# Example usage:
solution = Solution()
print(solution.climbStairs(2))  # Output: 2
print(solution.climbStairs(3))  # Output: 3

# GEN 3

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        # Initialize a list to store the number of ways to reach each step
        dp = [0] * (n + 1)
        
        # Base cases
        dp[1] = 1
        dp[2] = 2

        # Build the list bottom-up
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

# Example usage:
solution = Solution()
print(solution.climbStairs(2))  # Output: 2
print(solution.climbStairs(3))  # Output: 3
