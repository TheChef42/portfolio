from single_source_shortest_paths import initialize_single_source
from adjacency_list_graph import AdjacencyListGraph, Edge
from dll_sentinel import DLLSentinel
from dag_shortest_paths import dag_shortest_paths
import numpy as np
import random



N=int(input('input number of node in tangle: '))+1
#Nodes=input('input name of node in tangle: ')

Genesis = input("Input the genesis: ")

# Directed.
graph = AdjacencyListGraph(N)

walkOptions = []
tips = []
inputs = [1]

while True:
    connection = []
    inputs = (input('write the new nodes: ').split())
    if inputs[0] == "END":
        break
    for test in inputs:
        if ord(test)-96 > N:
            print(graph)
            exit("Idiot, your value is higher than allowed, you are stupid. Bye bye!")
    if len(list(graph.get_adj_list(0))) == 0:
        for currentNode in inputs:
            graph.insert_edge(0, ord(currentNode) - 96)
    else:
        for inputt in inputs:
            i = 0
            while True:
                if len(list(graph.get_adj_list(i))) == 0:
                    graph.insert_edge(i, ord(inputt) - 96)
                    break
                elif len(list(graph.get_adj_list(i))) < 4:
                    walkOptions.append(i+1)
                    for y in list(graph.get_adj_list(i)):
                        walkOptions.append(y)
                    k = int(str(random.choice(walkOptions)))-1
                    walkOptions = []
                    if i == k:
                        graph.insert_edge(i, ord(inputt) - 96)
                        break
                    else:
                        i = k
                else:
                    for y in list(graph.get_adj_list(i)):
                        walkOptions.append(y)
                    i = int(str(random.choice(walkOptions)))-1
                    walkOptions = []

print(graph)


Tips = []
for i in range(N-1):
    if len(list(graph.get_adj_list(i))) == 0:
        Tips.append(chr(i+97))

print("Tips:")
print(*Tips)

shortestpath = dag_shortest_paths(graph, 0)[0]

i = 0
for b in shortestpath:
    print(b)
    if b == float('inf'):
        shortestpath.pop(i)
    i += 1

print(shortestpath)

print(f"Tangle lenght: {max(shortestpath)+1}")