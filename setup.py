import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()
# here we need to specify the item name , description of that item price and type of food like Appetizer / dessert / On tray 
# I have added my favorate items in the list 

class Biryani_restaruant(Base):
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)


class MenuItem(Base):
    __tablename__ = 'menu_item'

    name = Column(String(50), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(150))
    price = Column(String(8))
    course = Column(String(50))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Biryani_restaruant)


engine = create_engine('sqlite:///restaurantmenu.db')


Base.metadata.create_all(engine)
metadata = sqlalchemy.MetaData()
items = sqlalchemy.Table('menu_item', metadata, autoload=True, autoload_with=engine)

#print(items.columns.keys())
print(repr(metadata.tables['menu_item']))
print('\n')
print(repr(metadata.tables['restaurant']))

#displaying the menu items 
from sqlalchemy.sql import select
s = select([MenuItem])
conn = engine.connect()
result = conn.execute(s)
for i in result:
    print(i)

