class A:
    attr = 'A'

    @staticmethod
    def method1():
        print('A.method1')

    def method2(self):
        print('A.method2')


class B(A):
    attr = 'B'

    @staticmethod
    def method3():
        print('B.method3')


class C(A):
    attr = 'C'

    def method2(self):
        print('C.method2')

    @staticmethod
    def method3():
        print('C.method3')


class D(B, C):
    @staticmethod
    def method4():
        print('D.method4')

    @classmethod
    def service1(cls):
        print('class method')

    @staticmethod
    def service2():
        print('static method')


d = D()
d.method4()  # 在 D 找到，D.method4
d.method3()  # 以 D->B 順序找到，B.method3
d.method2()  # 以 D->B->C 順序找到，C.method2
d.method1()  # 以 D->B->C->A 順序找到，A.method1
print('-----------------------------------------------')
D.service1()
D.service2()
print(d.attr)
print('-----------------------------------------------')
D.method4()  # 在 D 找到，D.method4
D.method3()  # 以 D->B 順序找到，B.method3
D.method2(D())  # 以 D->B->C 順序找到，C.method2
D.method1()  # 以 D->B->C->A 順序找到，A.method1
