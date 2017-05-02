# encoding: utf-8
import sys  # 插入sys檔案中所有函式，使用sys檔中的write函式前須加檔名
from time import time  # 從time檔案插入time()函式，使用time()前不需要加檔名

print(sys.version)
print(str(time()) + "\n")


def print_dash():
    print("----------------------------------------------------------------------------------------")
    print()


print_dash()
print("Hello World")

"""
This is pure python program
basic
"""

x = 3
x += 2
print(x)

x -= 1
print(x)

x, y = 99.99 + 1, 5

print(x, y)
print_dash()

my_list1 = []
print(len(my_list1))

my_list1.append(-1)
my_list1.append(25)
my_list2 = [55.55, "Hi", 3, 99, 222, 222]
print(len(my_list2))

my_list2.append('XXXXXXX')
my_list2[0] = 333.333

print(len(my_list1), sum(my_list1), my_list2.count(222))
print(my_list2[0], my_list2[-1], my_list2[1:3], my_list2[2:])
print_dash()

s = "Hello"
s += 'World'
s1 = "HelloWorld".replace("ll", "1")
s2 = "Hello"[0] + "i"
print(s, s1, s2, len(s))
print_dash()

passwd = {'Mars': 00000, 'Mark': 56680}
print(passwd)

passwd['Happy'] = 9999
passwd['Smile'] = 123456

del passwd['Mars']
passwd['Mark'] = passwd['Mark'] + 1

print(passwd)
print(passwd.keys())
print(passwd.get('Mars'))
print(passwd.get('Happy'))

print_dash()

admins = set()
users = {'Smile', 'Tony', 'Happy', 'Sherry', 'Allen', 'Andy', 'Mars'}
admins.add('ihc')
admins.add('Mars')

print(admins & users)
print(admins | users)
print(admins ^ users)
print(admins - users)
print(users - admins)

print_dash()

s = "Hello"
s += 'World'
s1 = "HelloWorld".replace("ll", "11")
s2 = "Hello"[0] + "i"
s3 = "This is a sentence."
print(s, s1, s2, len(s))
print(s3.split(' '))

print_dash()

t = "臺灣"
u = t.encode('utf8')

print(t)
print(u)
print(u.decode('utf8'))
print('臺', t[0], u[0])
print_dash()

x = 2 ** 3
y = 3 / 2
s = "3"
print(3 ** 3)
print(ord('a'), ord('c'), chr(ord('a') + 2))
print(y, int(s) / 2, float(s) / 2, 3 % 2)
print(str(x + y), str(x) + str(y))
print_dash()

print(list(range(0, 10)))
my_list = []

"""//for(i=0;i<10;i++)"""
for i in range(0, 10):
    my_list.append(i + 1)
if my_list[0] == 1 and len(my_list) < 10:
    my_list[0] += 1
    print("1 state")
elif (10 in my_list) or not (len(my_list) == 10):
    print("2 state")
    print("range(i,j) is i~j-1")
else:
    print("3 state")
    print("none of above")

for j in list(range(0, 5)):
    print(j)

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:  # traversal of List sequence
    print('Current fruit :', fruit)

count = 0
while count < 9:
    print('The count is:', count)
    count = count + 1

count = 0
while count < 5:
    print(count, " is  less than 5")
    count = count + 1
else:
    print(count, " is not less than 5")

print_dash()
