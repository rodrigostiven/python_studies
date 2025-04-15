# 3.1 Nomes

names = ['Helder', 'Luis', 'Ronaldo']

print(names[0])
print(names[1])
print(names[2])

#3.2 Cumprimentos

for name in names:
  message = f"Olá, meu nome é {name}."
  print(message)

#3.3

vehicle = ['moto', 'carro']

message = f"Eu tenho uma {vehicle[0]} e um {vehicle[1]}"

print(message)

# Metodo del para remover

motorcycles = ['honda', 'yamaha', 'suzuki']

print(motorcycles)

del motorcycles[0]
print(motorcycles)

# Metodo pop para remover

print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# Exemplo de uso real do metodo pop

last_owned = motorcycles.pop()
print(f"A ultima moto que saiu do estoque foi a {last_owned.title()}")

motorcycles2 = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles2.pop(0)

print(f"A primeira moto vendida foi a {first_owned.title()}.")