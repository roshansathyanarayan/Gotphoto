#!/usr/bin/env python

import csv
import json
import sqlalchemy
import pandas as pd 
import datetime
import mysql.connector

mydb = mysql.connector.connect(
  host="database",
  user="codetest",
  password="swordfish")

mycursor = mydb.cursor()
print("Cursor Created")
 
mycursor.execute("USE codetest")  

  

#Query to join the tables
qr ="""SELECT places.country, count( distinct people.id) as people
FROM places LEFT JOIN people on places.county = people.place_of_birth
GROUP BY 1"""
mycursor.execute(qr)

 
# output the table to a JSON file
with open('/data/output.json', 'w') as json_file:

  rows = mycursor.fetchall()
  rows = [{'country': row[0], 'count': row[1]} for row in rows]
  json.dump(rows, json_file, separators=(',', ':'))

print("Completed the task. You can now view the output in Data->output.json ")
