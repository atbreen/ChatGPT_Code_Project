# M1: Decode Ways
# https://leetcode.com/problems/decode-ways/


# **********************************************************
# DESCRIPTION:
# **********************************************************

# A message containing letters from A-Z can be encoded into numbers using the following mapping:

# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
# To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

# "AAJF" with the grouping (1 1 10 6)
# "KJF" with the grouping (11 10 6)
# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

# Given a string s containing only digits, return the number of ways to decode it.

# The test cases are generated so that the answer fits in a 32-bit integer.

 

# Example 1:

# Input: s = "12"
# Output: 2
# Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
# Example 2:

# Input: s = "226"
# Output: 3
# Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
# Example 3:

# Input: s = "06"
# Output: 0
# Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
 

# Constraints:

# 1 <= s.length <= 100
# s contains only digits and may contain leading zero(s).


# **********************************************************
# PROVIDED CODE:
# **********************************************************

class Solution:
    def numDecodings(self, s: str) -> int:
        pass


# **********************************************************
# CHATGPT ANSWER:
# **********************************************************

# GEN 2

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        
        # Handle edge case where the string is empty
        if n == 0:
            return 0

        # Initialize an array to store the number of ways to decode up to index i
        dp = [0] * (n + 1)

        # There is one way to decode an empty string
        dp[0] = 1

        # Check each character in the string
        for i in range(1, n + 1):
            # Check if the current character is not '0'
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]

            # Check if the current character and the previous one form a valid two-digit number
            if i > 1 and '10' <= s[i - 2:i] <= '26':
                dp[i] += dp[i - 2]

        return dp[n]


solution = Solution()
print(solution.numDecodings("12"))  # Output: 2
print(solution.numDecodings("226"))  # Output: 3
print(solution.numDecodings("06"))   # Output: 0


# GEN 2

class Solution:
    def numDecodings(self, s: str) -> int:
        # Check if the string is empty or starts with '0', return 0 in such cases
        if not s or s[0] == '0':
            return 0
        
        # Initialize an array to store the number of ways to decode at each position
        dp = [0] * (len(s) + 1)
        
        # There is one way to decode an empty string
        dp[0] = 1
        
        # There is one way to decode a string of length 1 if it's not '0'
        dp[1] = 1 if s[0] != '0' else 0
        
        # Iterate through the string to fill the dp array
        for i in range(2, len(dp)):
            # Check if the current digit is not '0', add the number of ways to decode
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            
            # Check if the current and previous digits form a valid mapping (between 10 and 26)
            two_digit = int(s[i-2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i-2]
        
        # The result is stored at the last position of the dp array
        return dp[-1]

# Example usage:
solution = Solution()
print(solution.numDecodings("12"))  # Output: 2
print(solution.numDecodings("226"))  # Output: 3
print(solution.numDecodings("06"))   # Output: 0


# GEN 3

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  # Empty string has one decoding (base case)

        for i in range(1, n + 1):
            # Single digit case
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]

            # Two-digit case
            if i > 1 and '10' <= s[i - 2:i] <= '26':
                dp[i] += dp[i - 2]

        return dp[n]

# Test cases
sol = Solution()
print(sol.numDecodings("12"))  # Output: 2
print(sol.numDecodings("226"))  # Output: 3
print(sol.numDecodings("06"))   # Output: 0
