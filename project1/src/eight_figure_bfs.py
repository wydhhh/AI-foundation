#--------------------用bfs解决八数码问题的最少步数解-----------------------------
#输入九个位置的数，输出最少步数

from collections import deque

# 目标状态
target = "12345678x"

# 四种动作
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start_state):
    
    # 把这些信息结构放在函数内，是因为八数码问题的起点是不定的
    queue = deque([(start_state, 0)])  # 初始化(状态, 步数)的队列
                                       # 这里直接把步数和状态保存在一起，因为各个状态难以在列表中索引
                                       # 当然这样做的话，最终只能保存终状态的步数，其他状态的步数本来就不必保存
    visited = set([start_state])       # 保存已经访问的状态

    while queue:

        state, step = queue.popleft() # 出队列

        if state == target:
            return step  #如果终状态已经被访问过，等价于已经确定最短步数，直接退出
        
        # 进行遍历探索
        zero_index = state.index('x')
        x, y = zero_index // 3, zero_index % 3 # x码在x行y列
        for i in range(4): # 四种动作
            new_x, new_y = x + dx[i], y + dy[i]
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                # 执行该动作
                new_zero_index = new_x * 3 + new_y
                new_state = list(state)
                new_state[zero_index], new_state[new_zero_index] = new_state[new_zero_index], new_state[zero_index]
                new_state = "".join(new_state)
                # 已经访问的节点 等价于 已经确定步数
                # 只对那些没有确定步数的节点访问
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, step + 1)) # 入队列

    return -1   # 这代表并没有找到那个终态

# 读取输入
start_state = input().replace(" ", "")

# 打印结果
print(bfs(start_state))