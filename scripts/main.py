from curses import echo
from sqlite3 import DatabaseError
from turtle import delay
from venv import create
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import docker_authentication
import docker_connect
import pwinput
import os

class engine:
    # def __init__(self):
    #     engine.dict_get()
    #     self.engine_var = engine.get_engine()
    #     self.case = engine.login_page()
    #     print("Directing to login page")
    #     delay(100)
    #     os.system('clear')
    
    # def dict_get():
    #         global passcode 
    #         passcode = authentication.postgres.get('passcode')
    #         global hostname
    #         hostname =authentication.postgres.get('hostname')
    #         global username
    #         username=authentication.postgres.get('username')
    #         global port
    #         port=authentication.postgres.get('port')
    #         global database
    #         database=authentication.postgres.get('database')
            

    # def get_engine():
    #     url_ = "postgresql://{username}:{passcode}@{hostname}:{port}/{database}"
    #     if engine := create_engine(url=url_, echo=True):
    #         print(engine)
    #     else:
    #         create_engine(engine)
    #         print("reconnecting")
    #         for _ in range(3):
    #             print('.')
    #             delay(100)
    #             print(' _ ')
    #     return url_
                
    
    # def access():
    #         username=str(input("Enter username :"))
    #         password=pwinput.pwinput(prompt="password :", mask="*")
    #         sql_q= 'SELECT isadmin FROM Authentication where username like %s and passcode like %s'
    #         data=(username,password)
    #         engine.execute(sql_q,data)
    #         isadmin=engine.fetchall()
    
    
    def __init__(self):
        self.connecction_request=docker_connect.database_connect
        
    def connection_do_Exist(self):
        if(self.connecction_request == 1):
            print("connection established to docker SQL engine")
        
    
    def login_page():
        # username = str(input("USERNAME:"))
        # password = pwinput.pwinput(prompt='PASSWORD:',mask='*')
        print("\n\n\t\t\t\t|WELCOME|")
        return input("1 CREATE TABLE \n2 VIEW TABLE \n3 DELETE TABLE\nCHOISE:")
    
    
    
    
if __name__=='__main__':
    
    def execution():
        obj = engine.__init__()
        obj.connection_do_Exist()
        obj.login_page()
    
    # case=engine.login_page()
    # if case == 1:
    #     table_creation
    
