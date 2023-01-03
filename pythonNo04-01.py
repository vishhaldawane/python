#!/usr/bin/python

def recursive_facto(n):
  if(n==0):
    return 1;
  return n*recursive_facto(n-1)

print(recursive_facto(6))
