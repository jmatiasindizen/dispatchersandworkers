from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:', echo=True)
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)

Base = declarative_base()

class IdentityA(Base):
    __tablename__ = 'IdentityA'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    result = Column(Integer)

    def __repr__(self):
        return "<Result(result='%s')>" % (self.result)

class IdentityB(Base):
    __tablename__ = 'IdentityB'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    result = Column(Integer)

    def __repr__(self):
        return "<Result(result='%s')>" % (self.result)

class IdentityC(Base):
    __tablename__ = 'IdentityC'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    result = Column(Integer)

    def __repr__(self):
        return "<Result(result='%s')>" % (self.result)

class persistentA(object):
    def __init__(self):
        self.name = ''
    def __call__(self,original_func):
        def new_function(*args,**kwargs):
            try:
                original_func(*args,**kwargs)
            except:
                return
            
            #if there are no problems in operation persist result
            session = Session()
            obj_result = ResultA(result=self.result)
            session.add(obj_result)
            session.commit()
            
        return new_function

class persistentB(object):
    def __init__(self):
        self.name = ''
    def __call__(self,original_func):
        def new_function(*args,**kwargs):
            try:
                original_func(*args,**kwargs)
            except:
                return
            
            #if there are no problems in operation persist result
            session = Session()
            obj_result = ResultB(result=self.result)
            session.add(obj_result)
            session.commit()
            
        return new_function

class persistentC(object):
    def __init__(self):
        self.name = ''
    def __call__(self,original_func):
        def new_function(*args,**kwargs):
            try:
                original_func(*args,**kwargs)
            except:
                return
            
            #if there are no problems in operation persist result
            session = Session()
            obj_result = ResultC(result=self.result)
            session.add(obj_result)
            session.commit()
            
        return new_function
