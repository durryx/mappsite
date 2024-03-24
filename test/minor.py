"""from treelib import Node, Tree

tree = Tree()

tree.create_node("1", "1")
tree.create_node("2", "2", parent="1")
tree.create_node("2", "2", parent="1")
tree.show()
"""

from queue import Queue

events_queue = Queue()

events_queue.put("a")
events_queue.put("a")
events_queue.put("a")
events_queue.put("a")
events_queue.put("a")

elems = [events_queue.get() for _ in range(events_queue.qsize())]


print(elems)
print(events_queue.get())
print(events_queue.get())
print(events_queue.get())
