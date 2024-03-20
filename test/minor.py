from treelib import Node, Tree

tree = Tree()

tree.create_node("1", "1")
tree.create_node("2", "2", parent="1")
tree.create_node("2", "2", parent="1")
tree.show()