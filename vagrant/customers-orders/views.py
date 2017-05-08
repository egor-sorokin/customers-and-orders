from flask import Flask, render_template, request, redirect, url_for
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
    return render_template('customers/index.html')

@app.route('/customer/new')
def create_new_customer():
    return render_template('customers/create.html')


@app.route('/customer/<int:customer_id>/edit')
def edit_customer(customer_id):
    return render_template('customers/edit.html')


@app.route('/customer/<int:customer_id>/delete')
def delete_customer(customer_id):
    return render_template('customers/delete.html')


@app.route('/customer/<int:customer_id>')
@app.route('/customer/<int:customer_id>/orders')
def show_orders(customer_id):
    return render_template('orders/index.html')


@app.route('/customer/<int:customer_id>/orders/new')
def create_new_orders(customer_id):
    return render_template('orders/create.html')


@app.route('/customer/<int:customer_id>/orders/<int:orders_id>/edit')
def edit_orders(customer_id, orders_id):
    return render_template('orders/edit.html')


@app.route('/customer/<int:customer_id>/orders/<int:orders_id>/delete')
def delete_orders(customer_id, orders_id):
    return render_template('orders/delete.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
