# project-one-warm_up
'''
以下是状态转移图：<>框出的为统一个状态衍生出的状态 ()框出的为上文中已经出现的状态,为避免无穷生成树故对这些状态不再衍生

FCGW||                (开始)

<CW||FG>                 (第一轮)

<(FCWG||)    FCW||G>             (第二轮)

<(CW||FG)  C||FGW  W||FCG>                 (第三轮)  

<FCG||W  (FCW||G)>    <(FCW||G)  FGW||C>         (第四轮)

<G||FCW  (C||FGW)>    <G||FCW  (W||FGC)>         (第五轮)

<FG||CW  (FCG||W)  (FGW||C)>     <FG||CW  (FCG||W)  (FGW||C)>     (第六轮) 

<(G||FCW)  ||FCGW>    <(G||FCW)  ||FCGW>         (结束)


如果觉得上面这个不是很清楚，那么run以下下面这个代码更清楚(只画出未过河的东西，并且删除所有的反复，得到的一个简洁完整的状态图):
当然下面这个状态图全部用的单向箭头，事实上应该全部用双向箭头(我没查到斜双向箭头的unicode值)
'''
#----------------------------------------------------------------
print("状态转移图：")

print("FWGC||0000                         (开始)")

print('\u2193')

print("WC||1010                           (第一轮)")

print('\u2193')

print("FWC||0010                          (第二轮)")

print('\u2199              \u2198')

print("C||1110         W||1011            (第三轮)")

print('\u2193              \u2193')

print("FGC||0100      FWG||0001           (第四轮)")

print('\u2198              \u2199')

print("G||1101                            (第五轮)")

print('\u2193')

print("FG||0101                           (第六轮)")  

print('\u2193')

print("空||1111                           (结束)")     

print('\n')
#----------------------------------------------------------------

#下面的代码负责打印队列和递归栈，并且展示分别通过两种方法找到的路径：
from collections import deque

# 定义初始状态和目标状态
initial_state = (0, 0, 0, 0)
goal_state = (1, 1, 1, 1)

# 检查状态是否合法
# 输入是一个元组
def is_valid(state):
    # 人    狼     羊      菜
    human, wolf, sheep, cabbage = state
    if (human != wolf and wolf == sheep) or (human != sheep and sheep == cabbage):
        return False
    return True

# 生成所有可能的下一个状态
# 输入当前的状态 返回若干状态的队列
def get_next_states(state):
    human, wolf, sheep, cabbage = state
    next_states = []
    # 人单独过河
    new_state = (1 - human, wolf, sheep, cabbage)
    if is_valid(new_state):
        next_states.append(new_state)
    # 人带狼过河
    if human == wolf:
        new_state = (1 - human, 1 - wolf, sheep, cabbage)
        if is_valid(new_state):
            next_states.append(new_state)
    # 人带羊过河
    if human == sheep:
        new_state = (1 - human, wolf, 1 - sheep, cabbage)
        if is_valid(new_state):
            next_states.append(new_state)
    # 人带菜过河
    if human == cabbage:
        new_state = (1 - human, wolf, sheep, 1 - cabbage)
        if is_valid(new_state):
            next_states.append(new_state)
    return next_states

# BFS 算法
# 返回单个合法路径
def bfs():
    queue = deque([(initial_state, [initial_state])])
    visited = set([initial_state])
    step = 0
    while queue:

        print(f"Step {step}: Queue is {[item for item,_ in queue]}") 

        # 这个是正确的队列演变路径

        current_state, path = queue.popleft()

        if current_state == goal_state:
            return path   # 仅返回找到的单条路径
        
        for next_state in get_next_states(current_state):
            if next_state not in visited :
                visited.add(next_state)
                new_path = path + [next_state]
                queue.append((next_state, new_path))

        step += 1

    return None

