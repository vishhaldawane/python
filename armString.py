# python 3 program
# to check whether the given number is armstrong or not
# without using power function
import string

n=153
s=n
b=len(str(n))
sum1=0
while n != 0:
	r = n % 10
	sum1 = sum1+(r**b)
	n = n//10
if s == sum1:
	print("The given number", s, "is armstrong number")
else:
	print("The given number", s, "is not armstrong number")

# This code is contributed by Gangarajula Laxmi

