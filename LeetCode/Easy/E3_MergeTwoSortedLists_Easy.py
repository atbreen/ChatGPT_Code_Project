# E3: Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/

# **********************************************************
# DESCRIPTION:
# **********************************************************
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]
 

# Constraints:

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.


# **********************************************************
# PROVIDED CODE
# **********************************************************

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pass



# **********************************************************
# GHATGPT ANSWER:
# **********************************************************

# GEN 1

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to start the merged list
        dummy = ListNode()
        current = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # If one of the lists is not empty, append the remaining nodes
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        # The merged list starts from the next of the dummy node
        return dummy.next

# GEN 2

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to start the merged list
        dummy = ListNode()
        # Pointer to the current node in the merged list
        current = dummy

        # Iterate until one of the lists becomes empty
        while list1 is not None and list2 is not None:
            # Compare the values of the current nodes in both lists
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            # Move the pointer in the merged list
            current = current.next

        # If there are remaining nodes in list1, append them to the merged list
        if list1 is not None:
            current.next = list1
        # If there are remaining nodes in list2, append them to the merged list
        elif list2 is not None:
            current.next = list2

        # Return the head of the merged list (skip the dummy node)
        return dummy.next


# GEN 3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify code
        dummy = ListNode()
        current = dummy

        # Traverse both lists
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        # If one list is not empty, append the remaining nodes
        if list1 is not None:
            current.next = list1
        else:
            current.next = list2

        # Return the merged list starting from the next of the dummy node
        return dummy.next
