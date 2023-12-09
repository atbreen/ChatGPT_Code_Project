# H5: The Skyline Problem
# https://leetcode.com/problems/the-skyline-problem/

# **********************************************************
# DESCRIPTION
# **********************************************************

# A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. 
# Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.

# The geometric information of each building is given in the array buildings where buildings[i] = [lefti, righti, heighti]:

# lefti is the x coordinate of the left edge of the ith building.
# righti is the x coordinate of the right edge of the ith building.
# heighti is the height of the ith building.
# You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

# The skyline should be represented as a list of "key points" sorted by their x-coordinate in the form 
# [[x1,y1],[x2,y2],...]. 
# Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, 
# which always has a y-coordinate 0 and is used to mark the skyline's termination where the rightmost building ends. 
# Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.

# Note: There must be no consecutive horizontal lines of equal height in the output skyline. 
# For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is not acceptable; 
# the three lines of height 5 should be merged into one in the final output as such: 
# [...,[2 3],[4 5],[12 7],...]

 

# Example 1:


# Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
# Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
# Explanation:
# Figure A shows the buildings of the input.
# Figure B shows the skyline formed by those buildings. The red points in figure B represent the key points in the output list.
# Example 2:

# Input: buildings = [[0,2,3],[2,5,3]]
# Output: [[0,3],[5,0]]
 

# Constraints:

# 1 <= buildings.length <= 104
# 0 <= lefti < righti <= 231 - 1
# 1 <= heighti <= 231 - 1
# buildings is sorted by lefti in non-decreasing order.


# **********************************************************
# PROVIDED CODE:
# **********************************************************

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        pass


# **********************************************************
# CHATGPT ANSWER:
# **********************************************************


# **********************************************************

# GEN 1

import heapq
from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Create a list to store the result skyline
        result = []
        
        # Create a list to store the critical points (start and end points of the buildings)
        critical_points = []
        
        # Populate the critical points list with start and end points of the buildings
        for building in buildings:
            # For the start point, use a negative height to indicate the start
            critical_points.append((building[0], -building[2]))
            # For the end point, use the actual height to indicate the end
            critical_points.append((building[1], building[2]))
        
        # Sort the critical points based on x-coordinate (and y-coordinate in case of a tie)
        critical_points.sort()
        
        # Create a max heap to keep track of the current maximum height
        max_heap = [0]
        
        # Iterate through the critical points
        for point in critical_points:
            x, h = point
            
            # If the point is a start point, add the negative height to the max heap
            if h < 0:
                heapq.heappush(max_heap, h)
            else:
                # If the point is an end point, remove the corresponding start point height from the max heap
                max_heap.remove(-h)
                heapq.heapify(max_heap)
            
            # Get the current maximum height from the max heap
            current_max_height = -max_heap[0]
            
            # If the result is empty or the current height is different from the previous height, add it to the result
            if not result or current_max_height != result[-1][1]:
                result.append([x, current_max_height])
        
        return result


# **********************************************************


# **********************************************************

# GEN 2

from sortedcontainers import SortedDict
from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Initialize a list to store the result
        result = []
        # Initialize a sorted dictionary to keep track of heights at each x-coordinate
        # The key is the x-coordinate, and the value is the maximum height at that x-coordinate
        active_heights = SortedDict()
        # Initialize a variable to keep track of the current maximum height
        current_max_height = 0

        # Combine the left and right edges of each building and sort them
        # We use a negative height for the left edges and positive height for the right edges
        events = [(left, -height, right) for left, right, height in buildings]
        events += list(zip(*[iter(events)] * 2))  # Combine left and right edges
        events.sort()

        # Iterate through the events
        for x, neg_height, right in events:
            # Update the active heights based on the current event
            if neg_height < 0:  # Left edge of the building
                active_heights[-neg_height] = active_heights.get(-neg_height, 0) + 1
            else:  # Right edge of the building
                active_heights[neg_height] -= 1
                if active_heights[neg_height] == 0:
                    del active_heights[neg_height]

            # Get the current maximum height
            current_max_height = next(reversed(active_heights), 0)

            # If the maximum height has changed, update the result
            if not result or result[-1][1] != current_max_height:
                result.append([x, current_max_height])

        return result

# Debugging Response #1

from sortedcontainers import SortedDict
from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Initialize a list to store the result
        result = []
        # Initialize a sorted dictionary to keep track of heights at each x-coordinate
        # The key is the x-coordinate, and the value is the maximum height at that x-coordinate
        active_heights = SortedDict()
        # Initialize a variable to keep track of the current maximum height
        current_max_height = 0

        # Combine the left and right edges of each building and sort them
        # We use a negative height for the left edges and positive height for the right edges
        events = [(left, -height, right) for left, right, height in buildings]
        events += list(zip(*[iter(events)] * 2))  # Combine left and right edges
        events.sort(key=lambda x: (x[0], x[1]))

        # Iterate through the events
        for x, neg_height, right in events:
            # Update the active heights based on the current event
            if neg_height < 0:  # Left edge of the building
                active_heights[-neg_height] = active_heights.get(-neg_height, 0) + 1
            else:  # Right edge of the building
                active_heights[neg_height] -= 1
                if active_heights[neg_height] == 0:
                    del active_heights[neg_height]

            # Get the current maximum height
            current_max_height = next(reversed(active_heights), 0)

            # If the maximum height has changed, update the result
            if not result or result[-1][1] != current_max_height:
                result.append([x, current_max_height])

        return result


