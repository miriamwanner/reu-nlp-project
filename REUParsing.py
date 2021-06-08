import conllu
import networkx as nx
from conllu import parse_tree_incr
from tqdm import tqdm
from matplotlib import pyplot as plt

def load_sentences(file):
    with open(file, "r", encoding="utf-8") as data:
        sentences = parse_tree_incr(data)
        sentences = list(sentences)
    return sentences

def ud_2_graph(tree, parent=1, graph=None):
    if graph is None:
        graph = nx.Graph()
        graph.add_node(graph.number_of_nodes(), name='root')
        graph.add_node(graph.number_of_nodes(), name=tree.token['form'])
        graph.add_edge(0, parent, deprel='<root>')
    for child in tree.children:
        child_num = graph.number_of_nodes()
        graph.add_node(child_num, name=child.token['form'])
        graph.add_edge(parent, child_num, deprel=child.token['deprel'])
        graph = UD2Graph(child, child_num, graph)
    return graph

def draw_dep_tree(UDtree):
    g = ud_2_graph(mostcommon[0])
    pos = nx.spring_layout(g)
    nx.draw(g, pos)
    nx.draw_networkx_labels(g, pos, labels={node:g.nodes[node]['name'] for node in g.nodes})
    nx.draw_networkx_edge_labels(g, pos, edge_labels={edge:g.edges[edge]['deprel'] for edge in g.edges})
    plt.show()

def generate_hashes(UDtrees):
    hashes = {}
    mostcommon = []
    for sentence in tqdm(sentences):
        hash_ = nx.weisfeiler_lehman_graph_hash(UD2Graph(sentence),edge_attr='deprel')
        if hash_ not in hashes:
            hashes[hash_] = []
        hashes[hash_].append(sentence)
    return hashes

def diversity(UDtrees):
    hashes = generate_hashes(UDtrees)
    return len(hashes)/len(UDtrees)

def compare_langs(langfile1, langfile2):
    pass