class Singleton:

    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

singleton_obj1 = Singleton()
singleton_obj2 = Singleton()

print(singleton_obj1)
print(singleton_obj2)