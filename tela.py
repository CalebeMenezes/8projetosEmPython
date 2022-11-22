import PySimpleGUI as sg

class TelaPython:
    sg.theme('purple')
    def __init__(self):
        #layout 
        layout =[
            [sg.Text('Login'),sg.Input()],
            [sg.Text('senha'),sg.Input()],
            [sg.Button('ok'),sg.Button('recuperar senha')]

        ]
        #janela
        janela = sg.Window('Dados do ususario').layout(layout)
        #extrair dados
        self.button, self.values = janela.Read() 

    def Iniciar(self):
        print(self.values)

tela = TelaPython()      
tela.Iniciar()

