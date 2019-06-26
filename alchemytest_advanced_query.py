import sqlalchemy
from sqlalchemy import create_engine

# connstr = 'mysql+?://username:pswd@ip:port/databasename?key=value'.format()
connstr = '{}://{}:{}@{}:{}/{}'.format('mysql+pymysql', 'root', '123456', '192.168.243.151', 3306, 'test')
engine = create_engine(connstr, echo=True)  # 数据库连接字符串
# 1 创建引擎

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()  # 基类, 元类被修改过
# 2 创建基类

from sqlalchemy import Column, Integer, String, Date, Enum
import enum
class Gender(enum.Enum):
    M = 'M'
    F = 'F'
class Employees(Base):  # class of table, 数据库中已经有表, 为了和这个表描述一致
    __tablename__ = 'employees'  # 指定表名称
    emp_no = Column(Integer, primary_key=True)
    birth_date = Column(Date, nullable=False)
    first_name = Column(String(64), nullable=False)
    last_name = Column(String(64), nullable=False)
    gender = Column(Enum(Gender), nullable=False)
    hire_date = Column(Date, nullable=False)
    def __repr__(self):
        return '<EMP {} {} {}>'.format(self.emp_no, self.first_name, self.last_name)

def show(emps):
    print('-' * 10)
    for x in emps:
        print(x)
    print('-'*10, end='\n\n')

# 建立会话
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)  # 得到Session的类
session = Session()  # 得到session的实例

query = session.query(Employees).filter(Employees.emp_no > 10016)
print(type(query))
show(query)







