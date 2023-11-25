# M2: Group Anagrams
# https://leetcode.com/problems/group-anagrams/


# **********************************************************
# DESCRIPTION:
# **********************************************************

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]
 

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.


# **********************************************************
# PROVIDED CODE:
# **********************************************************

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pass
        

# **********************************************************
# CHATGPT ANSWER:
# **********************************************************


# GEN 1

from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Use a defaultdict to store groups of anagrams
        anagram_groups = defaultdict(list)
        
        # Iterate through each word in the input list
        for word in strs:
            # Sort the characters in the word to use it as a key
            sorted_word = ''.join(sorted(word))
            
            # Add the word to the group of anagrams with the same sorted key
            anagram_groups[sorted_word].append(word)
        
        # Convert the values of the dictionary to a list to get the final result
        result = list(anagram_groups.values())
        
        return result

sol = Solution()

# Example 1
strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
output1 = sol.groupAnagrams(strs1)
print(output1)  # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

# Example 2
strs2 = [""]
output2 = sol.groupAnagrams(strs2)
print(output2)  # Output: [['']]

# Example 3
strs3 = ["a"]
output3 = sol.groupAnagrams(strs3)
print(output3)  # Output: [['a']]


# GEN 2

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a dictionary to store groups of anagrams
        anagram_groups = {}

        # Iterate through each word in the input list
        for word in strs:
            # Sort the characters in the word to get its signature
            sorted_word = ''.join(sorted(word))

            # Check if the signature is already in the dictionary
            if sorted_word in anagram_groups:
                # If yes, add the word to the corresponding group
                anagram_groups[sorted_word].append(word)
            else:
                # If no, create a new group with the current word
                anagram_groups[sorted_word] = [word]

        # Convert the values of the dictionary to a list to get the final result
        result = list(anagram_groups.values())

        return result

# Example usage:
solution = Solution()
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


# GEN 3

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a dictionary to store groups of anagrams
        anagram_groups = {}
        
        # Iterate through each word in the input list
        for word in strs:
            # Sort the letters of the word to use as a key for the dictionary
            sorted_word = ''.join(sorted(word))
            
            # Check if the sorted word is already a key in the dictionary
            # If yes, add the original word to the corresponding group
            # If no, create a new group with the sorted word as the key
            if sorted_word in anagram_groups:
                anagram_groups[sorted_word].append(word)
            else:
                anagram_groups[sorted_word] = [word]
        
        # Convert the values of the dictionary to a list to get the final result
        result = list(anagram_groups.values())
        
        return result

solution = Solution()

strs1 = ["eat","tea","tan","ate","nat","bat"]
output1 = solution.groupAnagrams(strs1)
print(output1)  # Output: [["eat","tea","ate"],["tan","nat"],["bat"]]

strs2 = [""]
output2 = solution.groupAnagrams(strs2)
print(output2)  # Output: [[""]]

strs3 = ["a"]
output3 = solution.groupAnagrams(strs3)
print(output3)  # Output: [["a"]]
