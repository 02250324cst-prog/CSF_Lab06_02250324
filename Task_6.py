def iterative_fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

count = 0

def recursive_fibonacci(n):
    global count
    count += 1

    if n <= 1:
        return n
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

num = int(input("Enter number: "))

iter_result = iterative_fibonacci(num)

count = 0
rec_result = recursive_fibonacci(num)

print("Iterative Fibonacci =", iter_result)
print("Recursive Fibonacci =", rec_result)
print("Number of recursive calls =", count)