from graph import *
from shortest_path import *

def graph_generate(dict, n):
    answer = []
    for key in dict.keys():
        for k, v in dict.items():
            if dict[key][-n:] == v[:n] and dict[key] != dict[k]:
                answer.append((key, k))
    return answer

def read_fasta(filename_as_string):
    """
    open text file with FASTA format
    read it and convert it into string list
    convert the list to dictionary
    >>> read_fasta('sample.txt')
        {'Rosalind_0000':'GTAT....ATGA', ... }
    """
    f = open(filename_as_string, 'r')
    content = [line.strip() for line in f]
    f.close()

    new_content = []
    for line in content:
        if '>Rosalind' in line:
            new_content.append(line.strip('>'))
            new_content.append('')
        else:
            new_content[-1] += line

    dict = {}
    for i in range(len(new_content)-1):
        if i % 2 == 0:
            dict[new_content[i]] = new_content[i+1]

    return dict


graph = AdjacencySetGraph(8, directed=False)

fasta = read_fasta('data/overlap_graph.txt')
for tup in graph_generate(fasta, 3):
    if tup[0] != tup[1]:
        graph.add_edge(Node(tup[0]), Node(tup[1]))


graph.add_edge(Node("1"), Node("2"))
graph.add_edge(Node("1"), Node("3"))
graph.add_edge(Node("3"), Node("4"))
graph.display()

shortest_path(graph, Node("Rosalind_5028"), Node("Rosalind_3843"))
