from graphviz import Digraph

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
    
    def __str__(self):
        current = self
        result = ""
        while current:
            result += str(current.value)
            if current.next:
                result += " -> "
            current = current.next
        return result
    


class Root:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self, level=0, prefix="Root: "):
        ret = "  " * level + prefix + str(self.val) + "\n"
        if self.left is not None:
            ret += self.left.__repr__(level + 1, "L--- ")
        if self.right is not None:
            ret += self.right.__repr__(level + 1, "R--- ")
        return ret
    
    @classmethod
    def insert_list(cls, values):
        if not values:
            return None
        
        root = cls(values[0])
        for value in values[1:]:
            cls._insert(root, value)
        
        return root

    @staticmethod
    def _insert(root, value):
        if value < root.val:
            if root.left is None:
                root.left = Root(value)
            else:
                Root._insert(root.left, value)
        elif value > root.val:
            if root.right is None:
                root.right = Root(value)
            else:
                Root._insert(root.right, value)

    def visualize_tree(self):
        def add_nodes_edges(dot, node):
            if node:
                dot.node(str(node.val))
                if node.left:
                    dot.edge(str(node.val), str(node.left.val))
                    add_nodes_edges(dot, node.left)
                if node.right:
                    dot.edge(str(node.val), str(node.right.val))
                    add_nodes_edges(dot, node.right)
        
        dot = Digraph(comment='Binary Tree Visualization')
        add_nodes_edges(dot, self)
        return dot

    def add_left(self, child_node):
        self.left = child_node

    def add_right(self, child_node):
        self.right = child_node
    
    def insert(self, val: int):
        if val < self.val:
            if self.left is None:
                self.add_left(Root(val))
            else:
                self.left.insert(val)
        elif val > self.val:
            if self.right is None:
                self.add_right(Root(val))
            else:
                self.right.insert(val)

    @classmethod
    def build_tree_from_list(cls, lst):
        def insert_level_order(arr, root, i, n):
            if i < n:
                if arr[i] is None:
                    return None
                temp = cls(arr[i])
                root = temp

                root.left = insert_level_order(arr, root.left, 2 * i + 1, n)
                root.right = insert_level_order(arr, root.right, 2 * i + 2, n)
            return root
        return insert_level_order(lst, None, 0, len(lst))