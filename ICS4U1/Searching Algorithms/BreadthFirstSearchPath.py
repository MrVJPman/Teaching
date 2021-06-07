# sample graph implemented as a dictionary
graph = {'A': 'BCE',
         'B': 'ADE',
         'C': 'AFG',
         'D': 'B',
         'E': 'ABD',
         'F': 'C',
         'G': 'C'}

def bfs_shortest_path(graph, start, goal):
    visited_nodes = []
    queue_of_possible_paths_to_check = [[start]]
    loop_num = 1
    while queue_of_possible_paths_to_check:
        path_to_check = queue_of_possible_paths_to_check.pop(0)
        print("path_to_check", path_to_check)
        print(loop_num, queue_of_possible_paths_to_check)
        last_node_of_path_to_check = path_to_check[-1]
        if last_node_of_path_to_check not in visited_nodes:
            neighbours_of_last_node_of_path_to_check = graph[last_node_of_path_to_check]
            for neighbour in neighbours_of_last_node_of_path_to_check:
                new_path = list(path_to_check) + [neighbour]
                queue_of_possible_paths_to_check.append(new_path)
                if neighbour == goal:
                    return new_path
            visited_nodes.append(last_node_of_path_to_check)
        loop_num += 1
print(bfs_shortest_path(graph, 'G', 'D'))  # returns ['G', 'C', 'A', 'B', 'D']