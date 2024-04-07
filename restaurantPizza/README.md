# Pizza Restaurants
For this assessment, I will be working with a Pizza Restaurant domain.

my job was to build out a Flask API that adheres to the functionality described in the deliverables below.

I tested my endpoints as stated below

I started by running the Flask server and using Postman to make requests.
 

Models
My model has the following relationships:

The Restaurant has many Pizzas through RestaurantPizza
A Pizza has many Restaurants through RestaurantPizza
A RestaurantPizza belongs to a Restaurant and belongs to a Pizza
I started by creating the models and migrations from a provided data base table. 

Validations
I added validations to the RestaurantPizza model:

the pizzas had a price between 1 and 30

Add validations to the Restaurant Model:

the restaurant mode was required to have a name less than 50 words in length
and the name must be unique. 

## Dependencies
1. Python latest version
2. Flask
3. flask_migrate
4. sqlAlchemy
5. postman

## starting project 
- open the project directory
- open the terminal and run `python run.py`

## testing routes
- open the postman app
- key in the routes with various methods

## posting restaurant_pizzas
- Open Postman enter the route 
- select the post method
- on the header add the new key `Content-Type` and value `application/json`

## how it works
### __init__.py
- opens the database
- creates the flask context 
- calls the seed.py 
- calls the routes and models

### seed.py
- adds an instance of values to the Restaurant and Pizza table

### routes.py
- creates various routes
1. GET/restaurant - Gets all restaurants
2. GET/rrstaurants/id - gets a restauarant by ids
3. DELETE/restaurant/:id - deletes a restaurant by id
4. GET/pizza - gets all pizzas
5. POST/restaurant_pizza - adds a new restaurant pizza

### models.py
- creates tables 
- creates the relationship between the Restaurant and the pizza table
- Adds values to the tables
