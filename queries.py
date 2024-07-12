# pylint:disable=C0111,C0103

import sqlite3

def detailed_orders(db):
    '''return a list of all orders (order_id, customer.contact_name,
    employee.firstname) ordered by order_id'''
    query = """
    SELECT
	    Orders.OrderID,
	    Customers.ContactName,
	    Employees.FirstName
    FROM
	    Orders
    JOIN Customers ON Orders.CustomerID = Customers.CustomerID
    JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID
    """
    conn = sqlite3.connect('data/ecommerce.sqlite')
    db = conn.cursor()
    db.execute(query)
    results = db.fetchall()
    print(results)
    return results

def spent_per_customer(db):
    '''return the total amount spent per customer ordered by ascending total
    amount (to 2 decimal places)
    Exemple :
        Jean   |   100
        Marc   |   110
        Simon  |   432
        ...
    '''
    query = """
    SELECT
	Customers.ContactName,
	    SUM(OrderDetails.UnitPrice * OrderDetails.Quantity) AS Total_spent
    FROM
	    Customers
    JOIN OrderDetails On Orders.OrderID = OrderDetails.OrderID
    JOIN Orders ON Customers.CustomerID = Orders.CustomerID
    Group by Customers.ContactName
    Order by Total_spent Asc

    """
    conn = sqlite3.connect('data/ecommerce.sqlite')
    db = conn.cursor()
    db.execute(query)
    results = db.fetchall()
    print(results)
    return results

def best_employee(db):
    '''Implement the best_employee method to determine who’s the best employee!
    By “best employee”, we mean the one who sells the most.
    We expect the function to return a tuple like:
    ('FirstName', 'LastName', 6000 (the sum of all purchase)).
    The order of the information is irrelevant'''
    query = """
    SELECT
	Employees.FirstName,
	Employees.LastName,
	    SUM(OrderDetails.UnitPrice * OrderDetails.Quantity) AS Purchase_sum
    FROM Employees
    JOIN Orders ON Employees.EmployeeID = Orders.EmployeeID
    JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID
    Group By Employees.FirstName
    ORDER by Purchase_sum DESC
    """
    conn = sqlite3.connect('data/ecommerce.sqlite')
    db = conn.cursor()
    db.execute(query)
    results = db.fetchall()[0]
    print(results)
    return results


# conn = sqlite3.connect('data/ecommerce.sqlite')
# db = conn.cursor()
# best_employee(db)
# results = db.fetchall()
# print(results)


def orders_per_customer(db):
    '''Return a list of tuples where each tuple contains the contactName
    of the customer and the number of orders they made (contactName,
    number_of_orders). Order the list by ascending number of orders'''
    query = """
    SELECT Customers.ContactName,
	    Count(Orders.OrderID) AS order_count
    FROM Customers
    LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
    GROUP by Customers.ContactName
    ORDER By order_count ASC
    """
    conn = sqlite3.connect('data/ecommerce.sqlite')
    db = conn.cursor()
    db.execute(query)
    results = db.fetchall()
    print(results)
    return results
