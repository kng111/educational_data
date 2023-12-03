from collections import deque

def max_in_sliding_window(nums, m):
    result = []
    window = deque()

    for i in range(len(nums)):
        while window and window[0] <= i - m:
            window.popleft()
        while window and nums[i] >= nums[window[-1]]:
            window.pop()

        window.append(i)
        if i >= m - 1:
            result.append(nums[window[0]])

    return result

# Ввод данных
n = int(input())
nums = list(map(int, input().split()))
m = int(input())

# Поиск максимумов в скользящем окне
result = max_in_sliding_window(nums, m)

# Вывод результата
print(' '.join(map(str, result)))