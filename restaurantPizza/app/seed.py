from app import db  
from app.models import Pizza, Restaurant

def seed_database():
    # Clearing existing data
    db.session.query(Restaurant).delete()
    db.session.query(Pizza).delete()
    db.session.commit()

    # Creating some restaurants
    restaurant1 = Restaurant(name='Dominion pizza', address='Good Italian, Ngong Road, 5th Avenue')
    restaurant2 = Restaurant(name='Pizza Hut', address='Westgate Mall, Mwanzi Road, Nrb 100')
    restaurant3 = Restaurant(name='Veggie Delight', address='789 Oak st, thika road')

    db.session.add_all([restaurant1, restaurant2, restaurant3])
    db.session.commit()

    # Creating some pizzas
    cheese_pizza = Pizza(name='Cheese Pizza', ingredients='Cheese, Tomato Sauce')
    pepperoni_pizza = Pizza(name='Pepperoni Pizza', ingredients='Pepperoni, Cheese, Tomato Sauce')
    veggie_pizza = Pizza(name='Veggie Pizza', ingredients='Mushrooms, Bell Peppers, Onions, Cheese, Tomato Sauce')

    db.session.add_all([cheese_pizza, pepperoni_pizza, veggie_pizza])
    db.session.commit()

    print("Database seeded to successfully.")

