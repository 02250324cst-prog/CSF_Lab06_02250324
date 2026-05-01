def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

stack = []

stack.append(40)
stack.append(10)
stack.append(30)
stack.append(20)
stack.append(50)

print("Stack elements:", stack)

numbers = list(stack)

sorted_list = selection_sort(numbers)

print("Sorted list:", sorted_list)