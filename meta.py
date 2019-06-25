#  对象关系映射(ORM)
class ModelMeta(type):
    def __new__(cls, name, bases, attrs):
        print('1--------------------------')
        print(cls)
        print(name)
        print(bases)
        print(attrs)
        print('2--------------------------')
        if '__table_name__' not in attrs.keys():
            attrs['__table_name__'] = name  # 可以对指定的类名做一写事情..

        primary_keys = []
        for k, v in attrs.items():
            if isinstance(v, Field):
                if v.pk:
                    primary_keys.append(v)
                if not v.field_name:
                    v.file_name = k

        attrs['__pks__'] = primary_keys

        return super().__new__(cls, name, bases, attrs)


class Base(metaclass=ModelMeta):
    """它自己和子类来自ModelMeta"""
    pass


class Field:  # 描述字段
    def __init__(self, field_name='', pk=False, nullable=True):
        self.field_name = field_name
        self.pk = pk
        self.nullable = nullable


#  SQLAlchemy
#  student
class Student(Base):
    id = Field(pk=True)
    name = Field('USERNAME', nullable=False)
    age = Field()

