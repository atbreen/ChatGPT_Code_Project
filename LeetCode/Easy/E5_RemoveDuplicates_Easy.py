# E5: Remove Duplicates
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# **********************************************************
# DESCRIPTION:
# **********************************************************

# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. 
# The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.

 

# Example 1:

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -100 <= nums[i] <= 100
# nums is sorted in non-decreasing order.


# **********************************************************
# PROVIDED CODE
# **********************************************************

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
      pass


# **********************************************************
# CHATGPT ANSWER:
# **********************************************************


# GEN 1

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Initialize two pointers
        i = 0  # slow pointer
        for j in range(1, len(nums)):
            # If the current element is different from the previous one,
            # update the slow pointer and replace the element at slow pointer with the current element
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        # i is the index of the last unique element
        # the length of unique elements is i + 1
        return i + 1

# Example usage:
solution = Solution()
nums1 = [1, 1, 2]
result1 = solution.removeDuplicates(nums1)
print(result1, nums1[:result1])  # Output: 2 [1, 2]

nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
result2 = solution.removeDuplicates(nums2)
print(result2, nums2[:result2])  # Output: 5 [0, 1, 2, 3, 4]


# GEN 2

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Initialize pointers
        slow_ptr = 0
        
        # Iterate through the array with fast_ptr
        for fast_ptr in range(1, len(nums)):
            # If the current element is not equal to the previous one
            if nums[fast_ptr] != nums[slow_ptr]:
                # Move slow_ptr to the next position
                slow_ptr += 1
                # Update the value at slow_ptr with the unique element
                nums[slow_ptr] = nums[fast_ptr]
        
        # Return the number of unique elements (k)
        return slow_ptr + 1


# GEN 3

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Initialize two pointers
        i = 0
        
        # Iterate through the array
        for j in range(1, len(nums)):
            # If the current element is different from the previous one
            if nums[j] != nums[i]:
                # Move the pointer and update the value
                i += 1
                nums[i] = nums[j]
        
        # The unique elements are from index 0 to i (inclusive)
        # Return the count of unique elements
        return i + 1

# Example usage:
solution = Solution()

# Example 1
nums1 = [1, 1, 2]
k1 = solution.removeDuplicates(nums1)
print(f"Output: {k1}, nums = {nums1[:k1]}")

# Example 2
nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k2 = solution.removeDuplicates(nums2)
print(f"Output: {k2}, nums = {nums2[:k2]}")
