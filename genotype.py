import genes.node as n
import genes.connection as c
import random


class Genotype:

    def __init__(self, number_inputs=None, number_outputs=None, node_genes=None, connection_genes=None):
        if node_genes:
            self.node_genes = node_genes
        else:
            self.node_genes = []

        if connection_genes:
            self.connection_genes = connection_genes
        else:
            self.connection_genes = []

        self.fitness = 0

        # TODO: both lists have to always be sorted by id / innov number!

        # If both needed parameters exist:
        if number_inputs and number_outputs:
            self._fill_with_base_genes(number_inputs, number_outputs)

    def _fill_with_base_genes(self, number_in, number_out):
        # Create all input and output nodes
        in_nodes = [n.Node('Input') for _ in range(number_in)]
        self.node_genes.extend(in_nodes)
        out_nodes = [n.Node('Output') for _ in range(number_out)]
        self.node_genes.extend(out_nodes)

        # Create all connection between input and output nodes
        self.connection_genes.extend(
            c.Connection(in_node.id, out_node.id) for in_node in in_nodes for out_node in out_nodes
        )

    def add_connection(self, in_node, out_node):
        self.connection_genes.append(c.Connection(in_node, out_node))

    def split_connection(self, innov):
        # Disable the old connection (it has to be enabled at first so a node can be added into it)
        disabled_connection = next(conn for conn in self.connection_genes if conn.innov == innov)
        disabled_connection.switch()

        # Create a new node that goes in between the two new connections
        new_node = n.Node('Hidden')
        self.node_genes.append(new_node)

        # Create two new connections, one that goes into the new node (weight = 1) and one that goes out of the new
        # node (weight = weight of old/disabled connection). The new "in" connection gets created first
        self.connection_genes.append(
            c.Connection(disabled_connection.in_node, new_node.id, weight=1)
        )
        self.connection_genes.append(
            c.Connection(new_node.id, disabled_connection.out_node, weight=disabled_connection.weight)
        )

    def _build_function(self):
        def network_function(input_value):
            pass
        return network_function

    def evaluate(self, input_value):
        pass

    def evolve(self):
        pass

    def crossover(self, mate):
        # Returns the new genotype
        # import random has its usage here
        pass

    # TODO: need a nice way to __repr__ a genotype
