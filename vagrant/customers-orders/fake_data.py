from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Customer, Order

engine = create_engine('sqlite:///customerorder.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# First customer and orders
customer = Customer(name="Tony Montana")
session.add(customer)
session.commit()

order = Order(name="M4", description="Weapon, Automatic firearm", manufacturer="China corporation", price="$107.50",
              customer=customer)
session.add(order)
session.commit()

order = Order(name="AWP", description="Sniper rifle", manufacturer="Japan Inc", price="$200.99",
              customer=customer)
session.add(order)
session.commit()

order = Order(name="Browning M2", description="Heavy machine gun", manufacturer="U.S. army", price="$500.50",
              customer=customer)
session.add(order)
session.commit()


# Second customer and orders
customer = Customer(name="Steve Doe")
session.add(customer)
session.commit()

order1 = Order(name="Chickens", description="Raw chickens", price="$17.99", manufacturer="OOO India",
               customer=customer)
session.add(order1)
session.commit()

order2 = Order(name="Lorem ipsum", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit.", price="$25",
               manufacturer="Ipsum factory", customer=customer)

session.add(order2)
session.commit()

order3 = Order(name="Maple apple syrup", description="Maple apple syrup", price="$1", manufacturer="Maple country",
               customer=customer)
session.add(order3)
session.commit()


# Third customer and orders
customer = Customer(name="John Stalin")
session.add(customer)
session.commit()

order = Order(name="Big ben", description="Big ben 5m toy", price="$13.95", manufacturer="Island GmbH",
              customer=customer)
session.add(order)
session.commit()

order = Order(name="Tank", description="Prototype of the green tank", price="$4.95", manufacturer="OOO Russian",
              customer=customer)

session.add(order)
session.commit()

order = Order(name="Spaghetti", description="Spaghetti with some incredible tomato sauce made by mom", price="$6.95",
              manufacturer="Mom LLC", customer=customer)

session.add(order)
session.commit()

print "Fake data has been successfully added!"
