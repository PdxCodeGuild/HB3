# list = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(list[1::2])

# print([[1 if col == row else 0 for col in range(0, 3)] for row in range(0, 3)])

# def fibonacci(n):
#     if n == 0 or n == 1:
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(17))

d = {1: "one", 2: "three"}
print(d)
d1 = {2: "two"}

# updates the value of key 2
d.update(d1)

print(d)