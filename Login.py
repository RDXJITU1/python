from fastapi import FastAPI
from pydantic import BaseModel 
from fastapi.middleware.cors import CORSMiddleware
# import mysql.connector 
# from mysql.connector import Error

app = FastAPI()
# db_connect = {
#      "host":"localhost",
#      "user":"root",
#      "password":"Jitu@143",
#      "database":"zoo"
#}
# def connect():
#      try:
#           connect = mysql.connector.connect(**db_connect)
#           return connect
#      except Error as e:
#           print("data base not connect", e)

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["https://login-form-theta-rust.vercel.app/"],
    allow_credentials=True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)
class Logindata(BaseModel):
    userName : str
    password : str
@app.post("/register")
def login(user: Logindata):
    #  def insert(u_name,u_password):
    #       conn = connect()
    #       cur = conn.cursor()
    #       try:
    #            sql = "insert into user(u_name,u_password)values(%s, %s)"
    #            cur.execute(sql,(u_name,u_password))
    #            conn.commit()
    #            print("datastore succesfull")
    #       except:
    #            print("data cant store")
    #       finally:
            #    if conn:
            #         print("database Close")
            #         cur.close()
            #         conn.close()          
     print(user.userName)
     print(user.password)
    #  insert(user.userName, user.password)
     return{
          "msg":"success",
          "data":user
     }
     
