import PySimpleGUI as sg
import os.path

# Primeiro o layout da janela em 2 colunas  
file_list_column = [
    [
        sg.Text('Image folder')
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40,20), key='-FILE LIST-'
        )
    ],
]
# Por enquanto só mostrará o nome do arquivo que foi escolhido
image_viewer_column = [
    [sg.text('Escolha uma imagem da lista à esquerda:')],
    [sg.text(size=(40,1)key='-TOUT-')],
    [sg.image(key='-IMAGE-')],
]
# ----- Full layout -----
layout = [
    [
        sg.Column(file_list_column),
        sg.VSeparator(),
        sg.Column(image_viewer_column),
    ]
]
window = sg.window('image Viewer',layout)
#loop de evento
while True:
    event, values = window.read()
    if event == "exit" or event == sg.WINDOW_CLOSED:
        break
# O nome da pasta foi preenchido, faça uma lista dos arquivos na pasta
if event == '-FOLDER-':
    folder = values['-FOLDER-']
    try:
        # Obtenha uma lista de arquivos na pasta
        file_list = os.listdir(folder)
    except:
        file_list = []

    fnames = [
        f
        for f in file_list
        if os.path.isfile(os.path.join(folder, f))
        and f.lower(),endswith(('.png, .gif'))
    ]
    window['-FILE LIST-'].update(fnames)
elif event == '-FILE LIST-':  # Um arquivo foi escolhido na caixa de listagem
    try:
        filename = os.path.join(
            values['-FOLDER-'], values['-FILE LIST-'][0]
        )
        window['-TOUT-'].update(filename)
        window['-IMAGE-'].update(filename=filename)
    except:
        pass
window.close()