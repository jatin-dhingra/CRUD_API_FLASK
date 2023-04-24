from flask import current_app as app
from flask import Flask, request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

    
import os

app=Flask(__name__)

basedir=os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'db.sqlite')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

ma=Marshmallow(app)

class Product(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),unique=True)
    description=db.Column(db.String(200))
    qty=db.Column(db.Integer)
    price=db.Column(db.Float)
    
    def __init__(self,name,description,qty,price):
        self.name=name
        self.description=description
        self.qty=qty
        self.price=price

class ProductSchema(ma.Schema):
  class Meta:
    fields = ('id', 'name', 'description', 'price', 'qty')



product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

@app.route('/product',methods=['POST'])
def addproduct():
    name=request.json['name']
    description=request.json['description']
    qty=request.json['qty']
    price=request.json['price']
    
    new_product=Product(name,description,qty,price)
    db.session.add(new_product)
    db.session.commit()
    
    return product_schema.jsonify(new_product)
    

@app.route('/product',methods=['GET'])
def getproduct():
    allproducts=Product.querry.all()
    result= products_schema.dump(allproducts)
    return jsonify(result.data)


@app.route('/product/<id>',methods=['GET'])
def getproduct(id):
    product=Product.querry.get(id)
    return product_schema.jsonify(product)


@app.route('/product/<id>',methods=['PUT'])
def updateproduct(id):
    product=Product.querry.get(id)
    name=request.json['name']
    description=request.json['description']
    qty=request.json['qty']
    price=request.json['price']
    
    product.name=name
    product.description=description
    product.qty=qty
    product.price=price
    
    
    db.session.commit()
    
    return product_schema.jsonify(new_product)

@app.route('/product/<id>',methods=['DELETE'])
def deletepro(id):
    product=Product.querry.get(id)
    db.session.delete(product)
    db.session.commit()

if __name__=='__main__':
    app.run(debug=True)
    
    