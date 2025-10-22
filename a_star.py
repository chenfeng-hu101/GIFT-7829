from heapq import heappush, heappop
from node import Node
import math

def a_star(start, end):
    open_set = []
    heappush(open_set, (0, start))

    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}
    visited = set()
    visit_history = []

    while open_set:
        _, current = heappop(open_set)
        if current in visited:
            continue
        visited.add(current)
        visit_history.append(current)

        if current == end:
            return reconstruct_path(came_from, current), visit_history

        for neighbor in current.get_neighbors():
            if neighbor.type == "wall":
                continue

            tentative_g = g_score[current] + distance(current, neighbor)
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(neighbor, end)
                heappush(open_set, (f_score[neighbor], neighbor))  # ✅ 正确调用

    return None, visit_history


def distance(n1, n2):
    return 1

def heuristic(node1, node2):
    # 曼哈顿距离
    return abs(node1.x - node2.x) + abs(node1.y - node2.y)

def reconstruct_path(came_from, current):
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path
