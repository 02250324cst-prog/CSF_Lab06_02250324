def linear_search(queue, key):
    for i in range(len(queue)):
        if queue[i] == key:
            return i
    return -1

queue = []

queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)
queue.append(50)

print("Queue elements:", queue)

search = int(input("Enter element to search: "))

position = linear_search(queue, search)

if position != -1:
    print("Element found at position", position + 1)
else:
    print("Element not found")