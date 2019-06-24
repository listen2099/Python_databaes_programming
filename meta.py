class ModelMeta(type):
    def __new__(cls, name, bases, attrs):
        print('1--------------------------')
        print(cls)
        print(name)
        print(bases)
        print(attrs)
        print('2--------------------------')
        return super().__new__(cls, name, bases, attrs)


class Base(metaclass=ModelMeta):
    """它自己和子类来自ModelMeta"""
    pass


class Field:  # 描述字段
    def __init__(self, field_name='id', pk=False, nullable=True):
        self.field_name = field_name
        self.pk = pk
        self.nullable = nullable


#  SQLAlchemy
#  student
class Student(Base):
    id = Field()
    name = Field()
    age = Field()
