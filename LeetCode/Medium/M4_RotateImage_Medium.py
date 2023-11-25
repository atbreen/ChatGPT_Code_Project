# M4: Rotate Image
# https://leetcode.com/problems/rotate-image/


# **********************************************************
# DESCRIPTION:
# **********************************************************

# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
# DO NOT allocate another 2D matrix and do the rotation.


# Example 1:

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
# Example 2:


# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 

# Constraints:

# n == matrix.length == matrix[i].length
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000


# **********************************************************
# PROVIDED CODE:
# **********************************************************

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        pass

# **********************************************************
# CHATGPT ANSWER:
# **********************************************************

# GEN 1:

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # Transpose the matrix
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse each row
        for i in range(n):
            matrix[i].reverse()

# Example usage:
solution = Solution()
matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
solution.rotate(matrix1)
print(matrix1)  # Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

matrix2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
solution.rotate(matrix2)
print(matrix2)  # Output: [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]


# GEN 2

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # Step 1: Transpose the matrix
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for i in range(n):
            matrix[i].reverse()

# Example usage:
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
solution = Solution()
solution.rotate(matrix1)
print(matrix1)

matrix2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
solution.rotate(matrix2)
print(matrix2)


# GEN 3

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        # Transpose the matrix
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse each row
        for i in range(n):
            matrix[i].reverse()

# Example usage:
solution = Solution()

matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
solution.rotate(matrix1)
print(matrix1)
# Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

matrix2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
solution.rotate(matrix2)
print(matrix2)
# Output: [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
