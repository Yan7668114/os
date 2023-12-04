import heapq

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.g = 0  # 此節點到起點的實際成本
        self.h = 0  # 启发式估計到目標點的成本
        self.f = 0  # 總估計成本（g + h）
        self.parent = None

    def __lt__(self, other):
        return self.f < other.f

def heuristic(node, goal):
    # 启发式估计函数（曼哈頓距離）
    return abs(node.x - goal.x) + abs(node.y - goal.y)

def generate_grid(rows, cols):
    # 生成 64x64 的網格
    grid = {}
    for x in range(rows):
        for y in range(cols):
            neighbors = []
            if x > 0:
                neighbors.append((x - 1, y))
            if x < rows - 1:
                neighbors.append((x + 1, y))
            if y > 0:
                neighbors.append((x, y - 1))
            if y < cols - 1:
                neighbors.append((x, y + 1))
            grid[(x, y)] = neighbors
    return grid

def astar(graph, start, goal):
    open_set = []  # 用於存儲待處理的節點
    closed_set = set()  # 用於存儲已處理的節點

    start_node = Node(start[0], start[1])
    goal_node = Node(goal[0], goal[1])

    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.x == goal_node.x and current_node.y == goal_node.y:
            path = []
            while current_node:
                path.append((current_node.x, current_node.y))
                current_node = current_node.parent
            return path[::-1]

        closed_set.add((current_node.x, current_node.y))

        for neighbor in graph[current_node.x, current_node.y]:
            if neighbor not in closed_set:
                neighbor_node = Node(neighbor[0], neighbor[1])
                neighbor_node.g = current_node.g + 1
                neighbor_node.h = heuristic(neighbor_node, goal_node)
                neighbor_node.f = neighbor_node.g + neighbor_node.h
                neighbor_node.parent = current_node

                heapq.heappush(open_set, neighbor_node)

    return None  # 如果找不到路徑

# 生成 64x64 的網格
graph = generate_grid(64, 64)

start_node = (0, 0)
goal_node = (63, 63)

path = astar(graph, start_node, goal_node)

if path:
    print("最短路徑:", path)
else:
    print("找不到路徑")
