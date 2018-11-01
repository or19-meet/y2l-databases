from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Write your functions to interact with the database here :

def create_product(name, price, quantity):
	product_object = Product(
		name=name,
        price=price,
        quantity=quantity)
	session.add(product_object)
	session.commit()





  #TODO: complete the functions (you will need to change the function's inputs)

def update_product():
  #TODO: complete the functions (you will need to change the function's inputs)
  pass

def delete_product(id):
	session.query(Product).filter_by(id=id).delete()
	session.commit()



  

def get_product(id):
  pass

#create_product("mug", 10, 50)
delete_product(2)