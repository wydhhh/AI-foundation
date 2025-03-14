#----------------朴素dij算法解最短路问题--------------------------
#假设所有边的权重均为正值，输出最小权重

INF = int(1e18)  # 无穷大

n, m = map(int, input().split())                 # 图的基本信息 (V,E)
graph = [[INF] * (n + 1) for _ in range(n + 1)]  # 矩阵格式的图，需要全部初始化为无穷

for _ in range(m):                               #构建图
    x, y, z = map(int, input().split())
    graph[x][y] = min(graph[x][y], z)  

dist = [INF] * (n + 1)       # 记录1号点到各点的最短距离的暂存值/确定值
dist[1] = 0                  # 起点到自身的距离初始化为0
visited = [False] * (n + 1)  # 记录节点是否已经确定了最短距离

for _ in range(n):           #需要反复进行“找到待确定最短距离的节点并进行更新”这件事

    t = -1
    for i in range(1, n + 1): #需要遍历每一个节点才能找到符合要求的节点
        if not visited[i] and (t == -1 or dist[i] < dist[t]): # 找到暂未确定最短距离的点中，距离起点最近的点
            t = i

    #if t == -1:
        #break         # 当所有节点都已经确定距离时，t就是-1
                      # 当然由于循环次数有限，t正常情况不会是-1
    visited[t] = True # t指向未确定到起点最短路径的所有点中，距离起点最近的点
                      # 这里确定它的最短距离就是dist[t]
    if t == n:
        break         # 已经确定答案，无需再探索

    for j in range(1, n + 1): #遍历每一个节点进行更新
        dist[j] = min(dist[j], dist[t] + graph[t][j])   # 用这个新最短距离更新所有节点到起点的最短距离
                                                        # 这些点只是暂时被访问而非确定下最短距离

print(-1 if dist[n]==INF else dist[n])   #打印起点到终点的最小权重距离