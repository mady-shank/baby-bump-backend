#import mysql.connector
import os
from os import getenv
from dotenv import load_dotenv
import dj_database_url


#calling the .env file
load_dotenv()
password = os.getenv("password_db")

#connect to server
#db = mysql.connector.connect(
#    host = "127.0.0.1",
#    #port = "5000",
#    #host = "localhost",
#    user = "root",
#    passwd = password,
#    database = "babybump"
)

#set cursor object
#mycursor = db.cursor()

# create database and tables if they don't already exist
#mycursor.execute("CREATE DATABASE IF NOT EXISTS babybump DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;".format("babybump"));
#mycursor.execute("CREATE TABLE IF NOT EXISTS User (username VARCHAR(25), password VARCHAR(25), email VARCHAR(25), role VARCHAR(25), id int PRIMARY KEY AUTO_INCREMENT)")
