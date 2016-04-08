import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

"""
Model for cities.
It has a one to many relationship with both Attractions and Restaurants.
"""
class City(Base):

    __tablename__ = 'city'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    population = Column(Integer, nullable=False)
    country = Column(String(80), nullable=False)
    demonym = Column(String(80), nullable=False)
    elevation = Column(Float, nullable=False)
    description = Column(String(255), nullable=False)
    image = Column(String(255), nullable=False)     

"""
Model for attractions.
It has a many to one relationship with City
"""

class Attraction(Base):
    __tablename__ = 'attraction'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    rating = Column(Float, nullable=False)
    city_id = Column(Integer, ForeignKey('city.id'), nullable=False)
    num_reviews = Column(Integer, nullable=False)
    category = Column(String(80), nullable=False)
    image = Column(String(255), nullable=False) 


"""
Model for restaurant.
It has a many to one relationship with City
"""
class Restaurant(Base):
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    rating = Column(Float, nullable=False)
    city_id = Column(Integer, ForeignKey('city.id'), nullable=False)
    category = Column(String(30), nullable=False)
    address = Column(String(255), nullable=False)
    image = Column(String(255), nullable=False)  


# engine = create_engine('mysql+mysqldb://swespt:@localhost/swespt?charset=utf8')
# engine = create_engine('sqlite:///swespt.db')


SQLALCHEMY_DATABASE_URI = \
    '{engine}://{username}:{password}@{hostname}/{database}'.format(
        engine='mysql+pymysql',
        username=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        hostname=os.getenv('MYSQL_HOST'),
        database=os.getenv('MYSQL_DATABASE'))

Base.metadata.create_all(SQLALCHEMY_DATABASE_URI)