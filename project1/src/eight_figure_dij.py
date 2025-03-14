#--------------------用dij解决八数码问题的最少步数解-----------------------------
#输入九个位置的数，输出最少步数

import heapq

# 目标状态
target = "12345678x"

# 四种动作
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra(start_state):
    
    # 把这些信息结构放在函数内，是因为八数码问题的起点是不定的
    dist = {start_state: 0}    # 记录各个状态到起点的步数
                               # 并对起点初始化
                               # 用字典比用列表更便于索引
    heap = [(0, start_state)]  # (步数, 状态)的最小堆
                               # 起点到自身步数初始化为0
    #visited = set()    # 保存已经确定步数的节点 (貌似不需要)

    while heap:

        d, state = heapq.heappop(heap) # 出最小堆 也就是目前距离起点步数最少的节点的信息

        #if state in visited:
            #continue   # 不考虑已经确定距离的状态
        #visited.add(state)
                        # (貌似不需要)
        if state == target:
            return d    # 已经确定答案，无需再探索
        
        # 进行相邻状态的遍历探索
        zero_index = state.index('x')
        x, y = zero_index // 3, zero_index % 3  # x码在x行y列
        for i in range(4): # 四种动作
            new_x, new_y = x + dx[i], y + dy[i]
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                # 执行该动作
                new_zero_index = new_x * 3 + new_y
                new_state = list(state)
                new_state[zero_index], new_state[new_zero_index] = new_state[new_zero_index], new_state[zero_index]
                new_state = "".join(new_state)
                # 对以下条件这些相邻的节点更新即可
                if new_state not in dist or d + 1 < dist[new_state]:
                    dist[new_state] = d + 1
                    heapq.heappush(heap, (d + 1, new_state)) # 入最小堆 (便于取堆顶)

    return -1 # 这代表并没有找到那个终态

# 读取输入
start_state = input().replace(" ", "")

#打印结果
print(dijkstra(start_state))