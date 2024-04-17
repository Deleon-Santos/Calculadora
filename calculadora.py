"""Estou desenvolvendo uma calculadora simplificada que possa executar corretamente as funcionalidades basicas do dia-a-dia"""


import PySimpleGUI as sg

#Neste bloco escolhemos o tema, visor, botões e layout da calculadora

sg.LOOK_AND_FEEL_TABLE['novoTheme'] = {'BACKGROUND': '#A9A9A9', 
                                    'TEXT': '#000000', 
                                    'INPUT': '#DCDCDC', 
                                    'TEXT_INPUT': '#000000', 
                                    'SCROLL': '#99CC99', 
                                    'BUTTON': ('#000000', '#C0C0C0'), 
                                    'PROGRESS': ('#D1826B', '#CC8019'), 
                                    'BORDER': 5, 'SLIDER_DEPTH': 5,  
                                    'PROGRESS_DEPTH': 6, } 
sg.theme('novoTheme') 

visor  =[[sg.Input("0", size=(28, 1), font=("Any", 18, "bold"),background_color="lightYellow", key="-manter-", justification='right'),sg.P(), sg.Button("Sair",size=(6,1),button_color="red",font=("Any",14))],
        [sg.Input("0", size=(13, 1), font=("Any", 49, "bold"), key="-out-", justification='right')],]

l_numeros=[[sg.Button("7", size=(7,3), key="7", font="bold",), sg.Button("8", size=(7, 3), key="8", font="bold"), sg.Button("9", size=(7, 3), key="9", font="bold")],
    [sg.Button("4", size=(7, 3), key="4", font="bold"), sg.Button("5", size=(7, 3), key="5", font="bold"), sg.Button("6", size=(7, 3), key="6", font="bold")],
    [sg.Button("1", size=(7, 3), key="1", font="bold"), sg.Button("2", size=(7, 3), key="2", font="bold"), sg.Button("3", size=(7, 3), key="3", font="bold")],
    [sg.Button("+/-", size=(7, 3), key="+/-", font="bold",button_color="lightBlue",), sg.Button("0", size=(7, 3), key="0", font="bold"), sg.Button(",", size=(7, 3), key=".", font="bold",button_color="lightBlue",)],]

operadores_1 =[[sg.Button("<", size=(5, 3), font="bold",button_color="#ECA138", key="<")],
    [sg.Button("x", size=(5, 3), font="bold",button_color="lightBlue", key="*")],
    [sg.Button("-", size=(5, 3), font="bold",button_color="lightBlue", key="-")],
    [sg.Button("+", size=(5, 3), font="bold",button_color="lightBlue", key="+")],]

operadores_2 =[[sg.Button("C", size=(5, 3), font="bold",button_color="red", key="c")],
    [sg.Button("/", size=(5, 3), font="bold",button_color="lightBlue", key="/")],
    [sg.Button("%", size=(5, 3), font="bold",button_color="lightBlue", key="%")],
    [sg.Button("=", size=(5, 3), font="bold",button_color="#ECA138", key="=")],]

layout_calculadora =[[sg.Frame("", visor)],
                    [sg.Frame("", l_numeros), sg.Col(operadores_1), sg.Col(operadores_2)],]
                    
tab_layout1 = [[sg.Frame("",layout_calculadora)], ]

menu_botao = [["Sobre",['Sobre']]]
janela = [
[sg.MenuBar(menu_botao)],
[sg.P(),sg.Text("NOVA CALCULADORA", justification='center', font=("Any", 20, "bold"), relief='flat'),sg.P()],
[sg.TabGroup([[sg.Tab("Calculadora", tab_layout1)],])],
]

#Inicio do programa, declaração das variaveis     
window = sg.Window("CALCULADORA SIMPLIFICADA", janela, resizable=True)
l_operadores = ["+", "-", "*","/"]
historico=""
display = ""
operador = ""
l_numeros = [str(i) for i in range(0, 10)]#uma laço para gerar "0 a 9 convertidos em str

while True: #laço principal
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, "Sair"):
        break
    #se o evento esta em l_numeros e nao foi registrado um operador faça...  
    if event in l_numeros:
        if not operador:
            display += event
            window["-out-"].update(display)
        else:
            display+=event
            historico+=event
            window["-out-"].update(display)

    elif event in l_operadores:
        numero_1=display
        
        if event in display[:-1]: #se o operador esta na ultima posição do display
            display = display[:-1] + event  #atualiza o operador
            operador=event
            window["-out-"].update(display)
            
        else:
            display+= event
            operador=event
            window["-out-"].update(display)

    elif event == "=":
        if operador:
            display+=event
            numero_2=historico
            window["-manter-"].update(display)
            
            if operador == "+":
                resp =str(float (numero_1)+ float(numero_2))
            elif operador == "-":
                resp =str(float (numero_1)- float(numero_2))
            elif operador == "*":
                resp =str(float (numero_1)* float(numero_2))
            elif operador == "/":
                if numero_2 != 0:
                    resp =str(float (numero_1)/ float(numero_2))
                else:
                    resp = "Erro"
            display = (f"{resp}".replace(".0",""))# remove o .0 do display
            window["-out-"].update(display)
            operador = ""
            historico=""
            numero_1=display #o numero_ deve receber o resto da operação
            numero_2=''
        
    elif event=="<":
        if len(display):
            display=display[:-1] #Apaga a ultima posição do display 
            historico=historico[:-1]
            window["-out-"].update(display)
            
    elif event == "c":
        display = ""
        operador = ""
        historico=""
        window["-out-"].update("0") #Limpa os valores no display

    elif event == "+/-":
        if display and display[0] != '-':# ler o valor de dispay na posição[0] para converter em negativo
            display = '-' + display
        elif display and display[0] == '-':
            display = display[1:]
            historico=display
        window["-out-"].update(display)

    elif event==".":
        if "." not in display:#Ler o display para adicionar um "."
            display += "."
            window["-out-"].update(display)

    elif event == "%":
        if operador:
            display+=event
            numero_2 = float(numero_1) * (float(historico) / 100)  # Convertendo o segundo numero no display para porcentagem
            window["-manter-"].update(display)
            if operador == "+":
                resp = str(float(numero_1) + numero_2)
            elif operador == "-":
                resp = str(float(numero_1) - numero_2)
            elif operador == "*":
                resp = str(float(numero_1) * numero_2)
            elif operador == "/":
                if numero_2 != 0:
                    resp =str(float (numero_1)+ float(numero_2))
                else:
                    display = "Erro"
            display = (f"{resp}".replace(".0",""))
            window["-out-"].update(display)
            numero_1=display 
            historico=''
            operador = ""
            numero_2=''

    elif event == "Sobre":
        sg.popup('Calculadora simplificada v3.2\n Desenvolvida para culculos entre\n dois numeros inteiros, flutuantes,\n negativos e porcentagens')       
window.close()    