# asami = input("inter Name (split with '-'):").split('-')
# i = 0
# while i < len(asami):
#     item = asami[i]
#     j = 0
#     while j < len(item):
#         if j % 2 == 0:
#             print(item[j].upper(), end='')
#         else:
#             print(item[j], end='')
#         j += 1
#     print()
#     i += 1

# -----------------------------------------------

# i = 1
# while i <= 10:
#     j = 1
#     while j <= 10:
#         print(i * j, end='\t')
#         j += 1
#     print()
#     i += 1

# -----------------------------------------------

# from random import random, seed, randrange, choice,choices
#
# # seed(5)
# # print(random())
# x = ('ali', 'mmd', 'akbr', 'koskhol','ali2', 'mmd2', 'akbr2', 'koskhol2')
# y = choices(x,k=2)
# print(x)
# print(y)

# -----------------------------------------------

# i = 1
# a, b = 0, 1
# while i<10:
#     a, b = b, a+b
#     print(a)
#     i += 1

# -----------------------------------------------

# n = int(input('inter'))
# c = 0
# i = 1
# while i < n:
#     if n % i == 0:
#         c += i
#     i += 1
#
#
# if c == n:
#     print('ok')

# -----------------------------------------------

# from random import randrange, seed
# asami = ['ali', 'mmd', 'hsn', 'konos', 'akbr', 'asqr', 'parpr']
# qoree = []
#
# for i in asami:
#     qoree += ['gol'] + ['poch']
#
# r = randrange(0, len(asami))
# r2 = randrange(0, len(qoree))
# print(asami[r], qoree[r2])

# -----------------------------------------------

# a = 21.6
# i = 10
# s = 'ABc'
# s2 = 'efG'
# d = {'a': 2.2,'b':3}

# print('%(a).1f %(b)i' % (d))                      # 2.2 3
# print('%*.*f'%(15,5,i))                           #         10.00000

# print("hello {1} im {0}".format(s, s2))           # hello efG im ABc
# print("hello {a} im {b}".format(**d))             # hello 2.2 im 3
# print("hello {0} im {1}".format(*'ab'))           # hello a im b
# print("hello {0} im {1}".format(*[1,2]))          # hello 1 im 2
# print("hello {0:,.1f} im {1}".format(1000000,2))  # hello 1,000,000.0 im 2
# print("hello {0:b} im {1}".format(i,2))           # hello 1010 im 2
# print("hello {0:#b} im {1}".format(i,2))          # hello 0b1010 im 2
# print("hello {0:+<10}".format(i,align='>'),"l")   # hello 10++++++++ l

# print(f"x is {i}")                                # x is 10
# print(f"x is {{i}}")                              # x is i
# print(f"x is {{{i}}}")                            # x is {10}

# -----------------------------------------------

# x = int(input('zl 1 :'))
# y = int(input('zl 2 :'))
# z = int(input('zl 3 :'))
#
# if (x+y > z and y+z > x and z+x > y):
#     print('midhd')
#     if x == y == z:
#         print('mots al')
#     elif x == y or z == x or z == y:
#         print('mots sa')
#     elif (x ** 2 == z ** 2 + y ** 2) or\
#             (y ** 2 == x ** 2 + z ** 2) or\
#                 (z ** 2 == x ** 2 + y ** 2):
#         print('qaem')
# else:
#     print('nmidhd')

# -----------------------------------------------

# x = input('bzn :')
#
# if 48 <= ord(x) <= 57:
#     print('add')
# elif 65 <= ord(x) <= 90:
#     print('horof bzorg')
# elif 97 <= ord(x) <= 122:
#     print('horof kochk')
# else:
#     print('symbool')

# -----------------------------------------------

# x = int(input('1 :'))
# y = int(input('2 :'))

# while x < y:
#     x += 1
#     if not x == y:
#         print(x)
# while y < x:
#     y += 1
#     if not x == y:
#         print(y)

