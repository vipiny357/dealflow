from fastapi import FastAPI, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import mysql.connector

# initializing an instance of fastapi
app = FastAPI()

# Allowing cross origin resource sharing
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Establish a connection to MySQL database
# it should be stored in enviornment variable or as secret for testing purpose only it is kept openly
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="dealflow",

)

# creating a cursor object for executing queries on database
cursor = db.cursor()

# Implementation of pagination logic, getting initial value and last value to be returned back


def get_page_size(page_number: int, page_size: int):

    # Validate page_number and page_size
    if page_number <= 0 or page_size <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Page number and page size must be positive integers."
        )

    initial_value = (page_number - 1) * page_size
    last_value = initial_value + page_size

    return initial_value, last_value

#  Filtering the database to get the result based on search parameters


def filter_freelancers(search_params, initial_value: int, last_value: int):
    query = "SELECT * FROM users WHERE "
    conditions = []
    params = []

    #  creating the checking conditions and parameters for SQL query of database
    for key, value in search_params.items():
        if value is not None:
            conditions.append(f"{key} = %s")
            params.append(value)

    # appending the conditions and pagination to query and used if else for any fallback condition

    if conditions:
        query += " AND ".join(conditions)
        query += " LIMIT %s OFFSET %s"
        params.extend([last_value - initial_value, initial_value])
        cursor.execute(query, tuple(params))
    else:
        cursor.execute("SELECT * FROM users")
        params = (last_value - initial_value, initial_value)
        cursor.execute(query, params)

    results = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

    filtered_freelancers = []
    for row in results:
        freelancer = dict(zip(columns, row))
        filtered_freelancers.append(freelancer)

    return filtered_freelancers

#  test for root endpoint


@app.get("/")
async def root():
    return {"message": "Hello World, API Endpoint testing with CI/CD enabled."}

# Endpoint to return the list of all freelancers with pagination default of 10 values


@app.get("/freelancers")
async def show_freelancers(page_number: int = 1, page_size: int = 10):

    initial_value, last_value = get_page_size(page_number, page_size)

    query = "SELECT COUNT(*) FROM users"
    cursor.execute(query)
    data_length = cursor.fetchone()[0]

    # if there are no freelancers in database return 404
    # also handling all cases for page number and page sizes

    if data_length == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Currently there are no Freelancers."
        )
    elif data_length < page_size:
        query = "SELECT * FROM users LIMIT %s OFFSET %s"
        params = (data_length, initial_value)
        cursor.execute(query, params)
    else:
        query = "SELECT * FROM users LIMIT %s OFFSET %s"
        params = (page_size, initial_value)
        cursor.execute(query, params)

    results = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

    freelancers = []
    for row in results:
        freelancer = dict(zip(columns, row))
        freelancers.append(freelancer)

    return freelancers

# Endpoint to search for specific freelancers with some criteria and pagination is also enabled for the same


@app.get("/freelancers/search")
async def specific_freelancer(
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        email: Optional[str] = None,
        phone_number: Optional[str] = None,
        username: Optional[str] = None,
        insta_full_name: Optional[str] = None,
        follower_count: Optional[int] = None,
        following_count: Optional[int] = None,
        verified_status: Optional[bool] = None,
        page_number: int = 1,
        page_size: int = 10):

    search_params = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone_number": phone_number,
        "username": username,
        "insta_full_name": insta_full_name,
        "follower_count": follower_count,
        "following_count": following_count,
        "verified_status": verified_status
    }

    initial_value, last_value = get_page_size(page_number, page_size)

    # call to filter and find required search reults from database

    freelancers = filter_freelancers(search_params, initial_value, last_value)

    if len(freelancers) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no user with the given query parameters. Try again."
        )

    return freelancers
