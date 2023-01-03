#!/usr/bin/python
data = data2=""

with open('file1.txt') as fp:
   data = fp.read();

with open('file2.txt') as fp:
   data2 = fp.read();

data +="\n"
data += data2

with open('file3.txt','w') as fp:
  fp.write(data)

print ('--------')

str=str2=""

with open('file1.txt') as fp:
   str = fp.read();


with open('file2.txt') as fp:
   str2 = fp.read();

str += "\n"
str += str2

with open('str3.txt','w') as fp:
   fp.write(str)

