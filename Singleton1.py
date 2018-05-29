class Singlet:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'instance'):
            cls.instance = super().__new__(cls,*args,**kwargs)
        return cls.instance

    def __init__(self):
        print('Singleton 1')

a = Singlet()
b = Singlet()
print(a is b)