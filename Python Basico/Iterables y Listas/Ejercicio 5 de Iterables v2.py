user_list = []
counter = 10
print ("Ingrese 10 números:")
for i in range(counter):
    user_input = int(input("Número {}: ".format(i+1)))
    user_list.append(user_input)
max_value = max(user_list)
print(user_list, "El más alto fue: ", max_value)
