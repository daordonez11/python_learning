max = int(raw_input("Escriba el limite para la serie:"))
fib1 = 1
fib2 = 2
total = ""
while fib1 < max:
    total += str(fib1)+" "
    new = fib1+fib2
    fib1 = fib2
    fib2 = new
print total
