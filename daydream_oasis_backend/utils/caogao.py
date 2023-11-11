class A:
    def fun(a):
        print('aaaaa')



class B:
    def fun(a):
        print('bbbbb')


class C(A, B):
    ...


c = C()
c.fun()
