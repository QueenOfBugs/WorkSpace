# encapsulation
# 封装，将变量(状态)和方法集中在对象本身

class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def area(self):
        return self.width * self.len


# len和width是对象的状态，area是对象的方法，用来返回长方形面积

# 封装的第二个概念就是，隐藏类的内部数据，避免外部代码直接访问

class Data:
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]

    def change_data(self, index, n):
        self.nums[index] = n


# 创建一个Data对象后，有两种方法访问nums实例变量


data_one = Data()
data_one.nums[0] = 100

data_two = Data()
data_two.change_data(0, 100)

print(data_one.nums)
print(data_two.nums)


# 上面两种方法都能访问nums变量，没有体现封装的隐藏数据的特点
# 其他语言有private variable和private method 来解决这个问题，使用private关键字声明
# 的变量和方法都只能在对象内部使用，外部是访问不了的，但是
# python中没有私有变量，那么所有的变量都是可以公开访问的，python采取了另一种方式解决私有的问题
# 那就是使用命名约定，如果有调用者不该使用的变量和方法，应该在变量名前加下划线

class PublicPrivateExample:
    def __init__(self):
        self.public = "safe"
        self._private = 'unsafe'

    def public_method(self):
        pass

    # 告诉使用者这是私有方法，不推荐调用的
    def _fake_private_method(self):
        pass

    # python会改写这个方法，
    # 实际上声明的是_PublicPrivateExample__private_method
    def __private_method(self):
        pass


# Abstraction
# 抽象--剥离事物的诸多特征，使其保留本质特征，例如长方形，最本质就是长和宽

# polymorphism
# 多态：为不同的基础形态提供相关接口(函数/方法)的能力

print("hello")
print(21)
print(1.2)


# print 为字符串，浮点，整数三种不同的数据类型提供了相同的接口

# 继承：创建类时，该类可以从另一个类继承方法和变量，被继承的叫父类，继承的类叫子类

# 组合：对象可以作为变量保存到另一个对象中--> 在python中可以认为任何事都是对象


# challenge 13
class Shape:
    def what_am_i(self):
        print("i am a {}".format(type(self)))


class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def calculate_perimeter(self):
        return 2 * (self.width + self.length)


class Square(Rectangle):
    def __init__(self, length):
        self.width = length
        self.length = length

    def change_size(self, change_num):
        self.width += change_num
        self.length += change_num


rectangle = Rectangle(3, 4)
square = Square(5)

print(rectangle.calculate_perimeter())
print(square.calculate_perimeter())
square.change_size(-1)
print(square.calculate_perimeter())

square.what_am_i()
rectangle.what_am_i()


class Horse:
    def __init__(self, name):
        self.name = name


class Rider:
    def __init__(self, name, horse):
        self.name = name
        self.horse = horse


horse = Horse("Horse1")
rider = Rider("Harry", horse)

print(rider.horse.name)