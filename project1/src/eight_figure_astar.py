import heapq

# 计算八个数码的曼哈顿距离之和作为状态的估价函数
# 该值越大，说明该状态与终态区别越大
def manhattan_distance(state):
    distance = 0
    target = "12345678x"
    pos = {num: i for i, num in enumerate(target)}
    for i, num in enumerate(state):
        if num != 'x':
            distance += abs(i // 3 - pos[num] // 3) + abs(i % 3 - pos[num] % 3)
    return distance

# 目标状态
target = "12345678x"

# 四种动作
directions = {'u': (-1, 0), 'd': (1, 0), 'l': (0, -1), 'r': (0, 1)}

# A* 算法
def astar(start_state):
    
    # 记录各个节点从七点开始需要的步数
    dist = {start_state: 0}
    # (曼哈顿距离f值, 状态, 动作路径字符串)的优先队列
    pq = [(manhattan_distance(start_state), start_state, "")]

    # 保存已经探索过的状态
    #visited = set([start_state])  (貌似不需要)

    while pq:

        _, state, path = heapq.heappop(pq) # 出队列
                                           # 也就是探索与目标状态最接近的那个状态
                                           
        if state == target:
            return path # 已经确定答案，无需再探索
        
        # 进行相邻状态的遍历探索
        zero_index = state.index('x')
        x, y = zero_index // 3, zero_index % 3
        for dir_char, (dx, dy) in directions.items(): # 四种动作
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                # 执行该动作
                new_zero_index = new_x * 3 + new_y
                new_state = list(state)
                new_state[zero_index], new_state[new_zero_index] = new_state[new_zero_index], new_state[zero_index]
                new_state = "".join(new_state)
                # 对以下条件这些相邻的节点更新即可
                if new_state not in dist or len(path) + 1 < dist[new_state]:
                    dist[new_state] = len(path) + 1
                    new_path = path + dir_char
                    new_manhattan = dist[new_state] + manhattan_distance(new_state)
                    heapq.heappush(pq, (new_manhattan, new_state, new_path)) # 入队列

    return "unsolvable" # 这代表并没有找到那个终态

# 读取输入
start_state = input().replace(" ", "")

# 打印结果
print(astar(start_state))