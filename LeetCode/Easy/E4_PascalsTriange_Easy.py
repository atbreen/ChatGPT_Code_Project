# E4: Pascal's Triangle
# https://leetcode.com/problems/pascals-triangle/

# **********************************************************
# DESCRIPTION:
# **********************************************************

# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:

# Input: numRows = 1
# Output: [[1]]
 

# Constraints:

# 1 <= numRows <= 30


# **********************************************************
# PROVIDED CODE:
# **********************************************************

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pass


# **********************************************************
# CHATGPT ANSWER:
# **********************************************************


# GEN 1

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Initialize the result list with the first row
        result = [[1] * (i + 1) for i in range(numRows)]
        
        # Calculate the values for each row starting from the third row
        for i in range(2, numRows):
            for j in range(1, i):
                result[i][j] = result[i-1][j-1] + result[i-1][j]
        
        return result

# Example usage:
solution = Solution()
print(solution.generate(5))


# GEN 2

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        triangle = [[1]]  # Initialize with the first row
        
        for i in range(1, numRows):
            # Generate the current row by adding the two numbers above it
            row = [1] + [triangle[i-1][j-1] + triangle[i-1][j] for j in range(1, i)] + [1]
            triangle.append(row)
        
        return triangle

# Example usage:
solution = Solution()
print(solution.generate(5))
print(solution.generate(1))



# GEN 3

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        # Initialize the result with the first row
        result = [[1]]
        
        for i in range(1, numRows):
            # Calculate the next row based on the previous row
            row = [1]
            for j in range(1, i):
                row.append(result[i-1][j-1] + result[i-1][j])
            row.append(1)
            
            # Add the current row to the result
            result.append(row)
        
        return result

# Example usage:
solution = Solution()
print(solution.generate(5))
# Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

print(solution.generate(1))
# Output: [[1]]
