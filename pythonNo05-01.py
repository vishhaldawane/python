#!/usr/bin/python

import sqlite3

cnt = sqlite3.connect('backup.dp1')
cnt.execute('''CREATE TABLE gfg(
NAME TEXT,
POINTS INTEGER,
ACCURACY REAL);''')
  
cnt.execute('''INSERT INTO emp2 VALUES(
'Count Inversion',20,80.5);''')
  
# insert in different order
cnt.execute('''INSERT INTO emp2 (ACCURACY, POINTS, NAME) VALUES(
90.5, 15, 'Kadanes Algo');''')
  
cnt.execute('''INSERT INTO emp2 (NAME, ACCURACY, POINTS) VALUES(
'REVERSE STR', 100, 5);''')
  
# commit changes to the database
cnt.commit()