# Debugging Response #2

from sortedcontainers import SortedList
from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Initialize a list to store the result
        result = []
        # Initialize a sorted list to keep track of heights at each x-coordinate
        active_heights = SortedList([0])
        # Initialize a variable to keep track of the current maximum height
        current_max_height = 0

        # Combine the left and right edges of each building and sort them
        # We use a negative height for the left edges and positive height for the right edges
        events = [(left, -height, right) for left, right, height in buildings]
        events += list(zip(*[iter(events)] * 2))  # Combine left and right edges
        events.sort(key=lambda x: (x[0], x[1]))

        # Iterate through the events
        for x, neg_height, right in events:
            # Update the active heights based on the current event
            if neg_height < 0:  # Left edge of the building
                active_heights.add(-neg_height)
            else:  # Right edge of the building
                active_heights.remove(neg_height)

            # Get the current maximum height
            current_max_height = active_heights[-1]

            # If the maximum height has changed, update the result
            if not result or result[-1][1] != current_max_height:
                result.append([x, current_max_height])

        return result


# Debugging Response #3

from sortedcontainers import SortedList
from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Initialize a list to store the result
        result = []
        # Initialize a list to keep track of heights at each x-coordinate
        active_heights = SortedList([0])
        # Initialize a variable to keep track of the current maximum height
        current_max_height = 0

        # Combine the left and right edges of each building and sort them
        # We use a negative height for the left edges and positive height for the right edges
        events = [(left, -height, right) for left, right, height in buildings]
        events += list(zip(*[iter(events)] * 2))  # Combine left and right edges
        events.sort(key=lambda x: (x[0], x[1], x[2]))

        # Iterate through the events
        for x, neg_height, right in events:
            # Update the active heights based on the current event
            if neg_height < 0:  # Left edge of the building
                active_heights.add(-neg_height)
            else:  # Right edge of the building
                active_heights.remove(neg_height)

            # Get the current maximum height
            current_max_height = active_heights[-1]

            # If the maximum height has changed, update the result
            if not result or result[-1][1] != current_max_height:
                result.append([x, current_max_height])

        return result
    
# **********************************************************


# **********************************************************

# GEN 3

from heapq import heappush, heappop

class Solution:
    def getSkyline(self, buildings):
        events = []  # To store the events (start or end of a building)
        for left, right, height in buildings:
            # Use negative height for the start of a building to prioritize it over ends
            events.append((left, -height, right))
            events.append((right, 0, 0))  # Mark the end of the building

        events.sort()  # Sort the events based on x-coordinate

        result = []
        max_heap = [(0, float('inf'))]  # Max heap to keep track of current heights

        for x, h, r in events:
            # If it's the start of a building, add its height to the heap
            if h != 0:
                heappush(max_heap, (h, r))
            # If it's the end of a building, remove its height from the heap
            else:
                while max_heap[0][1] <= x:
                    heappop(max_heap)

            # Check if the current max height has changed
            if result and result[-1][1] != -max_heap[0][0]:
                result.append([x, -max_heap[0][0]])

        return result

# Example 1
buildings1 = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
sol = Solution()
output1 = sol.getSkyline(buildings1)
print(output1)
# Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]

# Example 2
buildings2 = [[0,2,3],[2,5,3]]
output2 = sol.getSkyline(buildings2)
print(output2)
# Output: [[0,3],[5,0]]


# Debugging #1

from heapq import heappush, heappop

class Solution:
    def getSkyline(self, buildings):
        events = []  # To store the events (start or end of a building)
        for left, right, height in buildings:
            # Use negative height for the start of a building to prioritize it over ends
            events.append((left, -height, right))
            events.append((right, 0, 0))  # Mark the end of the building

        events.sort()  # Sort the events based on x-coordinate

        result = []
        max_heap = [(0, float('inf'))]  # Max heap to keep track of current heights

        for x, h, r in events:
            # If it's the start of a building, add its height to the heap
            if h != 0:
                heappush(max_heap, (h, r))
            # If it's the end of a building, remove its height from the heap
            else:
                while max_heap[0][1] <= x:
                    heappop(max_heap)

            # Check if the current max height has changed
            if not result or result[-1][1] != -max_heap[0][0]:
                result.append([x, -max_heap[0][0]])

        return result
# **********************************************************