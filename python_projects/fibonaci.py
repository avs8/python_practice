# Fibonacci series
# first check if number is less then 0, 1

def fib(num):
    if num == 0 or num == 1:
        return num
    else:
        return fib(num-1) + fib(num-2)

for i in range(1, 10):
    print fib(i)