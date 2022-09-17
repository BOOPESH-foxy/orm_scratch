import mysql.connector

import docker_authentication

database_connect = mysql.connector.connect(
    host = docker_authentication.docker.get('host'),
    user =docker_authentication.docker.get('username') ,
    password = docker_authentication.docker.get('passcode')
)

# Printing the connection object