#---------------------用逆序数解决八数码问题解的存在性问题-------------------------------
#输入九个位置的数，输出1/0

#计算数组的逆序数
def count_inversions(arr):
    inversions = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j] and arr[i] != 'x' and arr[j] != 'x':
                inversions += 1
    return inversions

# 读取输入
nums = input().split()
inversions = count_inversions(nums)

# 打印结果
print(1 if inversions % 2 == 0 else 0)