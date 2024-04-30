import sys
try:
   x = int(input("x: "))

   y = int(input("y: "))
except:
    ValueError: print("Value should be int")
    sys.exit(1)

try:
   result=x/y
except:
    ZeroDivisionError: print("Cannot divide by zero")
    sys.exit(1)

print (f"{x} /{y} = {result}")