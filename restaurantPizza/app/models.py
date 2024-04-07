from app import db

# Association table for Restaurant and Pizza
restaurant_pizza = db.Table(
    'restaurant_pizza',
    db.Column('restaurant_id', db.Integer, db.ForeignKey('restaurant.id'), primary_key=True),
    db.Column('pizza_id', db.Integer, db.ForeignKey('pizza.id'), primary_key=True),
    db.Column('price', db.Float, nullable=False),
    db.CheckConstraint('price >= 1 AND price <= 30', name='check_price_range')
)
#resataurant table model
class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(255), nullable=False)
    pizzas = db.relationship('Pizza', secondary=restaurant_pizza, backref=db.backref('restaurants', lazy='dynamic'))

#pizza table model
class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ingredients = db.Column(db.String(255), nullable=False)

