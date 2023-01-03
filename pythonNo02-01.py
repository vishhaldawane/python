#!/usr/bin/python
principal = float(input('enter amount : '))
numberOfYears= float(input('enter years : '))
rateOfInterest = float(input('enter rate : '))

simpleInterest = (principal * numberOfYears * rateOfInterest) / 100

print ('simple interest : %f'%(simpleInterest))

print ('------')

compoundInterest = principal * ( (1+rateOfInterest/100)**numberOfYears-1)

print ('compound interest : %f'%(compoundInterest))

print ('-------')

p=float(input('enter p '))
n=float(input('enter n '))
r=float(input('enter r '))
si=(p*n*r)/100
print('simple interest is as : %f'%(si))

ci=p*((1+r/100)**n-1)

print('ci %f'%(ci))


ci1=p*((1+r/100)**n-1)

print(ci1)

