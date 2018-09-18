class Singlet:
    def __new__(cls, *args, **kwargs):
        '''
        __new__()是真正的构造方法，它是一个类方法，
        必须返回一个实例，返回的实例会作为第一个参数（self）
        传给__init__()方法。__init__()方法实际上是初始化方法。
        '''
        if not hasattr(cls,'instance'):
            cls.instance = super().__new__(cls,*args,**kwargs)
        return cls.instance

    def __init__(self):
        print('Singleton 1')

a = Singlet()
b = Singlet()
print(a is b)