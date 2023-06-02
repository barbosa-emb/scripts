#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 12 08:24:19 2023

@author: eduardo
"""

# -*- coding: utf-8 -*-
import pyodbc
from datetime import datetime
import csv
from decimal import Decimal


a = 1
aa = 5000

args = []
args_2 = []
for k in range(a, aa):    
    args.append(str(k) + "/2022")

         


#args = ["82/2023"]


arquivo = open('/Users/eduardo/database.txt','w')
arquivo.write('proposta;nome_fantasia;razao_social;cnpj;vigini;vigfin;csn;cso;vlrtotal;vlrpagoparceiro;parceiro;area;subarea;tpservico;sol\n')
for j in args:
    
    print(j)
    
    lista = []
    lista_formatada = []
    
    con = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=10.3.4.93;'
            'PORT=1433;'
            'DATABASE=MP12;'
            f'UID=qliksense;'
            f'PWD=$3br@e01.SQL.SENSE')
    cursor = con.cursor()

    cursor.execute(
    		'SELECT For_Fantasia, Fornecedor, CPF_CNPJ, DtVigDe, DtVgAte, ValorCSN, ValorCSO, VlTotContr, VlPgoParce, Parceiro, Area, SubArea, TpServico, NmServico '\
    		'FROM dbo.fcCtrCredPropUTIP(?)', (j)
    		)
    results = cursor.fetchall()
    #print(results)
    for row in results:
        row = list(row)  # converte pyodbc.Row em lista
        for i, value in enumerate(row):
            if isinstance(value, Decimal):
                row[i] = float(value)  # converte Decimal em float
        lista.append(row)
        
        
    con.close()
    
    
    
    for i in lista:
        
        print(i[9])
						
        var_0 = i[0]
        if(type(i[0]) != str):
            var_0 = " "
        
        var_1 = i[1]
        if(type(i[1]) != str):
            var_1 = " "
            
        var_2 = i[2]
        if(type(i[2]) != str):
            var_2 = " "
        
        var_3 = i[3]
        if(type(i[3]) != str):
            var_3 = " "
            
            
        var_4 = i[4]
        if(type(i[4]) != str):
            var_4 = " "
        
        var_9 = i[9]
        if(type(i[9]) != str):
            var_9 = " "
            
        var_10 = i[10]
        if(type(i[10]) != str):
            var_10 = " "
        
        var_11 = i[11]
        if(type(i[11]) != str):
            var_11 = " "
            
        var_12 = i[12]
        if(type(i[12]) != str):
            var_12 = " "
        
        var_13 = i[13]
        if(type(i[13]) != str):
            var_13 = " "
            
            
            
            
        b = str(j).split("/")
        if(len(b[0]) == 1):
            c = b[0] + "/2022"
        elif(len(b[0]) == 2):
            c = b[0] + "/2022"
        elif(len(b[0]) == 3):
            c = b[0] + "/2022"
        elif(len(b[0]) == 4):
            c = b[0] + "/2022"
        else:
             c = b[0] + "/2022"
            
        print(c)
        value = c + ";" + var_0.strip(" ") + ";" + var_1.strip(" ") +";" + var_2.strip(" ") +";" + var_3.strip(" ") +";" + var_4.strip(" ") +";" + str(i[5]) +";" + str(i[6]) + ";" + str(i[7]) +";" + str(i[8]) +";" + var_9.strip(" ") +";" + var_10.strip(" ") +";" + var_11.strip(" ") +";" + var_12.strip(" ") +";" + var_13.strip(" ") +"\n"
        arquivo.write(value)
arquivo.close()


