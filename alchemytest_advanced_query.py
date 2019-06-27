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


class Department(Base):
    __tablename__ = 'departments'
    dept_no = Column(String(4), primary_key=True)
    dept_name = Column(String(40), nullable=False)

    def __repr__(self):
        return "Dept {} {}".format(self.dept_name, self.dept_no)


class Dept_emp(Base):
    __tablename__ = 'dept_emp'
    emp_no = Column(Integer, primary_key=True)
    dept_no = Column(String(4), primary_key=True)
    from_date = Column(Date, nullable=False)
    to_date = Column(Date, nullable=False)


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


# 与
from sqlalchemy import and_, or_, not_
query = session.query(Employees).filter(Employees.emp_no > 10016).filter(Employees.emp_no < 10019)
show(query)

query = session.query(Employees).filter((Employees.emp_no > 10016) & (Employees.emp_no < 10019))
show(query)

query = session.query(Employees).filter(and_(Employees.emp_no > 10016, Employees.emp_no < 10019))
show(query)

# 或
query = session.query(Employees).filter((Employees.emp_no < 10003) | (Employees.emp_no > 10018))
show(query)

query = session.query(Employees).filter(or_(Employees.emp_no < 10003, Employees.emp_no > 10018))
show(query)

# 非
query = session.query(Employees).filter(~(Employees.emp_no < 10003))
show(query)

query = session.query(Employees).filter(not_(Employees.emp_no < 10003))
show(query)

# in
query = session.query(Employees).filter(Employees.emp_no.in_([10005, 10018]))
show(query)
query = session.query(Employees).filter(~Employees.emp_no.in_([10005, 10018]))
show(query)

# like
query = session.query(Employees).filter(Employees.last_name.like('P%'))
show(query)


# order
query = session.query(Employees).filter(Employees.last_name.like('P%')).order_by(Employees.emp_no.desc())
show(query)

# limit offset
query = session.query(Employees).filter(Employees.last_name.like('P%')).\
    order_by(Employees.emp_no.desc()).offset(2).limit(1)
show(query)


print(1, 'query', '!!!!!!!!!!!!!')
print(query.first())  #
print(2, 'query', '!!!!!!!!!!!!!')
print(query.all())  #
print(3, 'query', '!!!!!!!!!!!!!')
print(query.one())  #
print(query.limit(1).one())  #
print(4, 'query', '!!!!!!!!!!!!!')
print(query.count())
print(query.count())


# 聚合函数
from sqlalchemy import func
query = session.query(func.count(Employees.emp_no))
print(query.all())
print(query.first())
print(query.one())
print(query.scalar())  # one结果的第一个元素

print(session.query(func.max(Employees.emp_no)).scalar())
print(session.query(func.min(Employees.emp_no)).scalar())
print(session.query(func.avg(Employees.emp_no)).scalar())

# group
print(session.query(Employees.gender, func.count(Employees.emp_no)).group_by(Employees.gender).all())
























