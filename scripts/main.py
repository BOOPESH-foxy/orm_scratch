from sqlite3 import DatabaseError
from turtle import delay
from venv import create
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import authentication
import table_creation
import pwinput
import os

class engine:
    
    def dict_get():
            global passcode 
            passcode = authentication.postgres.get('passcode')
            global hostname
            hostname =authentication.postgres.get('hostname')
            global username
            username=authentication.postgres.get('username')
            global port
            port=authentication.postgres.get('port')
            global database
            database=authentication.postgres.get('database')
            

    def get_engine():
        url="postgresql://{username}:{passcode}@{hostname}:{port}/{database}"
        engine_c=create_engine(url=url)
        if (engine_c):
            
                print(engine_c)
                print("connected to ORM Database..")
            
        else:
            create_engine(url=url)
            print("reconnecting")
            for i in range(3):
                
                print('.')
                delay(100)
                print(' _ ')
                
    
    # def access():
    #         username=str(input("Enter username :"))
    #         password=pwinput.pwinput(prompt="password :", mask="*")
    #         sql_q= 'SELECT isadmin FROM Authentication where username like %s and passcode like %s'
    #         data=(username,password)
    #         engine.execute(sql_q,data)
    #         isadmin=engine.fetchall()
        
    
    def login_page():
        # username = str(input("USERNAME:"))
        # password = pwinput.pwinput(prompt='PASSWORD:',mask='*')
        print("\n\n\t\t\t\t|WELCOME|")
        case=input("1 CREATE TABLE \n2 VIEW TABLE \n3 DELETE TABLE\nCHOISE:")
        return case
    
    
    def ready():
        engine.dict_get()
        engine.get_engine()
        print("Directing to login page")
        delay(100)
        os.system('clear')

    
    
    
if __name__=='__main__':
    engine.ready()
    case=engine.login_page()
    if case == 1:
        table_creation
    