# -----------------------------------------------

# x = int(input('1 :'))
# y = int(input('2 :'))
#
# s = set()
# i = 1
# while x % i == 0 and y % i == 0:
#     s.add(i)
#     i += 1
#
# print(s)

# -----------------------------------------------

# x = int(input('1 :'))
# y = int(input('2 :'))
#
# a, b, c = set(), set(), set()
#
# i = 1
# while i < 10:
#     a.add(x * i)
#     b.add(y * i)
#     i += 1
#
# c = a & b
# print(c)

# -----------------------------------------------

# row = int(input('ss :'))
# i = 1
# while i < row:
#     print(i * '*')
#     i += 1

# -----------------------------------------------

# x = int(input('ss :'))
# i = 0
# while x:
#     x //= 10
#     i += 1
# print(i)

# -----------------------------------------------

# from random import choice
# l = ['n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 'n8', 'n9', 'n10']
# while True:
#     if l:
#         c = choice(l)
#         g = input(f"it is {c} ?")
#         if g.lower() == 'no':
#             l.remove(c)
#             continue
#         else:
#             print('ok')
#             break
#     else:
#         print('r u fucking kidding me??')
#         break

# -----------------------------------------------

# def dec(func):
#     def inner(a, b):
#         if b == 0:
#             return 'biblbilak'
#         return func(a, b)
#     return inner
#
#
# @dec
# def f(a, b):
#     return a / b
#
# print(f(5, 5))

# -----------------------------------------------
# from functools import wraps
#
# def star(func):
#     @wraps(func)
#     def inner(*x, **y):
#         print('*' * 10)
#         func(*x, **y)
#         print('*' * 10)
#     return inner
#
#
# @star
# def msg(name):
#     """ docs.. """
#     print('im ' + name)
#
#
# msg('kiri :/')

# -----------------------------------------------
# from functools import wraps
#
# def star(a):
#     def inner1(func):
#         @wraps(func)
#         def inner2(*x, **y):
#             print('*' * a)
#             func(*x, **y)
#             print('*' * a)
#         return inner2
#     return inner1
#
#
# @star(7)
# def msg(name):
#     print('u r ' + name)
#
#
# msg('kivi :/')

# -----------------------------------------------
# from functools import wraps
#
# users = {'a':'1234', 'b':'5678', 'c':'9876'}
# b_list = {'a', 'c'}
#
# def c_ban(func):
#     @wraps(func)
#     def inner(*args, **kwargs):
#         if args[0] in b_list:
#             print('baned..!')
#         else:
#             func(*args, **kwargs)
#     return inner
#
#
# @c_ban
# def ch_pas(username, new_password):
#     users[username] = new_password
#     print(username + ' : ' + users[username])
#
#
# ch_pas('a', '9988')
# ch_pas('b', '9988')

# -----------------------------------------------
# from time import perf_counter
# from functools import wraps
#
# def time_c(func):
#     @wraps(func)
#     def wrapper_decorator(*args, **kwargs):
#         start_t = perf_counter()
#         value = func(*args, **kwargs)
#         run_t = perf_counter() - start_t
#         print('func ', func.__name__, 'is ', run_t)
#         return value
#     return wrapper_decorator
#
#
# @time_c
# def cube(x):
#     s = 0
#     for i in range(1, x):
#         s += i ** 2
#
#
# cube(5555500)

# -----------------------------------------------

# def g():
#     for i in range (5):
#         yield i * 2
#
#
# gg = g()
# for i in  gg:
#     print(i)

# -----------------------------------------------
# from functools import wraps
#
# def c_gen(func):
#     @wraps(func)
#     def start(*args, **kwargs):
#         gn = func()
#         next(gn)
#         return gn
#     return start
#
#
# @c_gen
# def my_gen():
#     print('start')
#     for i in range(3):
#         name = yield i
#         print('my name is : ', name)
#
#
# g = my_gen()
# print(g.send('koko'))
# print(g.send('bokhor'))

