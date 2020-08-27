class Node:

    _id = 1

    def __init__(self, node_type):
        self.id = Node._id
        self.node_type = node_type
        Node._id += 1
