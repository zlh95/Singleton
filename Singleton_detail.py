class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kw) #继承超类的__new__方法,'Create and return a new object'
        return cls._instance

# 将类的实例和一个类变量 _instance 关联起来，如果 cls._instance 为 None 则创建实例，否则直接返回 cls._instance。
class MyClass(Singleton):
    a = 1

one = MyClass()
#two = MyClass()
#print(one is  two)