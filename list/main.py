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

# Metodo remove

motorcycles_remove = ['honda', 'yamaha', 'suzuki']

print(motorcycles_remove)

too_expensive = 'suzuki'

motorcycles_remove.remove(too_expensive)

print(motorcycles_remove)

print(f"\nA {too_expensive.title()}")

# 3.4 Lista de convidados

convidados = ['Matheus', 'Silva', 'Helder']
print(convidados)

# 3.5 Adicionando outro convidado
convidados[0] = 'Homer'
print(convidados)

# 3.6 Mais Convidados
convidados.insert(0, 'Thanos')
convidados.insert(1, 'Tony')
convidados.append('Hulk')

print(convidados)

# 3.5 Reduzindo a lista de convidados

thanos = convidados.pop(0)
homer = convidados.pop(1)
helder = convidados.pop(2)

print(f"Lamentamos por não poder convidar o {thanos}")
print(f"Lamentamos por não poder convidar o {homer}")
print(f"Lamentamos por não poder convidar o {helder}")

print(convidados)

del convidados[0]
del convidados[0]
del convidados[0]

print(convidados)
