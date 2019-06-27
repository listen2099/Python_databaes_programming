import sqlalchemy
from sqlalchemy import create_engine

# connstr = 'mysql+?://username:pswd@ip:port/databasename?key=value'.format()
connstr = '{}://{}:{}@{}:{}/{}'.format('mysql+pymysql', 'root', '123456', '192.168.243.151', 3306, 'test')
engine = create_engine(connstr, echo=True)  # 数据库连接字符串
# 1 创建引擎

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()  # 基类, 元类被修改过
# 2 创建基类

from sqlalchemy import Column, Integer, String, Date, Enum, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
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

    departments = relationship('Dept_emp')

    def __repr__(self):
        return '<EMP {} {} {} {}>'.format(self.emp_no, self.first_name, self.last_name, self.departments)


class Department(Base):
    __tablename__ = 'departments'
    dept_no = Column(String(4), primary_key=True)
    dept_name = Column(String(40), nullable=False)

    def __repr__(self):
        return "Dept {} {}".format(self.dept_name, self.dept_no)


class Dept_emp(Base):
    __tablename__ = 'dept_emp'
    emp_no = Column(Integer, ForeignKey('employees.emp_no', ondelete='CASCADE'), primary_key=True)
    dept_no = Column(String(4), ForeignKey('departments.dept_no', ondelete='CASCADE'), primary_key=True)
    from_date = Column(Date, nullable=False)
    to_date = Column(Date, nullable=False)

    def __repr__(self):
        return "Dept_emp {} {}".format(self.dept_no, self.emp_no)


# Base.metadata.create_all(bind=engine)

def show(emps):
    print('-' * 10)
    for x in emps:
        print(x)
    print('-'*10, end='\n\n')



# 建立会话
from sqlalchemy.orm import sessionmaker, relationship
Session = sessionmaker(bind=engine)  # 得到Session的类
session = Session()  # 得到session的实例

# 多表查询
query = session.query(Employees, Dept_emp).filter(Employees.emp_no == 10010).filter(Employees.emp_no == Dept_emp.emp_no)
show(query)

query = session.query(Employees).join(Dept_emp).filter(Employees.emp_no == 10010).filter(Employees.emp_no == Dept_emp.emp_no)
print(query.all())

print('-'*30)
query = session.query(Employees).join(Dept_emp, Employees.emp_no == Employees.emp_no).filter(Employees.emp_no == 10010).filter(Employees.emp_no == Dept_emp.emp_no)
print(query.all())

print('-'*30)
query = session.query(Employees).join(Dept_emp, Employees.emp_no == Employees.emp_no).filter(Employees.emp_no == 10010)
print(query.all())
for x in query:
    print(x.emp_no)
    print(x.departments)














