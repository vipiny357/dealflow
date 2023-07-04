import mysql.connector
def test_database_connection():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="dealflow"
    )
    assert db.is_connected()  
    db.close()  
    # Test case to check if connection is successfull
