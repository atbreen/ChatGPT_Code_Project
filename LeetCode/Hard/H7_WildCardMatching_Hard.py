# H7: Wild Card Matching
# https://leetcode.com/problems/wildcard-matching/

# **********************************************************
# DESCRIPTION:
# **********************************************************

# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).

 

# Example 1:

# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:

# Input: s = "aa", p = "*"
# Output: true
# Explanation: '*' matches any sequence.
# Example 3:

# Input: s = "cb", p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
 

# Constraints:

# 0 <= s.length, p.length <= 2000
# s contains only lowercase English letters.
# p contains only lowercase English letters, '?' or '*'.


# **********************************************************
# PROVIDED CODE:
# **********************************************************

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pass


# **********************************************************
# CHATGPT ANSWER:
# **********************************************************

# GEN 1

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Create a 2D DP table to store intermediate results
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        # Empty pattern matches empty string
        dp[0][0] = True

        # Handle patterns with '*' at the beginning
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

        # Fill the DP table
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

        # The result is stored at the bottom-right cell of the DP table
        return dp[len(s)][len(p)]

# Test cases
solution = Solution()
print(solution.isMatch("aa", "a"))      # Output: False
print(solution.isMatch("aa", "*"))      # Output: True
print(solution.isMatch("cb", "?a"))     # Output: False


# GEN 2

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Create a 2D DP array to store the matching results
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        # An empty pattern matches an empty string
        dp[0][0] = True
        
        # Handle patterns with '*' at the beginning
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
        
        # Fill the DP array
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                # If characters match or pattern has '?', take the diagonal value
                if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                # If pattern has '*', consider '*' as either empty or match the current character
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
        
        # The result is stored in the bottom-right cell
        return dp[len(s)][len(p)]

# Example usage:
sol = Solution()
print(sol.isMatch("aa", "a"))    # Output: False
print(sol.isMatch("aa", "*"))    # Output: True
print(sol.isMatch("cb", "?a"))   # Output: False


# GEN 3

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Create a 2D DP array to store intermediate results
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        # Empty pattern matches empty string
        dp[0][0] = True

        # Handle patterns with '*' at the beginning
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

        # Fill in the DP array
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

        return dp[len(s)][len(p)]

# Example usage:
solution = Solution()
print(solution.isMatch("aa", "a"))      # Output: False
print(solution.isMatch("aa", "*"))      # Output: True
print(solution.isMatch("cb", "?a"))     # Output: False
