# H3: Serialize and Deserialize a Binary Tree
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# **********************************************************
# DESCRIPTION:
# **********************************************************

# Serialization is the process of converting a data structure or object into a sequence of bits so 
# that it can be stored in a file or memory buffer, or transmitted across a network connection link to be 
# reconstructed later in the same or another computer environment.
# Design an algorithm to serialize and deserialize a binary tree. 
# There is no restriction on how your serialization/deserialization algorithm should work. 
# You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

# Clarification: The input/output format is the same as how LeetCode serializes a binary tree. 
# You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

 
# Example 1:


# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]
# Example 2:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 10^4].
# -1000 <= Node.val <= 1000


# **********************************************************
# PROVIDED CODE:
# **********************************************************

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


# **********************************************************
# CHATGPT ANSWER:
# **********************************************************


# **********************************************************
# GEN 1

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def dfs(node):
            if not node:
                return 'null'
            return str(node.val) + ',' + dfs(node.left) + ',' + dfs(node.right)

        return dfs(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def build_tree(nodes):
            val = nodes.pop(0)
            if val == 'null':
                return None
            node = TreeNode(int(val))
            node.left = build_tree(nodes)
            node.right = build_tree(nodes)
            return node

        nodes = data.split(',')
        return build_tree(nodes)

# Example usage:
# ser = Codec()
# deser = Codec()
# root = deser.deserialize(ser.serialize(your_root_node))


# GEN 1 - Debugging Response #1

 # Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def dfs(node):
            if not node:
                return 'null'
            return str(node.val) + ',' + dfs(node.left) + ',' + dfs(node.right)

        return dfs(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def build_tree(nodes):
            val = nodes.pop(0)
            if val == 'null':
                return None
            node = TreeNode(int(val))
            node.left = build_tree(nodes)
            node.right = build_tree(nodes)
            return node

        nodes = data.split(',')
        return build_tree(nodes)

# Example usage:
# ser = Codec()
# deser = Codec()
# root = deser.deserialize(ser.serialize(your_root_node))



# GEN 1 - Debugging Response #2

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def dfs(node):
            if not node:
                return 'null'
            return str(node.val) + ',' + dfs(node.left) + ',' + dfs(node.right)

        return dfs(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def build_tree(nodes):
            val = nodes.pop(0)
            if val == 'null':
                return None
            node = TreeNode(int(val))
            node.left = build_tree(nodes)
            node.right = build_tree(nodes)
            return node

        nodes = data.split(',')
        return build_tree(nodes)

# Example usage:
# ser = Codec()
# deser = Codec()
# root = deser.deserialize(ser.serialize(your_root_node))


# GEN 1 - Debugging Response #3:

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def dfs(node):
            if not node:
                return 'null'
            return f'{node.val},{dfs(node.left)},{dfs(node.right)}'

        return '[' + dfs(root) + ']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def build_tree(nodes):
            val = nodes.pop(0)
            if val == 'null':
                return None
            node = TreeNode(int(val))
            node.left = build_tree(nodes)
            node.right = build_tree(nodes)
            return node

        data = data[1:-1]  # Remove '[' and ']'
        if not data:
            return None

        nodes = data.split(',')
        return build_tree(nodes)

# Example usage:
# ser = Codec()
# deser = Codec()
# root = deser.deserialize(ser.serialize(your_root_node))

# **********************************************************


# **********************************************************
# GEN 2

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def helper(node):
            if not node:
                return 'None,'
            return str(node.val) + ',' + helper(node.left) + helper(node.right)

        return helper(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def helper(values):
            if values[0] == 'None':
                values.pop(0)
                return None
            root = TreeNode(int(values[0]))
            values.pop(0)
            root.left = helper(values)
            root.right = helper(values)
            return root

        values = data.split(',')
        return helper(values[:-1])

# Example usage:
# Construct a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = None
root.left.right = None
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

# Instantiate Codec
ser = Codec()
deser = Codec()

# Serialize and Deserialize
serialized_tree = ser.serialize(root)
deserialized_tree = deser.deserialize(serialized_tree)

# Check if the deserialized tree is the same as the original tree
print(serialized_tree)  # Output: "1,2,None,None,3,4,None,None,5,None,None,"

# Debugging Response #1:

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def dfs(node):
            if not node:
                result.append("None")
                return
            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        result = []
        dfs(root)
        return ",".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def dfs():
            val = values.pop(0)
            if val == "None":
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        values = data.split(",")
        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


# Debugging Response #2:

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def dfs(node):
            if not node:
                result.append("None")
                return
            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        result = []
        dfs(root)
        return ",".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def dfs(values):
            val = values.pop(0)
            if val == "None":
                return None
            node = TreeNode(int(val))
            node.left = dfs(values)
            node.right = dfs(values)
            return node

        values = data.split(",")
        return dfs(values)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


# Debugging Response #3:

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def dfs(node):
            if not node:
                result.append("null")
                return
            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        result = []
        dfs(root)
        return ",".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def dfs(values):
            val = values.pop(0)
            if val == "null":
                return None
            node = TreeNode(int(val))
            node.left = dfs(values)
            node.right = dfs(values)
            return node

        values = data.split(",")
        return dfs(values)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# **********************************************************


# **********************************************************
# GEN 3

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def helper(node):
            if node is None:
                return "None,"
            return str(node.val) + "," + helper(node.left) + helper(node.right)
        
        return helper(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def helper(values):
            val = values.pop(0)
            if val == "None":
                return None
            node = TreeNode(int(val))
            node.left = helper(values)
            node.right = helper(values)
            return node
        
        values = data.split(",")
        return helper(values[:-1])  # The last element is an empty string

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


# Example usage:
# ser = Codec()
# deser = Codec()
# root = ...  # Initialize your binary tree
# serialized_tree = ser.serialize(root)
# deserialized_tree = deser.deserialize(serialized_tree)
# Now, deserialized_tree should be the same as the original tree.


# Debugging Response #1

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def helper(node):
            if node is None:
                return "None,"
            return str(node.val) + "," + helper(node.left) + helper(node.right)
        
        return helper(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def helper(values):
            val = values.pop(0)
            if val == "None":
                return None
            node = TreeNode(int(val))
            node.left = helper(values)
            node.right = helper(values)
            return node
        
        values = data.split(",")
        return helper(values[:-1])  # The last element is an empty string

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# **********************************************************






     

