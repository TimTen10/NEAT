# In this project I will implement NEAT (Neuroevolution of Augmenting Topologies) and use it to
# do Reinforcement Learning on ___.
# The original paper, this work is based on, can be found at: http://nn.cs.utexas.edu/downloads/papers/stanley.ec02.pdf

# A Genome (Genotype) consists of Node Genes and Connection Genes. Node Genes contain the Node ID / number and the type
# of the node (Input, Hidden or Output). Connection Genes contain the Node ID of the starting and ending Node of the
# connection, the weight, whether or not the connection is active in the current Genome and lastly the historic marking.
# The build Neural Network acts as the Phenotype.

# There are several types of mutation: Add Connection, Add Node and change weight.

# The Network will start as small as possible and will expand only through evolution.
from genes.connection import Connection
from genotype import Genotype


def main():
    g = Genotype(number_inputs=3, number_outputs=1)

    for gene in g.node_genes:
        print(gene)
    for gene in g.connection_genes:
        print(gene)

    g.split_connection(innov=7)
    print()

    for gene in g.node_genes:
        print(gene)
    for gene in g.connection_genes:
        print(gene)

    g.add_connection(in_node=1, out_node=5)
    print()

    for gene in g.node_genes:
        print(gene)
    for gene in g.connection_genes:
        print(gene)


if __name__ == '__main__':
    main()