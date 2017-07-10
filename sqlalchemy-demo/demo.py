# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, Text
from sqlalchemy import Sequence
from sqlalchemy import and_, or_
from sqlalchemy import ForeignKey

from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DATABASE_URI = "mysql://%s:%s@%s/%s" % ('root', '', '127.0.0.1', 'db_demo')

Base = declarative_base()
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)

# Create DB session
Session = sessionmaker(bind=engine)

class User(Base):
    """ User table scheme"""
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(50))

    addresses = relationship('Address', back_populates='user',
        cascade="all, delete, delete-orphan")

    posts = relationship('BlogPost', back_populates='author', lazy='dynamic')

    def __repr__(self):
        return "<User name='%s'>" % self.name

class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    email_address = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates='addresses')

    def __repr__(self):
        return '<Address email_address="%s">' % self.email_address

#=====================================================================================
# Many to many
#=====================================================================================

# association table
post_keywords = Table('post_keywords', Base.metadata,
    Column('post_id', ForeignKey('posts.id'), primary_key=True),
    Column('keyword_id', ForeignKey('keywords.id'), primary_key=True))

class BlogPost(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    headline = Column(String(255), nullable=False)
    body = Column(Text)

    # many to many BlogPost <-> Keyword
    keywords = relationship('Keyword', secondary=post_keywords, back_populates='posts')

    author = relationship('User', back_populates='posts')

    def __init__(self, headline, body, author):
        self.author = author
        self.headline = headline
        self.body = body

    def __repr__(self):
        return "BlogPost(%s, %s, %s)" % (self.headline, self.body, self.author)

class Keyword(Base):
    __tablename__ = 'keywords'

    id = Column(Integer, primary_key=True)
    keyword = Column(String(50), nullable=False, unique=True)
    posts = relationship('BlogPost', secondary=post_keywords, back_populates='keywords')

    def __init__(self, keyword):
        self.keyword = keyword

# Init db , create all table
Base.metadata.create_all(engine)

# Get session
session = Session()

def addUser(name, fullname, password):
    user = User(name=name, fullname=fullname, password=password)

    session.add(user)
    session.commit()

def add_all():
    user1 = User(name='wendy', fullname='Wendy Williams', password='foobar')
    user2 = User(name='mary', fullname='Mary Contrary', password='xxg527')
    user3 = User(name='fred', fullname='Fred Flinstone', password='blah')

    session.add_all([user1, user2, user3])
    session.commit()

def query():
    # user = session.query(User).filter_by(name='zhang').first()
    # print user

    query = session.query(User)

    # equals
    # print query.filter(User.name == 'mary').all()

    # not equals
    # print query.filter(User.name != 'mary').all()

    # like
    # print query.filter(User.name.like('%an%')).all()

    # ilike
    # print query.filter(User.name.ilike('%an%')).all()

    # in
    # print query.filter(User.name.in_(['wendy', 'jack'])).all()

    # and
    # print query.filter(and_(User.name == 'zhang', User.password == '123456')).first()
    # print query.filter(User.name == 'zhang', User.password == '123456').first()
    # print query.filter(User.name == 'zhang').filter(User.password == '123456').first()

    # or
    # print query.filter(or_(User.name == 'zhang', User.name == 'mary')).all()

    # match
    # print query.filter(User.name.match('zhang'))

    # count
    print query.filter(User.name.like('%li%')).count()

def deleteUser():
    user = session.query(User).filter_by(name='li').one()
    if user:
        session.delete(user)
        session.commit()

def addAddress():
    jack = User(name='jack', fullname='Jack Bean', password='123456')
    session.add(jack)
    session.commit()

    jack = session.query(User).filter_by(name='jack').first()
    print jack.addresses
    jack.addresses = [
        Address(email_address='jack@google.com'),
        Address(email_address='j25@yahoo.com')
    ]
    session.add(jack)
    session.commit()

def addBlogPost():
    jack = session.query(User).filter_by(name='jack').one()

    post = BlogPost("Jack's Blog Post", "This is a test", jack)
    post.keywords.append(Keyword('Jack'))
    post.keywords.append(Keyword('firstpost'))

    session.add(post)
    session.commit()

def queryBlogPost():
    # result = session.query(BlogPost).filter(BlogPost.keywords.any(keyword='firstpost')).all()
    # print result

    jack = session.query(User).filter_by(name='jack').one()
    result = session.query(BlogPost).\
                    filter(BlogPost.author==jack).\
                    filter(BlogPost.keywords.any(keyword='firstpost')).\
                    all()
    print result

def queryUserAndAddress():
    for u, a in session.query(User, Address).\
                        filter(User.id == Address.user_id).\
                        filter(Address.email_address == 'jack@google.com').\
                        all():
        print u
        print a


    result = session.query(User).join(Address).\
                    filter(Address.email_address=='jack@google.com').\
                    all()
    print result

def queryJoin():
    from sqlalchemy.orm import joinedload

    jack = session.query(User).options(joinedload(User.addresses)).filter_by(name='jack').one()
    print jack

    print jack.addresses

if __name__ == '__main__':
    # addUser('zhang', 'zhangsan', '123456')
    # addUser('li', 'lisi', '123456')
    # addUser('ling', 'lingliu', '123456')

    # add_all()
    # query()

    # deleteUser()

    # addAddress()
    # addBlogPost()
    queryBlogPost()



















































