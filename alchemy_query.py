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


# 建立会话
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)  # 得到Session的类
session = Session()  # 得到session的实例

# 检查查询
query = session.query(Student)  # 无条件查询
print(type(query), '1----------------------')
for student in query:
    print(student, '2----------------------')
    print(type(student), '3----------------------')


student = session.query(Student).get(10)  # 按主键查询,先查才能改
#student = Student()
student.id = 11
student.name = 'sam'
print(student)

# 改
student.age = 58  # update
session.add(student)
try:
    session.commit()
except Exception as e:
    print(e)
    session.rollback()
print(student)

# 删除
student = session.query(Student).get(10)  # 按主键查询,先查才能删除
#student = Student()
#student.id = 10
session.delete(student)
try:
    session.commit()
except Exception as e:
    print(e)
    session.rollback()
print(student)






