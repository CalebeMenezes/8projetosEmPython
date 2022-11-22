import random
import PySimpleGUI as sg
import os

class PassGen:
    def __init__(self):
        #layout
        sg.theme('purple')
        layout = [
            [sg.Text('site',size=(10,1)),sg.Input(key='site',size=(20,1))],
            [sg.Text('Usuario',size=(10,1)),sg.Input(key='Usuario',size=(20,1))],
            [sg.Text('Quantidade de caracteres'),sg.Combo(values=list(range(31)),key='Total_chars',default_value=1,size=(3,1))],
            [sg.Output(size=(32, 5))],
            [sg.Button('Gerar senha')]
        ]
    #declarar janela
        self.janela = sg.Window('Password generator',layout)

    def Iniciar(self):
        while True:
            evento,valores = self.janela.read() 
            if evento == sg.WIN_CLOSED:
                break
            if evento == 'Gerar senha':
                Nova_Senha = self.Gerar_Senha(valores)
                print(Nova_Senha)
                self.Salvar_Senha(Nova_Senha, valores)
    def Gerar_Senha(self, valores):
        Char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%¨&*'
        Chars = random.choices(Char_list,k=int(valores['Total_chars']))
        New_Pass = ''.join(Chars)
        return New_Pass
    def Salvar_Senha(self,Nova_Senha,valores):
        with open('senha.txt','a',newline='') as arquivo:
            arquivo.write(
                f"site: {valores['site']}, Usuario {valores['Usuario']}, nova senha {Nova_Senha}")
        print('arquivo salvo')

        
 
gen = PassGen()
gen.Iniciar()
