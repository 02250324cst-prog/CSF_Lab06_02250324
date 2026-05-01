numbers = [10, 20, 30, 40, 50]

print("List:", numbers)

search = int(input("Enter element to search: "))

found = False

for i in range(len(numbers)):
    if numbers[i] == search:
        print("Element found at position", i + 1)
        found = True
        break

if not found:
    print("Element not found")