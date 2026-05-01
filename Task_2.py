import math

numbers = [5, 10, 15, 20, 25, 30]

print("List:", numbers)

search = int(input("Enter element: "))

block_size = int(math.sqrt(len(numbers)))
start = 0
end = block_size

found = False

while start < len(numbers):
    if numbers[min(end, len(numbers)) - 1] >= search:
        break
    start = end
    end += block_size

for i in range(start, min(end, len(numbers))):
    if numbers[i] == search:
        print("Element found")
        found = True
        break

if not found:
    print("Element not found")