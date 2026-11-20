n=int(input("enter the no. of terms you want to show of fibonacci series"))
a=0
b=1
for c in range(0,n):
  c=a+b
  print(c)
  a=b
  b=c
