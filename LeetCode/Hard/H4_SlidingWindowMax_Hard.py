# H4: Sliding Window Maximum
# https://leetcode.com/problems/sliding-window-maximum/

# **********************************************************
# DESCRIPTION:
# **********************************************************

# You are given an array of integers nums, there is a sliding window of size k which is moving from 
# the very left of the array to the very right. You can only see the k numbers in the window. 
# Each time the sliding window moves right by one position.

# Return the max sliding window.

 
# Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# 1 <= k <= nums.length


# **********************************************************
# PROVIDED CODE:
# **********************************************************

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pass


# **********************************************************
# CHATGPT ANSWER:
# **********************************************************


# GEN 1

from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        max_queue = deque()

        for i in range(len(nums)):
            # Remove elements outside the current window
            while max_queue and max_queue[0] < i - k + 1:
                max_queue.popleft()

            # Remove elements smaller than the current element
            while max_queue and nums[max_queue[-1]] < nums[i]:
                max_queue.pop()

            # Add the current index to the deque
            max_queue.append(i)

            # Add the maximum element to the result when the window is fully formed
            if i >= k - 1:
                result.append(nums[max_queue[0]])

        return result

# Example usage:
nums1 = [1, 3, -1, -3, 5, 3, 6, 7]
k1 = 3
solution = Solution()
output1 = solution.maxSlidingWindow(nums1, k1)
print(output1)  # Output: [3, 3, 5, 5, 6, 7]

nums2 = [1]
k2 = 1
output2 = solution.maxSlidingWindow(nums2, k2)
print(output2)  # Output: [1]


# GEN 2

from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        result = []
        window = deque()

        # Helper function to update the window by removing elements that are out of the current window
        def update_window(i):
            if window and window[0] < i - k + 1:
                window.popleft()

            while window and nums[i] > nums[window[-1]]:
                window.pop()

        for i in range(len(nums)):
            update_window(i)
            window.append(i)

            if i >= k - 1:
                result.append(nums[window[0]])

        return result

solution = Solution()
nums1 = [1, 3, -1, -3, 5, 3, 6, 7]
k1 = 3
output1 = solution.maxSlidingWindow(nums1, k1)
print(output1)  # Output: [3, 3, 5, 5, 6, 7]

nums2 = [1]
k2 = 1
output2 = solution.maxSlidingWindow(nums2, k2)
print(output2)  # Output: [1]


# GEN 3

from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        window = deque()

        for i in range(len(nums)):
            # Remove elements outside the current window from the front of the deque
            while window and window[0] < i - k + 1:
                window.popleft()

            # Remove elements smaller than the current element from the back of the deque
            while window and nums[i] > nums[window[-1]]:
                window.pop()

            # Add the current index to the deque
            window.append(i)

            # Add the maximum element in the current window to the result
            if i >= k - 1:
                result.append(nums[window[0]])

        return result

# Example usage:
nums1 = [1, 3, -1, -3, 5, 3, 6, 7]
k1 = 3
solution = Solution()
output1 = solution.maxSlidingWindow(nums1, k1)
print(output1)  # Output: [3, 3, 5, 5, 6, 7]

nums2 = [1]
k2 = 1
output2 = solution.maxSlidingWindow(nums2, k2)
print(output2)  # Output: [1]

