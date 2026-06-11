my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#List Comprehension: Es la forma más rápida y limpia, generando una nueva lista filtrada.

peers = [n for n in my_list if n % 2 == 0]
print(peers)