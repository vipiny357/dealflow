import mysql.connector
from randominfo import Person
import random
from dotenv import load_dotenv
import sys
import os

load_dotenv()

# using .env file to get secret values
host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
database=os.getenv("database")

# Disable printing to console
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Enable printing to console
def enablePrint():
    sys.stdout = sys.__stdout__


# Establish a connection to the MySQL database
db = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)
cursor = db.cursor()

# Create a table named "users" in the database
create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(100),
    phone_number VARCHAR(20),
    username VARCHAR(50),
    insta_full_name VARCHAR(100),
    follower_count INT,
    following_count INT,
    verified_status BOOLEAN
)
"""
cursor.execute(create_table_query)

# Generate random data using the randominfo library and insert it into the table


for _ in range(10):
    blockPrint()
    ri = Person()
    first_name = ri.first_name
    last_name = ri.last_name
    email = ri.email
    phone_number = ri.phone
    username = first_name+" "+last_name
    insta_full_name = first_name+random.choice(["_", "."])+last_name+str(random.randint(0,1000))
    follower_count = random.randint(0, 10000)
    following_count = random.randint(0, 10000)
    verified_status = random.choice([True, False])
    enablePrint()
    insert_query = """
    INSERT INTO users
    (first_name, last_name, email, phone_number, username, insta_full_name, follower_count, following_count, verified_status)
    VALUES
    (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    insert_params = (first_name, last_name, email, phone_number, username,
                     insta_full_name, follower_count, following_count, verified_status)
    cursor.execute(insert_query, insert_params)

# Commit the changes and close the database connection
db.commit()
db.close()
