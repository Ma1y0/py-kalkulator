import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [[sg.Text('Kalkulačka')],
          [sg.Input(), sg.Button('+'), sg.Button('-'), sg.Button('*'), sg.Button('/'), sg.Input()],
          [sg.Button('OK'), sg.Button('Cancel')]]

window = sg.Window('Hello World', layout)

while True:
    event, values = window.read()

    if event == '+':
        print(float(values[0]) + float(values[1]))

    if event == '-':
        print(float(values[0]) - float(values[1]))

    if event == '*':
        print(float(values[0]) * float(values[1]))

    if event == '/':
        print(float(values[0]) / float(values[1]))

    if event == sg.WIN_CLOSED or event == 'Cancel':
        break


window.close()
