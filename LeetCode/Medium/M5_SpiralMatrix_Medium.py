# M5: Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/

# **********************************************************
# DESCRIPTION:
# **********************************************************

# Given an m x n matrix, return all elements of the matrix in spiral order.

# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:


# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100


# **********************************************************
# PROVIDED CODE:
# **********************************************************

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        pass


# **********************************************************
# CHATGPT ANSWER:
# **********************************************************


# GEN 1

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        
        while matrix:
            # Append the first row
            result += matrix.pop(0)
            
            # Append the last column
            if matrix and matrix[0]:
                for row in matrix:
                    result.append(row.pop())
            
            # Append the last row in reverse order
            if matrix:
                result += matrix.pop()[::-1]
            
            # Append the first column in reverse order
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    result.append(row.pop(0))
        
        return result

# Example usage:
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
solution = Solution()
output1 = solution.spiralOrder(matrix1)
print(output1)  # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
output2 = solution.spiralOrder(matrix2)
print(output2)  # Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]



# GEN 2

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        
        while matrix:
            result += matrix.pop(0)  # Add top row
            
            if matrix and matrix[0]:  
                for row in matrix:
                    result.append(row.pop())  # Add rightmost column
            
            if matrix:
                result += matrix.pop()[::-1]  # Add bottom row
            
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    result.append(row.pop(0))  # Add leftmost column
        
        return result

# Example usage:
matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
solution1 = Solution()
output1 = solution1.spiralOrder(matrix1)
print(output1)  # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

matrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
solution2 = Solution()
output2 = solution2.spiralOrder(matrix2)
print(output2)  # Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]


# GEN 3

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        while matrix:
            result += matrix.pop(0)

            if matrix and matrix[0]:
                for row in matrix:
                    result.append(row.pop())

            if matrix:
                result += matrix.pop()[::-1]

            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    result.append(row.pop(0))

        return result

# Example usage:
solution = Solution()
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(solution.spiralOrder(matrix1))  # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(solution.spiralOrder(matrix2))  # Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
