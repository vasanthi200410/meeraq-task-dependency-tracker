def dfs(node, graph, visited, stack, path):
    visited.add(node)
    stack.add(node)
    path.append(node)

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            cycle = dfs(neighbor, graph, visited, stack, path)
            if cycle:
                return cycle
        elif neighbor in stack:
            return path[path.index(neighbor):] + [neighbor]

    stack.remove(node)
    path.pop()
    return None


def check_circular_dependency(task_id, depends_on_id, existing_deps):
    graph = {}

    for t, d in existing_deps:
        graph.setdefault(t, []).append(d)

    graph.setdefault(task_id, []).append(depends_on_id)

    visited = set()
    stack = set()

    return dfs(task_id, graph, visited, stack, [])
