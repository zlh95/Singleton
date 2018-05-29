class Borg(object):
    _state = {}
    def __new__(cls, *args, **kw):
        ob = super(Borg, cls).__new__(cls, *args, **kw)
        ob.__dict__ = cls._state
        return ob.__dict__

class MyClass2(Borg):
    a = 1

a = MyClass2()
b = MyClass2()
print(a is b)