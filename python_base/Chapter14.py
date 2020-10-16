# 类变量和实例变量
# python中，类即对象，每一个类都是type类的实例对象
# 类本身就是一个对象，通过self.[name] = name 的语法定义的都是实例变量，
# 实例变量也属于对象，是属于类实例化后的对象，
# 而不同过self.[name]在类中定义的就是为类本身创建的变量，类变量和普通变量的定义方式一样，只不过必须要在类内部定义
# 类变量的访问方式和实例变量的访问方式一样self.name

class Rectangle:
    recs = []

    def __init__(self, w, l):
        self.width = w
        self.len = l
        self.recs.append((self.width, self.len))


r1 = Rectangle(1, 3)
r2 = Rectangle(2, 4)
r3 = Rectangle(5, 6)

print(Rectangle.recs)


# 魔法方法
# python中所有类都是Object类的子类
# python会在不同情况下使用从Object父类中继承的方法
# 使用pritn打印对象时会调用从Object继承过来的__repr__()方法class Lion
# 如果重写__repr__()方法，那么print对象时就返回自定义的结果class Cat


class Lion:
    def __init__(self, name):
        self.name = name


lion = Lion("Xinba")

print(lion)

print(lion.__repr__())


class Cat:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


cat = Cat("喵喵喵")

print(cat)
print(dir(cat))


# 之所以python可以用加法，是因为每个整数对象都有一个__add__方法，在表达式求值时会自动调用
# 如果在一个类中定义了__add__方法 ，那么就可以在表达式中对其进行加法运算

class AlwaysPositive:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return abs(self.num + other.num)


x = AlwaysPositive(-10)
y = AlwaysPositive(-11)

print(x + y)

# is 关键字可以判断两个对象是否为同一个,其实就是比对地址是否相同
li = [1, 2]
tup = (1, 2, li)

print(tup[2] is li)

p = None
d = 0

print(p is None)
print(d is None)
d = p
print(d is None)
print(d is p)


# challenge14
class Square:
    square_list = []

    def __init__(self, length):
        self.width = length
        self.length = length
        self.square_list.append(self)

    def __repr__(self):
        return '{} by {} by {} by {}'.format(self.width,self.width,self.width,self.width)

s1 = Square(1)
s2 = Square(2)
print(type(Square.square_list))
print(s1)
print(s2)


def is_same(obj1, obj2):
    return obj2 is obj1


print(is_same(s1,s2))

s1 = Square(1)
s2 = Square(1)

print(is_same(s1,s2))
s3 = s1
print(is_same(s1,s3))

li = [1,2]
li_copy = li.copy()
li_asig = li
print(is_same(li,li_asig))
print(is_same(li,li_copy))