


import PySimpleGUI as sg

#Neste bloco escolhemos o tema, visor, botões e layout da calculadora
sg.theme("NeutralBlue")

visor  =[[sg.Input("0", size=(22, 1), font=("Any", 30, "bold"),background_color="lightYellow", key="-manter-", justification='right')],
         [sg.Input("0", size=(12, 1), font=("Any", 54, "bold"), key="-out-", justification='right')],]

numeros=[[sg.Button("7", size=(7,3), key="7", font="bold",), sg.Button("8", size=(7, 3), key="8", font="bold"), sg.Button("9", size=(7, 3), key="9", font="bold")],
        [sg.Button("4", size=(7, 3), key="4", font="bold"), sg.Button("5", size=(7, 3), key="5", font="bold"), sg.Button("6", size=(7, 3), key="6", font="bold")],
        [sg.Button("1", size=(7, 3), key="1", font="bold"), sg.Button("2", size=(7, 3), key="2", font="bold"), sg.Button("3", size=(7, 3), key="3", font="bold")],
        [sg.Button("+/-", size=(7, 3), key="+/-", font="bold",button_color="lightBlue",), sg.Button("0", size=(7, 3), key="0", font="bold"), sg.Button(",", size=(7, 3), key=".", font="bold",button_color="lightBlue",)],]
    
bloco1 =[[sg.Button("<", size=(7, 3), font="bold",button_color="#ECA138", key="<")],
        [sg.Button("x", size=(7, 3), font="bold",button_color="lightBlue", key="*")],
        [sg.Button("-", size=(7, 3), font="bold",button_color="lightBlue", key="-")],
        [sg.Button("+", size=(7, 3), font="bold",button_color="lightBlue", key="+")],]

bloco2 =[[sg.Button("C", size=(7, 3), font="bold",button_color="#ECA138", key="c")],
        [sg.Button("/", size=(7, 3), font="bold",button_color="lightBlue", key="/")],
        [sg.Button("%", size=(7, 3), font="bold",button_color="lightBlue", key="%")],
        [sg.Button("=", size=(7, 3), font="bold",button_color="#ECA138", key="=")],]
    
layout_calculadora =[[sg.Frame("", visor)],
                     [sg.Frame("", numeros), sg.Col(bloco1), sg.Col(bloco2)],]
                     
tab_layout1 = [[sg.Frame("",layout_calculadora)], ]

menu_botao = [["Sobre"]]
janela = [
    [sg.MenuBar(menu_botao)],
    [sg.Text("NOVA TABOADA", size=(45, 1), justification='center', font=("Any", 18, "bold"), relief='flat')],
    [sg.TabGroup([[sg.Tab("Calculadora", tab_layout1)],])],
    [sg.Text("", size=(22, 1)), sg.Button("Sair",size=(18,1),button_color="red")],]
    
window = sg.Window("TABOADA", janela,size=(550,660), resizable=True)
operadores = ["+", "-", "*","/"]
calculo=""
manter = ""
operacao = ""
numeros = [str(i) for i in range(0, 10)]#uma laço para gerar "0 a 9 convertidos em str
while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, "Sair"):
        break
       
       
    elif event in numeros:
        if not operacao:
            if len(manter) < 12:
                manter += event
                calculo+=event
                window["-out-"].update(calculo)
        else:
            manter+=event
            calculo+=event
            window["-out-"].update(calculo)
        
    elif event in operadores:
        operacao=event
        numero_1=manter
        if event not in manter:
            manter += event
            calculo+=event
            window["-out-"].update(calculo)
            manter=""
        else:
            manter = manter[:-1] + operacao  #
            calculo=manter
            window["-out-"].update(calculo)
            window["-manter-"].update(calculo)
            manter=""
    
    elif event == "=":
        if operacao:
            numero_2=manter
            window["-manter-"].update(calculo)
            calculo=""
            if operacao == "+":
                resp =str(float (numero_1)+ float(numero_2))
            elif operacao == "-":
                resp =str(float (numero_1)- float(numero_2))
            elif operacao == "*":
                resp =str(float (numero_1)* float(numero_2))
            elif operacao == "/":
                if numero_2 != 0:
                    resp =str(float (numero_1)/ float(numero_2))
                else:
                    resp = "Erro"
            
            manter = (f"{resp}".replace(".0",""))
            window["-out-"].update(manter)
            operacao = ""
            numero_1=manter
            calculo=manter
            numero_2=''
    
    elif event=="<":
        if len(manter):
            manter=manter[:-1]
            window["-out-"].update(manter)
    
    elif event == "c":
        manter = ""
        operacao = ""
        calculo=""
        window["-out-"].update("0")
    
    elif event == "+/-":
        manter=str(float(manter * -1))
        window["-out-"].update(manter)
    elif event==".":
        if "." not in manter:
            manter += "."
            window["-out-"].update(manter)
    
    elif event == "%":
        if operacao:
            porcentagem = float(numero_1) * (float(manter) / 100)  # Convertendo para porcentagem
            numero_2 = porcentagem
            window["-manter-"].update(calculo)
            if operacao == "+":
                resp = str(float(numero_1) + numero_2)
            elif operacao == "-":
                resp = str(float(numero_1) - numero_2)
            elif operacao == "*":
                resp = str(float(numero_1) * numero_2)
            elif operacao == "/":
                if numero_2 != 0:
                    resp =str(float (numero_1)+ float(numero_2))
                else:
                    manter = "Erro"
            manter = (f"{resp}".replace(".0",""))
            window["-out-"].update(manter)
            numero_1=manter 
            calculo=manter
            operacao = ""
            numero_2=''
window.close()    