# BFS 算法
# 返回全部合法路径
def bfs_all_paths():

    queue = deque([(initial_state, [initial_state])])
    visited = set() 
    all_paths = []
    step = 0
    print(f"非“标准”演示 Step {step}: Queue is {[item for item,_ in queue]}")

    while queue: 

        current_state, path = queue.popleft() # 出队列
        visited.add(current_state)                            
        step += 1

        if current_state == goal_state:
            all_paths.append(path)
            print(f"非“标准”演示 Step {step}: Queue is {[item for item,_ in queue]}")
            continue  # 保存找到的路径并且本轮不再探索

        for next_state in get_next_states(current_state):
            if next_state not in visited :  
                new_path = path + [next_state]
                queue.append((next_state, new_path)) # 入队列 

        print(f"非“标准”演示 Step {step}: Queue is {[item for item,_ in queue]}")

    return all_paths  # 为了可以返回全部的合法路径，代码输出的queue并不是真实BFS的队列演变，真实的BFS不会对边界进行重复探索，然而真实的BFS无法得到所有合法路径

# DFS 算法
# 返回单个合法路径
def dfs(state=initial_state, path=[initial_state], stack=[]):

    stack.append(state) # 当前节点先入栈

    print(f"非“标准”演示 Depth of exploration is {len(stack) - 1} and recursive Stack is {stack}")

    if state == goal_state:
        return path   #由于只返回一条合法路径，因此这个不是完整的递归栈的演变展示，只是众多分支中触底的一条
    
    for next_state in get_next_states(state):
        if next_state not in path: # 不探索本条路经过的节点
            new_path = path + [next_state]
            result = dfs(next_state, new_path, stack) # 递归探索
            if result:
                return result # 一旦返回则代表找到了合法路径，则整个函数直接返回
            
    stack.pop() # 当前节点晚出栈

    return None

# DFS 算法
# 返回全部合法路径
# 严格来说这只是DFS-visit算法，但考虑到我们应该不会从指定根节点之外的节点开始探索(总是从全没过河那个状态开始探索)那DFS-visit = DFS
# 严格来说DFS应当是遍历所有节点并对他们应用该DFS-visit算法
def dfs_all_paths(state=initial_state, path=[initial_state], stack=[], all_paths=[]):
    
    stack.append(state) # 当前节点先入栈
    print(f"Depth of exploration is {len(stack) - 1} and recursive Stack is {stack}")

    if state == goal_state:
        all_paths.append(path[:]) # 保存找到的路径

    for next_state in get_next_states(state):
        if next_state not in path:  # 不探索本条路经过的节点
            new_path = path + [next_state]
            dfs_all_paths(next_state, new_path, stack, all_paths) # 递归探索

    stack.pop()         # 当前节点晚出栈
    if stack != []:
        print(f"Depth of exploration is {len(stack) - 1} and recursive Stack is {stack}")

    return all_paths # 返回全部合法路径

print("标准的队列演变看bfs的单路径展示，标准的递归栈演变看dfs的多路径展示:")
print("-----------------------------------------------------------------------")
# 运行 BFS 算法
# 打印要求内容
print("BFS Search for one path:")
bfs_path = bfs()
# 打印找到的路径
if bfs_path:
    for item in bfs_path:
        print(item)
else :
    print("no answer found.")

print("-----------------------------------------------------------------------")
# 运行完全 BFS 算法
# 打印要求内容
print("BFS Search for all paths:")
all_paths = bfs_all_paths()
# 打印找到的所有路径
if all_paths:
    print("All valid paths found by BFS:")
    for i, path in enumerate(all_paths, start = 1):
        print(f"Path {i}:")
        for state in path:
            print(state)
        print()
else:
    print("No solution found using BFS.")

print("-----------------------------------------------------------------------")
# 运行 DFS 算法
# 打印要求内容
print("DFS Search for one path:")
dfs_path = dfs()
# 打印找到的路径
if dfs_path:
    for item in dfs_path:
        print(item)
else :
    print("no answer found.")

print("-----------------------------------------------------------------------")
# 运行完全 DFS（-visit） 算法
# 打印要求内容
print("DFS Search for all paths:")
all_paths = dfs_all_paths()
# 打印找到的路径
if all_paths:
    print("All valid paths found by DFS:")
    for i, path in enumerate(all_paths, start = 1):
        print(f"Path {i}:")
        for state in path:
            print(state)
        print()
else:
    print("No solution found using DFS.")

print("-----------------------------------------------------------------------")

