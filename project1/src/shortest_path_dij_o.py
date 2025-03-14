#----------------------堆优化dij解最短路问题------------------------
#假设所有边的权重均为正值，输出最小权重

import heapq

INF = int(1e18)  # 无穷大

n, m = map(int, input().split())    # 图的基本信息 (V,E)
graph = [[] for _ in range(n + 1)]  # 邻接表格式的图

for _ in range(m):                  # 构建图
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
                                    # (这个方法构建的图没有垃圾值INF)
dist = [INF] * (n + 1)  # 记录各点到起点的最短距离
dist[1] = 0             # 初始化1号点到起点距离为0
#visited = set()         # 保存已经确定最短距离的节点 (貌似不需要)

heap = [(0, 1)]         # 一个最小堆，存储 (距离起点最短距离, 节点编号)元组
                        # 起点到自身距离初始化为0
while heap:
    d, u = heapq.heappop(heap) # 取最小堆顶的元素，也就是距离起点最近的那个节点的信息
                               # (无需像之前那样遍历所有的节点进行寻找)
    #if u in visited:
        #continue     # 不考虑已经确定距离的节点
    #visited.add(u)   # 确定该点的最短距离为dist[u]
                      # (似乎不需要保存访问过的节点，因为堆里面永远是需要更新的节点)

    if u == n:       # 已经确定答案，无需再探索
        break
    
                     # 遍历相邻的节点进行更新即可
                     # (无需像之前那样遍历所有的节点进行更新)
    for v, w in graph[u]:
        if dist[v] > d + w:
            dist[v] = d + w
            heapq.heappush(heap, (dist[v], v))  # 入堆(便于取出最小堆顶的元素)

print(-1 if dist[n]==INF else dist[n])  #打印起点到终点的最小权重距离