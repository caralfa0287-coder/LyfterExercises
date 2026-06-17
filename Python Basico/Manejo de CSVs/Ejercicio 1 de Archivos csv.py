import csv

def save_videogames_file(path):
    while True:
        try:
            n = int(input("¿Cuántos video juegos desea ingresar?: "))
            if n <= 0: raise ValueError
            break
        except ValueError:
            print("Por favor, introduce un número válido mayor a 0.")
    with open(path, 'w', encoding='utf-8', newline='') as file:
        headers = ['Name', 'Genre', 'Developer', 'ESRB Classification']
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for i in range(n):
            print(f"\n--- Videogame {i+1} ---")
            name = input("Nombre: ")
            genre = input("Genero: ")
            developer = input("Desarrollador: ")
            esrb_classification = input("Clasificación ESRB: ")
            
            writer.writerow({'Name': name, 'Genre': genre, 'Developer': developer, 'ESRB Classification': esrb_classification})

    print(f"\nDatos guardados exitosamente en '{path}'")


save_videogames_file("New_videogames_file.csv")