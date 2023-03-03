from curses import echo
from select import select
from turtle import delay
from venv import create
import docker_connect
from peewee import *
import os
import table_creation


class engine():
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
        self.connection_request= docker_connect.database_connect
        
    def connection_do_Exist(self):
        if(self.connection_request == True):
            print("connection established to docker SQL engine")
        
    
    def login_page(self):
        # username = str(input("USERNAME:"))
        # password = pwinput.pwinput(prompt='PASSWORD:',mask='*')
        os.system('clear')
        txt="|WELCOME|"
        print(txt.center(100))
        choise =  input("1. CREATE TABLE \n2. VIEW TABLE \n3. DELETE TABLE\n\n\nCHOISE:")
        if (choise == 1):
            table_creation.table.table_creator_fun()
            
            
if __name__=='__main__':
    
    obj=engine()
    obj.connection_do_Exist()
    obj.login_page()
