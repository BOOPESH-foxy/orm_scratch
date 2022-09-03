from sqlite3 import DatabaseError
from turtle import delay
from venv import create
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import authentication
import pwinput
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
        
        url=f"postgresql://{username}:{passcode}@{hostname}:{port}/{database}"
        engine_c=create_engine(url=url)
        if create_engine(url=url):
            {
                print("connected to ORM Database..")
            }
        else:
            create_engine(url=url)
            print("reconnecting")
            i=0;
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
        
    
    # def login_page():
    #     username = str(input("USERNAME:"))
    #     password = pwinput.pwinput(prompt='PASSWORD:',mask='*')

    def ready():
        engine.dict_get()
        a=engine.get_engine()
        engine.login_page()
    
    
    
if __name__=='__main__':
    engine.ready()
    
