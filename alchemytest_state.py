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
        return '<{} id={} name={} age={}>'.format(self.__class__.__name__, self.id, self.name, self.age)


# 建立会话
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)  # 得到Session的类
session = Session()  # 得到session的实例



from sqlalchemy.orm.state import InstanceState
def getstate(entity, i):
    insp = sqlalchemy.inspect(entity)
    state = "sessionid={}, attached={}\ntransient={}, persistent={}\npending={},deleted={},detached={}".format(
        insp.session_id,
        insp._attached,
        insp.transient,
        insp.persistent,
        insp.pending,
        insp.deleted,
        insp.detached
    )
    print(i, state)
    print(insp.key)
    print('-' * 30)

student = session.query(Student).get(2)
getstate(student, 1)  # persistent


try:
    student = Student(id=2, name="sam", age=30)
    getstate(student, 2)  # transit
    student = Student(name="sammy", age=30)
    getstate(student, 3)  # transit
    session.add(student)  # add后变成pending
    getstate(student, 4)  # pending
    # session.delete(student) # 删除的前提是persistent，否则抛异常
    # getstate(student, 5)
    session.commit()
    getstate(student, 6)  # persistent
except Exception as e:
    session.rollback()
    print('~~~~~~~~')
    print(e)


# student = session.query(Student).get(2)
# getstate(student, 10) # persistent
# try:
#     session.delete(student) # 删除的前提是persistent
#     getstate(student, 11) # persistent
#     session.flush()
#     getstate(student, 12) # deleted
#     session.commit()
#     getstate(student, 13) # persistent
# except Exception as e:
#     session.rollback()
#     print('~~~~~~~~')
#     print(e)














