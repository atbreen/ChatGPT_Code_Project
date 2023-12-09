# E2: FizzBuzz
# https://leetcode.com/problems/fizz-buzz/

# **********************************************************
# DESCRIPTION:
# **********************************************************

# Given an integer n, return a string array answer (1-indexed) where:

# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.
 

# Example 1:

# Input: n = 3
# Output: ["1","2","Fizz"]
# Example 2:

# Input: n = 5
# Output: ["1","2","Fizz","4","Buzz"]
# Example 3:

# Input: n = 15
# Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
 

# Constraints:

# 1 <= n <= 10^4


# **********************************************************
# PROVIDED CODE:
# **********************************************************

# class Solution:
#     def fizzBuzz(self, n: int) -> List[str]:
#         pass


# **********************************************************
# CHATGPT ANSWER:
# **********************************************************

# GEN 1

from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        
        return result

# Example usage:
solution = Solution()
print(solution.fizzBuzz(3))  # Output: ["1", "2", "Fizz"]
print(solution.fizzBuzz(5))  # Output: ["1", "2", "Fizz", "4", "Buzz"]
print(solution.fizzBuzz(15)) # Output: ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]

# GEN 2

from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result

# Example usage:
solution = Solution()
print(solution.fizzBuzz(3))  # Output: ["1", "2", "Fizz"]
print(solution.fizzBuzz(5))  # Output: ["1", "2", "Fizz", "4", "Buzz"]
print(solution.fizzBuzz(15))  # Output: ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]


# GEN 3

from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
                
        return result

# Example usage:
solution = Solution()
print(solution.fizzBuzz(3))  # Output: ["1", "2", "Fizz"]
print(solution.fizzBuzz(5))  # Output: ["1", "2", "Fizz", "4", "Buzz"]
print(solution.fizzBuzz(15))  # Output: ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
