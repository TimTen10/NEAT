import genes.node as n
import genes.connection as c


class Genotype:

    def __init__(self, number_inputs, number_outputs):
        self.node_genes = []
        self.connection_genes = []
        # TODO: both lists have to always be sorted by id / innov number!

        self._fill_with_base_genes(number_inputs, number_outputs)

    def _fill_with_base_genes(self, number_in, number_out):
        # Create all input and output nodes
        in_nodes = [n.Node('Input') for i in range(number_in)]
        self.node_genes.extend(in_nodes)
        out_nodes = [n.Node('Output') for o in range(number_out)]
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
        # TODO: still have to check if a split is even possible
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

    # TODO: need a nice way to __repr__ a genotype
