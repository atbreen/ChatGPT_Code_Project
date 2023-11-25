# E6: Roman to Integer
# https://leetcode.com/problems/roman-to-integer/

# **********************************************************
# DESCRIPTION:
# **********************************************************

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

 

# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

# Constraints:

# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].


# **********************************************************
# PROVIDED CODE:
# **********************************************************

class Solution:
    def romanToInt(self, s: str) -> int:
        pass


# **********************************************************
# CHATGPT ANSWER:
# **********************************************************


# GEN 1

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0  # To keep track of the previous symbol's value
        
        for symbol in reversed(s):  # Iterate the string in reverse order
            value = roman_values[symbol]
            
            if value < prev_value:
                total -= value
            else:
                total += value
                
            prev_value = value  # Update the previous value for the next iteration
        
        return total


sol = Solution()
print(sol.romanToInt("III"))      # Output: 3
print(sol.romanToInt("LVIII"))    # Output: 58
print(sol.romanToInt("MCMXCIV"))  # Output: 1994


# GEN 2

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int_mapping = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        result = 0
        prev_value = 0
        
        for symbol in s:
            current_value = roman_to_int_mapping[symbol]
            
            # If the current value is greater than the previous, subtract the previous value
            if current_value > prev_value:
                result += current_value - 2 * prev_value
            else:
                result += current_value
            
            prev_value = current_value
        
        return result

# Test cases
solution = Solution()
print(solution.romanToInt("III"))  # Output: 3
print(solution.romanToInt("LVIII"))  # Output: 58
print(solution.romanToInt("MCMXCIV"))  # Output: 1994


# GEN 3

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prev_value = 0

        for char in s:
            value = roman_dict[char]

            if value > prev_value:
                # Subtraction case
                result += value - 2 * prev_value
            else:
                result += value

            prev_value = value

        return result


sol = Solution()
print(sol.romanToInt("III"))      # Output: 3
print(sol.romanToInt("LVIII"))    # Output: 58
print(sol.romanToInt("MCMXCIV"))  # Output: 1994
