# Define the graph as a dictionary where each node is a key, and its value is a list of tuples.
# Each tuple represents a connection to another node and the distance to that node.
""" my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
} """

my_graph = {
    'A': [('B', 3), ('D', 1)],
    'B': [('A', 3), ('C', 4)],
    'C': [('B', 4), ('D', 7)],
    'D': [('A', 1), ('C', 7)]
}

# Function to find the shortest path from a start node to all other nodes in the graph,
# or to a specific target node if one is provided.
def shortest_path(graph, start, target=''):
    # Initialize a list of unvisited nodes from the graph.
    unvisited = list(graph) # returns ['A', 'B', 'C', 'D']
    
    # Initialize distances from the start node to all other nodes as infinity, except the start node itself which is 0.
    distances = {node: 0 if node == start else float('inf') for node in graph}
    
    # Initialize paths to store the shortest path found to each node, starting only with the start node for itself.
    paths = {node: [] for node in graph}
    paths[start].append(start)
    
    # Loop until there are no unvisited nodes left.
    while unvisited:
        # Select the unvisited node with the smallest distance from the start node.
        current = min(unvisited, key=distances.get)
       
        # Explore each neighbor of the current node.
        for node, distance in graph[current]:
            # If a shorter path to the neighbor is found, update the neighbor's distance and path.
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]
                
                # Update the path for the neighbor. Copy the path from the current node if necessary.
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]
                else:
                    paths[node].extend(paths[current])
                paths[node].append(node)
        
        # Mark the current node as visited by removing it from the unvisited list.
        unvisited.remove(current)
    
    # Determine which nodes' distances and paths to print based on whether a target was specified.
    targets_to_print = [target] if target else graph
    print(targets_to_print)
    for node in targets_to_print:
        if node == start:
            continue
        
        # Print the distance and path from the start node to the current node.
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')
    
    # Return the distances dictionary for all nodes from the start node.
    return distances, paths

# Example usage: find the shortest path from node 'A' to node 'F' in the graph.
shortest_path(my_graph, 'A') #, 'F')
