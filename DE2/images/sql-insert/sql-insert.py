#!/usr/bin/env python

import csv
import json
import sqlalchemy
import pandas as pd 
import datetime
import mysql.connector



#Attempting a connection with SQL
try:
  engine = sqlalchemy.create_engine("mysql://codetest:swordfish@database/codetest")
  connection = engine.connect()
  metadata = sqlalchemy.MetaData()
   
  print("Database connection is working")   
except:
  ("Unable to connect to mysql, trying read csv from pandas")



mydb = mysql.connector.connect(
  host="database",
  user="codetest",
  password="swordfish")

mycursor = mydb.cursor()
print("Cursor Created")
 
mycursor.execute("USE codetest")  

 
print ("")
print ("")

print("Creating tables")
 

filenames = ['people.csv','places.csv'] 
for file in filenames:
  qr= """DROP TABLE IF EXISTS """ + str(file).replace(".csv","") 
  mycursor.execute(qr)
  df = pd.read_csv(file)
  a= "CREATE TABLE " + str(file).replace(".csv","") +" ( id int not null auto_increment,  "
  for col in df.columns:
    
    a=a+ str(col) + " varchar(80) default null, "
  a= a+ "primary key(id) )"
  qr = a
  mycursor.execute(qr)
  


 
#Inserting to People Table
with open('people.csv') as csv_file:
  reader = csv.reader(csv_file)
  next(reader)
  for row in reader: 
    r=row
    mycursor.execute('INSERT INTO people(given_name, family_name, date_of_birth, place_of_birth) VALUES("%s","%s","%s","%s")', r)

print("rows inserted for people.csv")



#Inserting to Places Table
with open('places.csv') as csv_file:
  reader = csv.reader(csv_file)
  next(reader)
  for row in reader: 
    r=row
    mycursor.execute('INSERT INTO places (city, county, country) VALUES("%s","%s","%s")', r)
 
print("rows inserted for places.csv")



mydb.commit()
