import mysql.connector
import authentication

database_connect = mysql.connector.connect(
    host = authentication.docker.get('host'),
    user =authentication.docker.get('username') ,
    password = authentication.docker.get('passcode')
)
# Printing the connection object