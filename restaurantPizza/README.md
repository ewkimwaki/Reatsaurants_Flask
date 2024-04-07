# Pizza Restaurants

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
- open postman enter the route 
- select post method
- on the header add new key `Content-Type` and value `application/json`

## how it works
### __init__.py
- opens the database
- creates the flask context 
- calls the seed.py 
- calls the routes and models

### seed.py
- adds an inatance of values to the Restaurant and Pizza table

### routes.py
- creates various routes
1. GET/restaurant - Gets all rastaurants
2. GET/rrstaurants/id - gets a restauarant by ids
3. DELETE/restaurant/:id - deletes a restaurant by id
4. GET/pizza - gets all pizzas
5. POST/restaurant_pizza - adds a new restaurant pizza

### models.py
- creates tables 
- creates the relationship between Restaurant and pizza table
- Adds values to te tables
