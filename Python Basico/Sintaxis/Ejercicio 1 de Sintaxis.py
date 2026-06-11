code = str("Hola")
code2 = str("Familia")
full_code = code + code2
print(full_code)

name = str("Juan")
age = int(30)
greeting = name + age
print(greeting)
# Este código dará un error porque no se puede concatenar una cadena (string) con un entero (integer).

weight = int(70)
scale = str("kilos")
message = weight + scale
print (message)
# Este código también dará un error por la misma razón que el anterior.:

list_of_prices = [10, 15, 20, 25]
list_of_products = ["zapatos", "camisa", "pantalon", "sombrero"]
price = list_of_prices + list_of_products
print(price)

weekly_weights = [94, 93, 92, 89, 86, 83, 80]
list_of_weights = scale + weekly_weights
print(list_of_weights)
# este código dará un error porque no se puede concatenar una cadena (string) con una lista (list).

price = int(25)
taxes = float (price * 0.09)
total_price = price + taxes
print (total_price)

pants_size= bool(True)
price = bool(True)
print (pants_size + price)
# ste código no dará error, pero el resultado será 2,
# ya que en Python, el valor booleano True se considera como 1 y False se considera como 0. 
# Por lo tanto, al sumar dos valores True, el resultado es 2.