# -----------------------------------------------

# def cen_gen(words):
#     print('start..')
#     w = None
#     while True:
#         word = yield w
#         if word not in words:
#             w = word
#         else:
#             w = "*" * len(word)
#
#
# g = cen_gen(['koni', 'kivi', 'lashi'])
# next(g)                                                      # start..
# print(g.send('khobi'))                                       # khobi
# print(g.send('lashi'))                                       # *****

# -----------------------------------------------

# def spl_gen(delimeter=' '):
#     print('start..')
#     s = None
#     while True:
#         line = yield s
#         s = line.split(delimeter)
#
#
# g = spl_gen('-')
# next(g)
# print(g.send('ali-mmd-hsn-baqr'))                          # start..
# g = spl_gen()                                              # ['ali', 'mmd', 'hsn', 'baqr']
# next(g)                                                    # start..
# print(g.send('asqr jafar akbr abas'))                      # ['asqr', 'jafar', 'akbr', 'abas']

# -----------------------------------------------
# from time import sleep
#
# def reverse(n):
#     if n <= 0:
#         return
#     sleep(1)
#     print(n)
#     reverse(n-1)
#
#
# reverse(5)

# -----------------------------------------------

# def mul5(n):
#     if n == 0:
#         return 1
#     elif n % 10 < 5:
#         return mul5(n // 10)
#     else:
#         return n % 10 * mul5(n // 10)
#
#
# print(mul5(654982135))                                     # 10800

# -----------------------------------------------

# def fib(n):
#     if n == 0 or n == 1:
#         return n
#     return fib(n-1) + fib(n-2)
#
# print(fib(6))

# -----------------------------------------------
# from time import sleep
#
# def g_rev(n):
#     if n <= 0:
#         return
#     sleep(1)
#     yield n
#     for i in g_rev(n-1):
#         yield i
#
#
# print(list(g_rev(5)))

# -----------------------------------------------
# from time import sleep
# from functools import wraps
#
# def dec(func):
#     @wraps(func)
#     def wrapper_decorator(*args, **kwargs):
#         print('*' * 10)
#         value = func(*args, **kwargs)
#         print('-' * 10)
#         return value
#     return wrapper_decorator
#
# @dec
# def reverse(n):
#     if n <= 0:
#         return
#     sleep(0.5)
#     print(n)
#     reverse(n-1)
#
#
# reverse(5)

# -----------------------------------------------
# from functools import wraps
#
# def memoize(func):
#     memory = {}
#     @wraps(func)
#     def w_dec(n):
#         if n not in memory:
#             memory[n] = func(n)
#             print(memory)
#         return memory[n]
#     return w_dec
#
# @memoize
# def fib(n):
#     if n == 0 or n == 1:
#         return n
#     return fib(n-1) + fib(n-2)
#
# print(fib(5))

# -----------------------------------------------

# x1 = [i ** 2 for i in range(5) if i % 2 == 0]
# print(x1)


# s1 = [1, 2]
# s2 = [2, 4]
# x2 = [(i, j) for i in s1 for j in s2 if i != j]
# print(x2)


# names = ['ali', 'mmd', 'hsn']
# x3 = [ch for name in names for ch in name]
# print(x3)


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# t = [[row[i] for row in matrix] for i in range(3)]
# # t = list(zip(*matrix))
# for j in t:
#     print(j)


# x = [1, 2, 7, 9, 10]
# z = [j if j % 2 == 0 else 0 for j in x]
# print(z)

# x = [1, 2, 7, 9, 10]
# def f(x):
#     if x % 2 == 0:
#         return x
#     return 0
#
# z = [f(j) for j in x]
# print(z)


# from random import randrange
# def f():
#     return randrange(50, 150)
#
# z = [n for _ in range(10) if (n := f()) > 100]
# print(z)


