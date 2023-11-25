# M3: Jump Game
# https://leetcode.com/problems/jump-game/

# **********************************************************
# DESCRIPTION:
# **********************************************************

# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

# Constraints:

# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 10^5


# **********************************************************
# PROVIDED CODE:
# **********************************************************

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pass

# **********************************************************
# CHATGPT ANSWER:
# **********************************************************
    
# GEN 1

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        n = len(nums)

        for i in range(n):
            # If the current index is greater than the maximum reachable index, return False
            if i > max_reach:
                return False

            # Update the maximum reachable index at each step
            max_reach = max(max_reach, i + nums[i])

            # If the maximum reachable index is greater than or equal to the last index, return True
            if max_reach >= n - 1:
                return True

        return False

sol = Solution()

print(sol.canJump([2,3,1,1,4]))  # Output: True
print(sol.canJump([3,2,1,0,4]))  # Output: False


# GEN 2

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Initialize the furthest position you can reach
        max_reach = 0

        # Iterate through the array
        for i in range(len(nums)):
            # If the current index is greater than the furthest position, return False
            if i > max_reach:
                return False

            # Update the furthest position you can reach
            max_reach = max(max_reach, i + nums[i])

            # If the furthest position exceeds or reaches the last index, return True
            if max_reach >= len(nums) - 1:
                return True

        # If the loop completes without returning, it means you can reach the end
        return True

# Example usage:
solution = Solution()
print(solution.canJump([2, 3, 1, 1, 4]))  # Output: True
print(solution.canJump([3, 2, 1, 0, 4]))  # Output: False


# GEN 3

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Initialize the furthest position to 0
        furthest = 0
        
        # Iterate through the array
        for i in range(len(nums)):
            # If the current index is beyond the furthest position, return False
            if i > furthest:
                return False
            
            # Update the furthest position you can reach
            furthest = max(furthest, i + nums[i])
            
            # If the furthest position is beyond or at the last index, return True
            if furthest >= len(nums) - 1:
                return True
        
        return False

# Example usage:
sol = Solution()
print(sol.canJump([2,3,1,1,4]))  # Output: True
print(sol.canJump([3,2,1,0,4]))  # Output: False
