from tkinter import * #biblioteca  de interface
from tkinter.ttk import * #módulo de widgets
from time import strftime #biblioteca e função para informações das horas

janela = Tk() #instância para manipulação da janela
janela.title('Relógio Digital') #título da janela

#função para manipulação das horas
def time():
	string = strftime('%H:%M:%S %p') #tempo formatado
	lbl.config(text = string) #configuração do texto
	lbl.after(1000, time) #manipulação do tempo

#instância para definir a interface
lbl = Label(janela, font = ('arial', 40, 'bold'), #definição da fonte
		background = 'white', #cor de fundo
		foreground = 'black') #cor do primeiro plano

lbl.pack(anchor = 'center') #posicionando o rótulo ao centro da janela

time() #chamando a função "time" para início do relógio
