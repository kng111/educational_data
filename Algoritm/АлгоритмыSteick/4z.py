import sys

stack_max = []  # стек текущих максимумов стека величин, сам стек величин не нужен

n = int(input().strip()) # а зачем нам n?
for query in sys.stdin:
    if 'push' in query:
        value = int(query.strip().split()[1])
        max_value = max(value,stack_max[-1]) if stack_max else value
        stack_max.append(max_value)
    if 'pop' in query:
        stack_max.pop()
    if 'max' in query:
        sys.stdout.write(str(stack_max[-1])+'\n')