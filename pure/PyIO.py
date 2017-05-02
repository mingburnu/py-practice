# encoding: utf-8

fo = open("foo.txt", "w+")

print("Name of the file: ", fo.name)
print("Closed or not : ", fo.closed)
print("Opening mode : ", fo.__getattribute__('mode'))
fo.write("Python is a great language.\nYeah its great!!\n")
fo.close()

fo = open("foo.txt", "r+")
do = open("doo.txt", "w+")
content = fo.read()
print("foo content : ", content)
do.write(content)

fo.close()
do.close()
