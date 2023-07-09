# Search API README

This API has been built using the FastAPI framework and MYSQL database to handle the freelancers data. It can retrieve the list of freelancers available on the website and filter out the result based on specific parameters.

### Setup

To set up the project:

1. Clone the repository to your local machine.
2. Create a virtual environment for the project. You can use the following command: `python3 -m venv venv`
3. Activate the virtual environment. You can use the following command: `venv\Scripts\activate`

4. Install all the required dependencies. You can use the following command: `pip install -r requirements.txt`.
5. To set up MySQL, specify the appropriate MySQL server details in the code.
6. Set up `.env` file with enviornment details that is host, user, password and database name.
7. Modify the connection details `mysql.connector.connect` method with the host, user, password and database name accordingly.
   // this would be updated in the next update and values would be fetched from .env file only.
8. Run the API by executing the Python script. You can use the following command: `uvicorn main:app --reload`.
9. The API should now be running on `http://localhost:8000`.

## Endpoints

### Root endpoint

- URL: `/`
- Method: `GET`
- Description: Test endpoint to check if the API is running.
- Response: `{"message": "Hello World, API Endpoint testing"}`

### Get all freelancer

- URL: `/freelancers`
- Method: `GET`
- Description: Retrieve a list of all freelancers with pagination.
- Query Parameters:
  - page_number (optional): Page number to retrieve (default: 1).
  - page_size (optional): Number of freelancers per page (default: 10).
- Response: List of freelancers with pagination.

### Search Freelancer on basis of parameters

- URL: `/freelancers/search`
- Method: `GET`
- Description: Search for freelancers based on specific criteria with pagination.
- Query Parameters:
  - first_name (optional): First name of the freelancer.
  - last_name (optional): Last name of the freelancer.
  - email (optional): Email of the freelancer.
  - phone_number (optional): Phone number of the freelancer.
  - username (optional): Username of the freelancer.
  - insta_full_name (optional): Full name on Instagram of the freelancer.
  - follower_count (optional): Number of followers of the freelancer.
  - following_count (optional): Number of accounts the freelancer is following.
  - verified_status (optional): Verification status of the freelancer (True or False).
  - page_number (optional): Page number to retrieve (default: 1).
  - page_size (optional): Number of freelancers per page (default: 10).
- Response: List of freelancers matching the search criteria with pagination.

## Pagination

Pagination is enabled for the `/freelancers` and `/freelancers/search` endpoints. The `page_number` parameter represents the page number to retrieve, and the `page_size` parameter defines the number of freelancers per page. By default, the page number is set to 1, and the page size is set to 10.

## Error Handling

The API handles some error scenarios and returns appropriate HTTP status codes and error messages. For example, if there are no freelancers in the database, a `404 Not Found` response is returned. If the provided page number or page size is invalid (e.g., negative or zero), a `400 Bad Request` response is returned.

> Further information can be referred from `http://localhost:8000/docs` and `http://localhost:8000/redocs` these documentations are already created by Fastapi.

## Testing with Pytest

Pytest is used for testing API functionality. These are loacted in the `tests` directory. To run the test, use the following command: `pytest`.
Currently the tests cover following aspects:

- Connectivity: Tests the database connectivity function
- Endpoint Test: Tests the response and status code of endpoints
- Pagination: Tests the pagination functionality and displays the correct numberof result.
- All Freelancers: Tests the `/freelancers` endpoint and verifies that the correct data is returned.
- Specific Freelancer: Tests the `/freelancers/search` endpoint and verifies that the search functionality returns the expected results.

## Populating Dummy Data

The provided code in `randomdata.py` generates random data using the randominfo library and inserts it into the MySQL database. This step is optional and can be modified according to your needs. The code snippet creates a table named "users" in the database and inserts 1000 random records.

This has been created for testing load by Loading 1000 data points in the application and testing it.

> If you are facing issue with randominfo library, please refer `https://github.com/bmg02/randominfo/pull/4/commits`

Also the out.sql file is available for testing purposes created by above code ad can be imported to MySQL using `mysqlimport` command.


> The `coding_practices.txt` file shows the coding practice i have tried to follow. and the `improvements.txt` file shows possible improvements that can be incorporated

## CI/CD pipeline 

This repository has been set up with GitHub Actions and PM2 to enable continuous integration and continuous deployment (CI/CD) of the code. The code is deployed on an AWS EC2 instance and utilizes NGINX as the backend service to provide a seamless experience to users.