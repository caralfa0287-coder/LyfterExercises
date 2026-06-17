#Cree un programa que lea nombres de canciones de un archivo (línea por línea) 
# y guarde en otro archivo los mismos nombres ordenados alfabéticamente.

def open_songs_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for number, line in enumerate(lines, start=1):
            print(f"Line {number}: {line.strip()}")
    return lines

def sorted_and_create_file(lines, path):
    lines.sort(key=str.lower)
    with open(path, 'w', encoding='utf-8') as f:
        for song in lines:
            f.write(song.strip() + '\n')

def main():
    songs = open_songs_file('Song names.txt')
    sorted_and_create_file(songs, 'New song list.txt')  

if __name__ == "__main__":
    main()  