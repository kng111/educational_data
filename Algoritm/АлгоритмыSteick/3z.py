buffer_max_capacity, n = (int(i) for i in input().split(' '))

processing_stack = []
current_time = 0

for _ in range(n):
    arrival_time, duration = (int(i) for i in input().split(' '))
    if processing_stack and processing_stack[0][1] <= arrival_time:
        processing_stack.pop(0)
    is_stack_free = True if not processing_stack else False

    if is_stack_free:
        current_time = arrival_time
        processing_stack.append((arrival_time, current_time + duration))
        print(arrival_time)
    else:
        if len(processing_stack) < buffer_max_capacity:
            print(processing_stack[-1][1])
            processing_stack.append((arrival_time, processing_stack[-1][1] + duration))
        else:
            print(-1)