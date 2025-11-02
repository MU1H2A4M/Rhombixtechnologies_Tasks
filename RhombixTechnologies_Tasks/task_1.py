def fib(a):
    if (a <= 1):
      return a
    else:
        return fib(a-1)+fib(a-2)

n=int(input("enter the number "))
for i in range(0,n+1):
    print(fib(i))
