import random


class Connection:

    _id = 1

    def __init__(self, in_node, out_node, weight=random.uniform(-1, 1), is_enabled=1):
        # TODO: in_node and out_node always ids!
        self.in_node = in_node
        self.out_node = out_node
        self.weight = weight
        self.is_enabled = is_enabled
        self.innov = Connection._id
        Connection._id += 1

    def switch(self):
        # Swap from 1 to 0 (from enabled to disabled)
        self.is_enabled = 0 if self.is_enabled else 1
        return self.is_enabled

    def __repr__(self):
        return f'in: {self.in_node}, out: {self.out_node}, weight: {self.weight}, ' \
               f'is_enabled: {self.is_enabled}, innov: {self.innov}'
