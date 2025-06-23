# Define the graph as an adjacency list with weighted edges
my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

def shortest_path(graph, start, target=''):
    # Initialize all nodes as unvisited
    unvisited = list(graph)

    # Distance from start node to others: 0 for start, infinity for others
    distances = {node: 0 if node == start else float('inf') for node in graph}

    # Store shortest path to each node
    paths = {node: [] for node in graph}
    paths[start].append(start)  # Start path with the starting node

    # Main loop: keep processing until all nodes have been visited
    while unvisited:
        # Choose the unvisited node with the smallest known distance
        current = min(unvisited, key=distances.get)

        # Explore all neighbors of the current node
        for node, distance in graph[current]:
            # If new path is shorter, update the distance and path
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]
                
                # Update the path based on whether the node's path already ends in itself
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]
                else:
                    paths[node].extend(paths[current])
                
                # Append the current neighbor node to the path
                paths[node].append(node)

        # Remove the current node from the list of unvisited
        unvisited.remove(current)

    # Determine which target(s) to show: one specific target or all
    targets_to_print = [target] if target else graph

    for node in targets_to_print:
        if node == start:
            continue
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')

    # Return final results
    return distances, paths

# Example usage
shortest_path(my_graph, 'A', 'F')