# names = ['akbr', 'mmd', 'hsn']
# d = {name:[0 for _ in range(5)] for name in names}
# print(d)

# -----------------------------------------------

# def len2(x):
#     t = 0
#     if isinstance(x, int):
#         return len2(str(x))
#     elif isinstance(x, float):
#         return
#     for i in x:
#         t += 1
#     return t

# x = ['a', 'b']
# print(len2(x))


# def max1(*x):
#     s = 0
#     for i in x:
#         if i > s:
#             s = i
#     return s
#
# print(max1(1, 2, 3))


# def sq(x):
#     for i in range(1, x):
#         if i ** 2 == x:
#             return True
#     return False
#
# print(sq(81))


# li = [1,2,3,4]
# z = list(filter(lambda x: x % 2 == 0, li))
# print(z)


# li = [
#     ('ali', 2),
#     ('mmd', 3),
#     ('kok', 1)
# ]
# li.sort(key=lambda x: x[1])
# print(li)


# li = [
#     {'name': 'efi', 'age': 20},
#     {'name': 'ahmd', 'age': 30}
# ]
# li.sort(key=lambda x: x['name'])
# print(li)


# s = 'asdi'
# sw = lambda x: x[0]=='a'
# print(sw(s))


# s = '2.5'
# sw = lambda x: x.replace(".", "", 1).isdigit()
# print(sw(s))



# def en(sec, start=0):
#     s = start
#     for i in sec:
#         yield s, i
#         s += 1
#
# for i, j in en(['aa','bb'], 3):
#     print(i, j)


# def fib():
#     f1 = 0
#     yield f1
#     f2 = 1
#     yield f2
#     while True:
#         f3 = f1 + f2
#         yield f3
#         f1 = f2
#         f2 = f3
#
# fib = fib()
# for _ in range(8):
#     print(next(fib))


# def e_or_o(c):
#     s = 0
#     if c == 'o':
#         s = 1
#     while True:
#         yield s
#         s += 2
#
# eo = e_or_o('o')
# for _ in range(10):
#     print(next(eo))


# def num_gen():
#     c = 1
#     while True:
#         s = ''
#         for i in range(1, c+1):
#             s += f"{c}\t"
#         yield s
#         c += 1
#
# n = num_gen()
# for j in range(10):
#     print(next(n))

# -----------------------------------------------

# import json
# j = {'a': 1, 'b': 2, 'aa': {'aaa': 111}}
# print(json.loads(j))

# with open('f.json', 'r') as i:
#     x = json.load(i)

# print(x)

# with open('f.json', 'w') as bb:
#     json.dump(j, bb, indent=2, sort_keys=True, separators=(',', ':'))

# -----------------------------------------------
# from math import hypot
#
# class Point:
#     def __init__(self, x: float = 0, y: float = 0) -> None:
#         self.move(x, y)
#
#     def move(self, x: float, y: float) -> None:
#         self.x = x
#         self.y = y
#
#     def reset(self):
#         self.move(0, 0)
#
#     def difrence(self, othre: "Point") -> float:
#         return hypot(self.x - othre.x, self.y - othre.y)
#
# p1 = Point()
# p2 = Point(3, 4)
#
# p1.move(1,2)
#
# print(p1.difrence(p2))
# print(p2.difrence(p1))
#
# p1.reset()
# print(p1.x, p1.y)

# -----------------------------------------------
# from bank import BankAccount
#
# p1 = BankAccount('mmd')
# p1.display()
# p1.deposit()
# p1.withdraw()

# -----------------------------------------------

# class PowTow:
#     def __init__(self, max_p):
#         self.n = 0
#         self.max_p = max_p
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.n <= self.max_p:
#             result = self.n ** 2
#             self.n += 1
#             return result
#         raise StopIteration

# obj = PowTow(5)
# for i in obj:
#     print(i)

# print(next(obj))
# print(next(obj))

# -----------------------------------------------








