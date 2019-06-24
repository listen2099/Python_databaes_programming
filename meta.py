class ModelMeta(type):
    def __new__(cls, name, bases, attrs):
        print('--------------------------')
        print(cls)
        print(name)
        print(bases)
        print(attrs)
        print('--------------------------')
        return super().__new__(cls, name, bases, attrs)
