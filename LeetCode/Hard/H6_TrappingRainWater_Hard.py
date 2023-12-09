# H6: Trapping Rainwater
# https://leetcode.com/problems/trapping-rain-water/

# **********************************************************
# DESCRIPTION:
# **********************************************************

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

# Example 1:


# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9
 

# Constraints:

# n == height.length
# 1 <= n <= 2 * 10^4
# 0 <= height[i] <= 10^5

# **********************************************************
# PROVIDED CODE:
# **********************************************************
class Solution:
    def trap(self, height: List[int]) -> int:
        pass

# **********************************************************
# CHATGPT ANSWER:
# **********************************************************

# GEN 1

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        if n <= 2:
            return 0
        
        left, right = 0, n - 1
        left_max, right_max = height[left], height[right]
        trapped_water = 0
        
        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                trapped_water += max(0, left_max - height[left])
                left += 1
            else:
                right_max = max(right_max, height[right])
                trapped_water += max(0, right_max - height[right])
                right -= 1
        
        return trapped_water

# Example usage:
solution = Solution()
print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # Output: 6
print(solution.trap([4,2,0,3,2,5]))              # Output: 9



# GEN 2

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)
        left, right = 0, n - 1
        left_max, right_max = 0, 0
        result = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    result += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    result += right_max - height[right]
                right -= 1

        return result

# Example usage:
solution = Solution()
print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # Output: 6
print(solution.trap([4,2,0,3,2,5]))  # Output: 9


# GEN 3

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2:
            return 0

        left_max = [0] * n
        right_max = [0] * n

        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        trapped_water = 0
        for i in range(n):
            trapped_water += min(left_max[i], right_max[i]) - height[i]

        return trapped_water

# Example usage:
height1 = [0,1,0,2,1,0,1,3,2,1,2,1]
solution1 = Solution()
print(solution1.trap(height1))  # Output: 6

height2 = [4,2,0,3,2,5]
solution2 = Solution()
print(solution2.trap(height2))  # Output: 9


