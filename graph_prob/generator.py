import sys

from graph import Graph, Node

generate_graph = Graph.generate_graph


from random import random

args = sys.argv

# number of nodes
n = int(sys.argv[1])


# node probability
p = float(sys.argv[2])


def names(): 
    with open('names list.csv') as f:
        while True:
            boy, girl = f.readline().strip().split(',')

            yield boy
            yield girl

names = names()

values = range(0, n)


g = generate_graph(n, p, names, values)



    



