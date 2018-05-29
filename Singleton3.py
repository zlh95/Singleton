
def singleton(cls):
    instance = {}
    def wrap(*args,**kwargs):
        if cls not in instance:
            instance[cls] = cls(*args,**kwargs)
        #print(instance[cls])
        return instance[cls]
    return wrap

@singleton
class Single:
    pass

a = Single()
b = Single()
print(a is b)