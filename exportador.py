# -*- coding: utf-8 -*-
from tkinter import *
import pyodbc
from datetime import datetime
import csv

lista = []
lista_formatada = []

con = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost;'
        'PORT=1433;'
        'DATABASE=TAMPPLAST;'
        f'UID=sa;'
        f'PWD=Zuc@mago4')
         
cursor = con.cursor()
cursor.execute(
		'SELECT InstallmentDate, MA_PyblsRcvblsDetails.Notes, MA_PyblsRcvblsDetails.CostCenter, Amount, MA_PyblsRcvblsDetails.PymtAccount,  MA_PyblsRcvblsDetails.InstallmentType, MA_CustSupp.Account, MA_Banks.Account, Closed, MA_ChartOfAccounts.ExternalCode, MA_PyblsRcvblsDetails.PymtSchedId, MA_PyblsRcvblsDetails.InstallmentNo '\
		'FROM TAMPPLAST.dbo.MA_PyblsRcvblsDetails '\
		'INNER JOIN TAMPPLAST.dbo.MA_CustSupp ON (MA_PyblsRcvblsDetails.CustSuppType = MA_CustSupp.CustSuppType AND MA_PyblsRcvblsDetails.CustSupp = MA_CustSupp.CustSupp) '\
		'INNER JOIN TAMPPLAST.dbo.MA_Banks ON (MA_PyblsRcvblsDetails.PymtCash = MA_Banks.Bank) '\
		'INNER JOIN TAMPPLAST.dbo.MA_ChartOfAccounts ON (MA_PyblsRcvblsDetails.PymtAccount = MA_ChartOfAccounts.Account)'
		)
results = cursor.fetchall()
for row in results:
    lista.append(row)
    
    
con.close()


arquivo = open('C:/Temp/202301.txt','w')
arquivo.write("0000|37308375000123|\n")
for i in lista:
	dData = i[0].strftime("%d/%m/%Y")
	dMesAno = i[0].strftime("%m/%Y")
	if(dMesAno == "01/2023" and i[8] == '1'):

		cConta = str(i[9]) #era4
		cCodTipo = str(i[5])
		cTipo = ""
		if(cCodTipo == "5505025"):
			cTipo = "D"
		else:
			cTipo = "C"	
							
		
		value = "6100|" + dData + "|" + cConta + "|" + str(i[7]) + "|" + f'{i[3]:.2f}'.replace('.', ',') + "||" + i[1] + " - DOC: " + str(i[10]) + "-" + str(i[11]) + "|||\n"
		if(len(cConta) > 0 and len(str(i[7]))>0 and str(i[7]) != cConta and cTipo == "D"): 
			lista_formatada.append("6000|x|||")
			lista_formatada.append(value)

			arquivo.write("6000|x||||\n")
			arquivo.write(value)
arquivo.close()
print(lista_formatada)
class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Dados do usuario")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.nomeLabel = Label(self.segundoContainer,text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.senhaLabel = Label(self.terceiroContainer, text="Senha", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)

        self.senha = Entry(self.terceiroContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Autenticar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    #Método verificar senha
    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "usuariodevmedia" and senha == "dev":
            self.mensagem["text"] = "Autenticado"
        else:
            self.mensagem["text"] = "Erro na autenticacao"


root = Tk()
Application(root)
root.mainloop()