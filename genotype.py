class Genotype:

    def __init__(self):
        self.node_genes = []
        self.connection_genes = []

    def add_node(self, node):
        self.node_genes.append(node)

    def add_connection(self, connection):
        self.connection_genes.append(connection)
