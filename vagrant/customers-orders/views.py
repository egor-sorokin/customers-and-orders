from flask import Flask, render_template, request, redirect, url_for, abort
from sqlalchemy import exc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Customer, Order

app = Flask(__name__)

engine = create_engine('sqlite:///customerorder.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/', methods=['GET'])
@app.route('/customers', methods=['GET'])
def show_customers():
    customers = session.query(Customer).all()
    return render_template('customers/index.html', customers=customers)


@app.route('/customers/new', methods=['GET', 'POST'])
def create_new_customer():
    if request.method == 'POST':
        try:
            newCustomer = Customer(name=request.form['name'])
            session.add(newCustomer)
            session.commit()

        except exc.SQLAlchemyError:
            print "Customer can't be created, database error"

        return redirect(url_for('show_customers'))
    else:
        return render_template('customers/create.html')


@app.route('/customers/<int:customer_id>/edit', methods=['GET', 'POST'])
def edit_customer(customer_id):
    if request.method == 'POST':
        try:
            customer = session.query(Customer).filter_by(id=customer_id).one()

            if request.form['name']:
                customer.name = request.form['name']

            session.add(customer)
            session.commit()

        except exc.SQLAlchemyError:
            print "Customer can't be modified, database error"

        return redirect(url_for('show_customers'))
    else:
        return render_template('customers/edit.html', customer_id=customer_id)


@app.route('/customers/<int:customer_id>/delete', methods=['GET', 'POST'])
def delete_customer(customer_id):
    if request.method == 'POST':
        try:
            customer = session.query(Customer).filter_by(id=customer_id).one()
            session.delete(customer)
            session.commit()
        except exc.SQLAlchemyError:
            print "Customer can't be deleted, database error"

        return redirect(url_for('show_customers'))
    else:
        return render_template('customers/delete.html', customer_id=customer_id)


@app.route('/customers/<int:customer_id>', methods=['GET'])
@app.route('/customers/<int:customer_id>/orders', methods=['GET'])
def show_orders(customer_id):
    try:
        orders = session.query(Order).filter_by(customer_id=customer_id)
        return render_template('orders/index.html', orders=orders, customer_id=customer_id)
    except exc.SQLAlchemyError:
        print "Orders of this customer can't be found, database error"


@app.route('/customers/<int:customer_id>/orders/new', methods=['GET', 'POST'])
def create_new_order(customer_id):
    if request.method == 'POST':
        try:
            if request.form['price']:
                price = request.form['price']
                if price[:1] != '$':
                    price = '$' + price
                else:
                    price = price
            else:
                price = ''

            newOrder = Order(name=request.form['name'], description=request.form['description'],
                             manufacturer=request.form['manufacturer'], price=price,
                             customer_id=customer_id)
            session.add(newOrder)
            session.commit()

        except exc.SQLAlchemyError:
            print "Order can't be created, database error"

        return redirect(url_for('show_orders', customer_id=customer_id))
    else:
        return render_template('orders/create.html', customer_id=customer_id)


@app.route('/customers/<int:customer_id>/orders/<int:order_id>/edit', methods=['GET', 'POST'])
def edit_order(customer_id, order_id):
    if request.method == 'POST':
        try:
            order = session.query(Order).filter_by(id=order_id, customer_id=customer_id).one()

            if request.form['name']:
                order.name = request.form['name']

            if request.form['description']:
                order.description = request.form['description']

            if request.form['manufacturer']:
                order.manufacturer = request.form['manufacturer']

            if request.form['price']:
                price = request.form['price']
                if price[:1] != '$':
                    order.price = '$' + price
                else:
                    order.price = price

            session.add(order)
            session.commit()

        except exc.SQLAlchemyError:
            print "Order can't be modified, database error"

        return redirect(url_for('show_orders', customer_id=customer_id))
    else:
        return render_template('orders/edit.html', customer_id=customer_id, order_id=order_id)


@app.route('/customers/<int:customer_id>/orders/<int:order_id>/delete', methods=['GET', 'POST'])
def delete_order(customer_id, order_id):
    if request.method == 'POST':
        try:
            order = session.query(Order).filter_by(id=order_id, customer_id=customer_id).one()
            session.delete(order)
            session.commit()

        except exc.SQLAlchemyError:
            print "Order can't be deleted, database error"

        return redirect(url_for('show_orders', customer_id=customer_id))
    else:
        return render_template('orders/delete.html', customer_id=customer_id, order_id=order_id)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
