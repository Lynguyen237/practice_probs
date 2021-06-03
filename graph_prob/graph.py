from random import random

from itertools import islice


class Node:
    def __init__(self, display_name, value = 0):
        self.display_name = display_name
        self.value = value

        self.neighbors = []

    def __repr__(self):
         return f"<{self.display_name}:{self.value}>"


class Graph:
    def __init__(self, nodes=None):
        self.nodes = nodes if nodes else []

    def __getitem__(self, idx):
        return self.nodes[idx]

    @staticmethod
    def generate_graph(n, p, names, values):
        nodes = list(islice((Node(n, v) for (n, v) in zip(names, values)), n))

        for node1 in nodes:
            for node2 in nodes:
                if (node1 != node2 and p > random()):
                    node1.neighbors.append(node2)

        return Graph(nodes)


    def find_best(self, start_node):
        """ Return the largest data value accessable from the start_node"""
        # import pdb

        # pdb.set_trace()

        seen = set()

        def compare_values(cur_node):

            max_val = cur_node.value
            
            if cur_node in seen:
                return -1

            seen.add(cur_node)

            for neighbor in cur_node.neighbors:
                max_val = max(max_val, compare_values(neighbor))
            
            return max_val

        return compare_values(start_node)


    def find_best2(self, start_node):

        best = start_node.value

        nodes_to_visit = [start_node]

        visited = set()

        while nodes_to_visit:

            current_node = nodes_to_visit.pop()
    
            if current_node in visited:
                continue

            visited.add(current_node)
            nodes_to_visit.extend(current_node.neighbors)

            best = max(best, current_node.value)

        return best

'''
INSTRUCTIONS
2 ways to generate a graph with 10 nodes and .2 probability of being connected
    -> python3 -i generator.py 10 .2
    >>> g = generate_graph(10, .2, names, range(10))

Then test
    >>> g.find_best(g[1])
    >>> g.find_best2(g[1]) 
'''