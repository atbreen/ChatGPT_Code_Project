
# M6: Unique Paths
# https://leetcode.com/problems/unique-paths/


# **********************************************************
# DESCRIPTION:
# **********************************************************

# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

# Example 1:


# Input: m = 3, n = 7
# Output: 28
# Example 2:

# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
 

# Constraints:

# 1 <= m, n <= 100


# **********************************************************
# PROVIDED CODE:
# **********************************************************

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        pass

# **********************************************************
# CHATGPT ANSWER:
# **********************************************************


# GEN 1

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create a 2D array to store the number of unique paths
        dp = [[0] * n for _ in range(m)]

        # Initialize the top row and left column to 1, as there is only one way to reach any cell in the top row or left column
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        # Fill the rest of the grid using dynamic programming
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # The value at the bottom-right corner represents the number of unique paths
        return dp[m - 1][n - 1]

# Test cases
sol = Solution()
print(sol.uniquePaths(3, 7))  # Output: 28
print(sol.uniquePaths(3, 2))  # Output: 3


# GEN 2

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create a 2D array to store the number of unique paths
        dp = [[0] * n for _ in range(m)]

        # Initialize the top row and left column to 1 since there is only one way to reach any cell in those
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        # Fill in the rest of the array by summing the paths from the top and the left
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # The result is stored in the bottom-right cell
        return dp[m - 1][n - 1]

# Example usage:
solution = Solution()
print(solution.uniquePaths(3, 7))  # Output: 28
print(solution.uniquePaths(3, 2))  # Output: 3


# GEN 3

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create a 2D array to store the number of unique paths
        dp = [[1] * n for _ in range(m)]

        # Fill the dp array
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # The result is stored in the bottom-right cell
        return dp[m - 1][n - 1]

# Test cases
sol = Solution()
print(sol.uniquePaths(3, 7))  # Output: 28
print(sol.uniquePaths(3, 2))  # Output: 3
