import math

# def distance(p1, p2):
#     dx = p1[0] - p2[0]
#     dy = p1[1] - p2[1]
#     return math.sqrt(dx*dx + dy*dy)

# p1 = [10, 39]
# p2 = [8, 20]

# print(distance(p1, p2))

# def distance(p1, p2):
#     dx = p1['x'] - p2['x']
#     dy = p1['y'] - p2['y']
#     return math.sqrt(dx*dx + dy*dy)

# p1 = {'x': 10, 'y': 39}
# p2 = {'x': 8, 'y': 20}

# print(distance(p1, p2))

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y

#     def distance(self, p):
#         dx = self.x - p.x
#         dy = self.y - p.y
#         return math.sqrt(dx*dx + dy*dy)
    
#     def scale(self, v):
#         self.x = v
#         self.y = v


# # point_0 = Point()
# point_1 = Point(3, 10)
# point_2 = Point(8,4)
# print(point_1)

# x = [1, 2, 4, 5]

# print(type(point_1))
# print(point_1.distance(point_2))
# print(point_1.scale(6))

# class Rotator:
    
#     def __init__(self, alpha):
#         self.setAlpha(alpha)

#     def set_alpha(self, alpha):
#         self.__alpha = alpha
#         self.cos_alpha = math.cos(alpha)
#         self.sin_alpha = math.sin(alpha)

#     def rotate(self, px, py):
#         rx = px*self.cos_alpha + py * self.sin_alpha
#         ry = -px*self.sin_alpha + py * self.cos_alpha
#         return rx, ry

# move = Rotator()

# class MyClass:

#     def __init__(self):
#         pass

#     def __privatemethod(self, x):
#         print(x)

#     def publicmethod(self):
#         self.__privatemethod('hi')

# mc = MyClass()
# mc.publicmethod()
# mc.__privatemethod('hi')

# class ParentA:
#     def __init__(self):
#         super().__init__()
#         print('parent a initializer')

# class ParentB:
#     def __init__(self):
#         super().__init__()
#         print('parent b initializer')

# class Child(ParentA, ParentB):
#     def __init__(self):
#         super().__init__()

# kids = Child()

# print(kids)

class User:
    def __init__(self, name):
        self.name = name
        self.log_count = 0
        self.__id = 1

    def __log(self):
        self.log_count += 1
    
    def login(self):
        self.__log()
        return self.name + '  has logged in'

    def show_logs(self):
        print(self.log_count)
    
    def __str__(self):
        return self.name
    
    def __len__(self):
        return self.log_count + 1

user_1 = User('Ronnie')
user_2 = User('Scott')

# print(user_1)
# print(type(user_1))
# print(user_1.login())
# print(user_1.login())
# print(user_1.login())
# print(user_1.login())
# print(user_1.show_logs())

print(user_1 == user_2)
print(user_1 != user_2)
print(user_1.__str__())
print(user_1.__len__())

