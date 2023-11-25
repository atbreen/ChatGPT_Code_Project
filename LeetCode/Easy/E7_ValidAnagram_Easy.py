# E7: Valid Anagram
# https://leetcode.com/problems/valid-anagram/

# **********************************************************
# DESCRIPTION:
# **********************************************************

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
 

# Constraints:

# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.


# **********************************************************
# PROVIDED CODE:
# **********************************************************

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        pass

# **********************************************************
# CHATGPT ANSWER:
# **********************************************************

# GEN 1

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if the lengths of the strings are equal
        if len(s) != len(t):
            return False

        # Use dictionaries to store character frequencies
        char_count_s = {}
        char_count_t = {}

        # Count character frequencies in string s
        for char in s:
            char_count_s[char] = char_count_s.get(char, 0) + 1

        # Count character frequencies in string t
        for char in t:
            char_count_t[char] = char_count_t.get(char, 0) + 1

        # Compare the character frequencies
        return char_count_s == char_count_t

# Example usage:
solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))  # Output: True
print(solution.isAnagram("rat", "car"))          # Output: False


from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_count_s = defaultdict(int)
        char_count_t = defaultdict(int)

        for char in s:
            char_count_s[char] += 1

        for char in t:
            char_count_t[char] += 1

        return char_count_s == char_count_t


# GEN 2

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if the lengths of the two strings are equal
        if len(s) != len(t):
            return False

        # Create dictionaries to store the frequency of each character in both strings
        s_freq = {}
        t_freq = {}

        # Populate the frequency dictionary for string s
        for char in s:
            s_freq[char] = s_freq.get(char, 0) + 1

        # Populate the frequency dictionary for string t
        for char in t:
            t_freq[char] = t_freq.get(char, 0) + 1

        # Compare the frequency dictionaries
        return s_freq == t_freq

# Example usage:
solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))  # Output: True
print(solution.isAnagram("rat", "car"))          # Output: False


# GEN 3

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t, key=ord)
