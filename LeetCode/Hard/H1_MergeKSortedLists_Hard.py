# H1: Merge K Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/

# **********************************************************
# DESCRIPTION:
# **********************************************************

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
# Example 2:

# Input: lists = []
# Output: []
# Example 3:

# Input: lists = [[]]
# Output: []
 

# Constraints:

# k == lists.length
# 0 <= k <= 104
# 0 <= lists[i].length <= 500
# -104 <= lists[i][j] <= 10^4
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 10^4.


# **********************************************************
# PROVIDED CODE:
# **********************************************************

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pass


# **********************************************************
# CHATGPT ANSWER:
# **********************************************************

# GEN 1

import heapq
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        # Add the head of each linked list to the heap
        for i, lst in enumerate(lists):
            if lst is not None:
                heapq.heappush(heap, (lst.val, i, lst))
        
        dummy = ListNode()
        current = dummy
        
        while heap:
            val, i, node = heapq.heappop(heap)
            
            # Move to the next node in the selected linked list
            if node.next is not None:
                heapq.heappush(heap, (node.next.val, i, node.next))
            
            # Add the current node to the merged list
            current.next = node
            current = current.next
        
        return dummy.next

# Example usage:
# lists = [[1,4,5], [1,3,4], [2,6]]
# Convert lists to linked lists
linked_lists = [ListNode(val) for val in lists[0]]
for i in range(len(lists)-1):
    current = linked_lists[i]
    for val in lists[i+1]:
        current.next = ListNode(val)
        current = current.next

solution = Solution()
result = solution.mergeKLists(linked_lists)

# Print the result
while result is not None:
    print(result.val, end="->")
    result = result.next


# GEN 2

from typing import List, Optional
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Define a min heap to store (value, node) tuples
        heap = []

        # Push the first element from each linked list into the heap
        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(heap, (lst.val, i, lst))

        # Create a dummy node to simplify the code
        dummy = ListNode()
        current = dummy

        # Continue until the heap is not empty
        while heap:
            # Pop the smallest element from the heap
            val, i, node = heapq.heappop(heap)

            # Append the smallest element to the result list
            current.next = ListNode(val)
            current = current.next

            # Move to the next element in the linked list
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next


# GEN 3

import heapq
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Create a min heap to keep track of the smallest element among the heads
        heap = []

        # Push the first element of each list into the heap
        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(heap, (lst.val, i, lst))

        # Dummy node to simplify the code
        dummy = ListNode()
        current = dummy

        # Continue until the heap is not empty
        while heap:
            # Pop the smallest element from the heap
            val, i, node = heapq.heappop(heap)
            
            # Move the current pointer to the smallest element
            current.next = ListNode(val)
            current = current.next
            
            # Move to the next element in the list
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
