#!/usr/bin/python

print ( 'invoked')

def order(x) :
  n=0
  print ( 'order')
  while(x!=0):
    n = n + 1
    x = x // 10
  return n

def isArmstrong(x):
  print('is armstrong')
  n = order(x)
  temp = x
  sum1 = 0
  
  while( temp != 0 ) :
  	r = temp % 10
    	sum1 = sum1 + power (r,n)
    	temp = temp // 10
  return (sum1 ==  x)

  x = 153
  print('main')
  print (isArmstrong(x))
