

results = []

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print (fib(5))
print (fib(6))



fib(0) == 0
fib(1) == 1
fib(2) == fib(1) + fib(0)  # Se repite el cálculo de fib(1) y fib(0)
fib(3) == fib(2) + fib(1)  # Se repite el cálculo de fib(2) y fib(1)
fib(4) == fib(3) + fib(2)
fib(5) == fib(4) + fib(3)