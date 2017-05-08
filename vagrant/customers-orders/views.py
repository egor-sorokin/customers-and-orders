from flask import Flask, render_template, request, redirect
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Customer, Order

app = Flask(__name__)

engine = create_engine('sqlite:///customerorder.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/customer')
def show_customers():
    return "Show all customers"


@app.route('/customer/new')
def create_new_customer():
    return "create a new customer"


@app.route('/customer/<int:customer_id>/edit')
def edit_customer(customer_id):
    return "Edit the customer with id = %s" % customer_id


@app.route('/customer/<int:customer_id>/delete')
def delete_customer(customer_id):
    return "Delete the customer with id = %s" % customer_id


@app.route('/customer/<int:customer_id>')
@app.route('/customer/<int:customer_id>/orders')
def show_orders(customer_id):
    return "Show all orders in the customer with id = %s" % customer_id


@app.route('/customer/<int:customer_id>/orders/new')
def create_new_orders(customer_id):
    return "Create a new order in the customer with id = %s" % customer_id


@app.route('/customer/<int:customer_id>/orders/<int:orders_id>')
def edit_orders(customer_id, orders_id):
    return "Edit the order with id = %s in the customer with id = %s" % (orders_id, customer_id)


@app.route('/customer/<int:customer_id>/orders/<int:orders_id>')
def delete_orders(customer_id, orders_id):
    return "Delete the order with id = %s in the customer with id = %s" % (orders_id, customer_id)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
