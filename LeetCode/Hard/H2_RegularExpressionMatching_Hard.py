# H2: Regular Expression Matching
# https://leetcode.com/problems/regular-expression-matching/

# **********************************************************
# DESCRIPTION:
# **********************************************************

# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

 

# Example 1:

# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:

# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
# Example 3:

# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
 

# Constraints:

# 1 <= s.length <= 20
# 1 <= p.length <= 20
# s contains only lowercase English letters.
# p contains only lowercase English letters, '.', and '*'.
# It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.


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
        m, n = len(s), len(p)
        
        # Initialize a 2D DP table
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # An empty pattern matches an empty string
        dp[0][0] = True
        
        # Fill in the first row (empty string)
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        # Fill in the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] if s[i - 1] == p[j - 2] or p[j - 2] == '.' else False)
        
        return dp[m][n]

# Test cases
solution = Solution()
print(solution.isMatch("aa", "a"))    # Output: False
print(solution.isMatch("aa", "a*"))   # Output: True
print(solution.isMatch("ab", ".*"))   # Output: True


# GEN 2

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Create a 2D DP array to store intermediate results
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        # Empty pattern matches empty string
        dp[0][0] = True
        
        # Handle patterns with '*'
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        # Dynamic programming to fill the DP array
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] if s[i - 1] == p[j - 2] or p[j - 2] == '.' else False)
        
        return dp[len(s)][len(p)]

# Test cases
solution = Solution()
print(solution.isMatch("aa", "a"))      # Output: False
print(solution.isMatch("aa", "a*"))     # Output: True
print(solution.isMatch("ab", ".*"))     # Output: True


# GEN 3

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Create a 2D DP table to store the matching results
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        # Empty pattern matches empty string
        dp[0][0] = True

        # Handle patterns with '*' at the beginning
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        # Fill the DP table
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] if s[i - 1] == p[j - 2] or p[j - 2] == '.' else False)

        return dp[len(s)][len(p)]

# Test cases
solution = Solution()
print(solution.isMatch("aa", "a"))  # Output: False
print(solution.isMatch("aa", "a*"))  # Output: True
print(solution.isMatch("ab", ".*"))  # Output: True
