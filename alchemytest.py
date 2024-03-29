import sqlalchemy
from sqlalchemy import create_engine

# connstr = 'mysql+?://username:pswd@ip:port/databasename?key=value'.format()
connstr = '{}://{}:{}@{}:{}/{}'.format('mysql+pymysql', 'root', '123456', '192.168.243.151', 3306, 'school')
engine = create_engine(connstr, echo=True)  # 数据库连接字符串
# 1 创建引擎

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()  # 基类, 元类被修改过
# 2 创建基类

from sqlalchemy import Column, Integer, String, Date
class Student(Base):  # class of table, 数据库中已经有表, 为了和这个表描述一致
    __tablename__ = 'student'  # 指定表名称
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=False)
    age = Column(Integer)

    def __repr__(self):
        return '<Student {} {} {}>'.format(self.id, self.name, self.age)
# 3 创建实体类

# s1 = Student()  # 创建一个实例
# s1.age = 20
# s1.name = 'tom'
# print(s1)
#
# s2 = Student(id=5, name='jerry')  # 创建另一个实例
# s2.age = 30
# print(s2)

Base.metadata.create_all(bind=engine)
# Base.metadata.drop_all(bind=engine)
# 这个是用来创建或删除表的,一般不这样用,一般都是操作已经有的表








