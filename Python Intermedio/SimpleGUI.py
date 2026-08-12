import FreeSimpleGUI as sg

counter = 0

layout = [
    [sg.Text("Haz click en lo que quieras hacer")],
    [sg.Text(counter, key="-COUNTER-")],
    # Añadimos un segundo botón en la misma fila (misma lista)
    [sg.Button("Sumar"), sg.Button("Restar")],
]

window = sg.Window("Primer programa", layout)

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    elif event == "Sumar":
        counter += 1
    elif event == "Restar":
        counter -= 1

    # Refrescamos la pantalla con el nuevo valor
    window["-COUNTER-"].update(counter)

window.close()
