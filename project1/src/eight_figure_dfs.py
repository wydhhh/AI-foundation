#----------------------用dfs解决八数码问题解的存在性-------------------------
#输入九个位置的数，输出1/0

# 控制递归深度
MAX_DEPTH = 1000

# 目标状态
target = "12345678x"

# 四种动作
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(state, step, visited, max_step):
    
    if state == target:
        return 1         # 找到的情况，可以直接返回1表示找到
    
    visited.add(state)   # 标记路过这个节点
    
    if step + 1 > max_step:
        return 0         # 本深度没有找到
    
    answer = 0           # 存储本树的搜索结果

    # 进行遍历探索
    zero_index = state.index('x')
    x, y = zero_index // 3, zero_index % 3 # x码在x行y列
    for i in range(4):   # 四种动作
         new_x, new_y = x + dx[i], y + dy[i]
         if 0 <= new_x < 3 and 0 <= new_y < 3:
            # 执行该动作
            new_zero_index = new_x * 3 + new_y
            new_state = list(state)
            new_state[zero_index], new_state[new_zero_index] = new_state[new_zero_index], new_state[zero_index]
            new_state = ''.join(new_state)
            # 探索沿途未访问过的节点
            if new_state not in visited:
                new_visited = visited.copy()
                new_step = step + 1
                answer = max(dfs(new_state, new_step, new_visited, max_step),answer) #递归探索

    # 本树的探索结果
    return answer

# 读取输入
start_state = input().replace(" ", "")

# 调用 dfs 函数开始进行不同深度的探索，不断更新最小深度
explore_depth = 1
while(dfs(start_state, 0, set(), explore_depth) == 0 and explore_depth <= MAX_DEPTH):
      explore_depth += 1

# 打印结果
print(1 if explore_depth <= MAX_DEPTH else 0)