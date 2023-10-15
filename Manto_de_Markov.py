# Definir una matriz de transición de cadena de Markov
P = [[0.7, 0.3], [0.4, 0.6]]

# Calcular el manto de Markov
def markov_blanket(node_index, adjacency_matrix):
    num_nodes = len(adjacency_matrix)
    parents = [i for i in range(num_nodes) if adjacency_matrix[i][node_index] == 1]
    children = [i for i in range(num_nodes) if adjacency_matrix[node_index][i] == 1]
    siblings = []
    for child in children:
        for sibling in range(num_nodes):
            if adjacency_matrix[sibling][child] == 1:
                siblings.append(sibling)
    siblings = list(set(siblings) - {node_index})
    return parents, children, siblings

node_index = 1  # Índice del nodo en la cadena de Markov
parents, children, siblings = markov_blanket(node_index, P)

print("Padres:", parents)
print("Hijos:", children)
print("Hermanos:", siblings)
