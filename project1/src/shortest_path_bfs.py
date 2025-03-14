#-------------------BFS解最短路问题-----------------------
#假设所有边的权重相同，均为1，输出最小权重

from collections import deque

n, m = map(int, input().split()) #图的基本信息 (V,E)
graph = [[] for _ in range(n + 1)]  # 邻接表格式的图

# 构建图
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

dist = [-1] * (n + 1)  # 记录每个点到起点的最短距离,初始值-1
dist[1] = 0            # 起点到自身的距离为0

queue = deque([1])  # 初始化节点的队列，将起点加入队列

while queue:
    u = queue.popleft()  # 出队列

    if u == n:           # 如果终节点已经被访问过，等价于确定了最短距离，直接退出
        break

    for v in graph[u]:
        if dist[v] == -1:  # 如果v点未确定最短距离，等价于它未被访问过
            dist[v] = dist[u] + 1  # 确定v点到起点的最短距离
            queue.append(v)  # 入队列

print(dist[n])  # 打印起点到终点的最短距离