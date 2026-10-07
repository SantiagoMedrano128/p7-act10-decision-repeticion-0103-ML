# Santiago Medrano 0103
# Machine Learning
print("+-+-+-+-+-+-Condicionales-+-+-+-+-+-+")
print("Ejemplo 1")
a = 33
b = 200
if b > a:
  print("b es mayor que a")
print("Ejemplo 2")
number = 15
if number > 0:
  print("El numero es positivo")

print("+-+-+-+-+-+-if elif-+-+-+-+-+-+")
print("Ejemplo 1")
a = 33
b = 33
if b > a:
  print("b es mayor que a")
elif a == b:
  print("a y b son igualex")

print("Ejemplo 2")
age = 25

if age < 13:
  print("eres un niño")
elif age < 20:
  print("eres un adolescente")
elif age < 65:
  print("eres un adulto")
elif age >= 65:
  print("eres un adulto mayor")

print("+-+-+-+-+-+-if else-+-+-+-+-+-+")
print("Ejemplo 1")
a = 200
b = 33
if b > a:
  print("b es mayor que a")
elif a == b:
  print("a y b son iguales")
else:
  print("a es mayor que b")

print("Ejemplo 2")
a = 200
b = 33
if b > a:
  print("b es mayor que a")
else:
  print("b no es mayor que a")

print("+-+-+-+-+-+-for loops-+-+-+-+-+-+")
print("Ejemplo 1")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

print("Ejemplo 2")
for x in "banana":
  print(x)

print("+-+-+-+-+-+-while loops-+-+-+-+-+-+")
print("ejemplo 1")

i = 1
while i < 6:
  print(i)
  i += 1
print("Ejemplo 2")
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

print("Santiago Medrano NC 0103")
