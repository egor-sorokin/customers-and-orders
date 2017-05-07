from flask import Flask, render_template, request, redirect
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Store, Good

app = Flask(__name__)

engine = create_engine('sqlite:///storegood.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/store')
def show_stores():
    return "Show all stores"


@app.route('/store/new')
def create_new_store():
    return "create a new store"


@app.route('/store/<int:store_id>/edit')
def edit_store(store_id):
    return "Edit the store with id = %s" % store_id


@app.route('/store/<int:store_id>/delete')
def delete_store(store_id):
    return "Delete the store with id = %s" % store_id


@app.route('/store/<int:store_id>')
@app.route('/store/<int:store_id>/goods')
def show_goods(store_id):
    return "Show all goods in the store with id = %s" % store_id


@app.route('/store/<int:store_id>/goods/new')
def create_new_goods(store_id):
    return "Create a new good in the store with id = %s" % store_id


@app.route('/store/<int:store_id>/goods/<int:goods_id>')
def edit_goods(store_id, goods_id):
    return "Edit the good with id = %s in the store with id = %s" % (goods_id, store_id)


@app.route('/store/<int:store_id>/goods/<int:goods_id>')
def delete_goods(store_id, goods_id):
    return "Delete the good with id = %s in the store with id = %s" % (goods_id, store_id)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
