num = int(input("Write number:"))
print("Result:", end=" ")
for i in range(num - 1, 1, -1):
    if num % i == 0:
        print(i, end=", ")
