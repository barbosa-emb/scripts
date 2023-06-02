# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
import json
import csv


f = open('output.csv', 'w', newline='', encoding='utf-8')
w = csv.writer(f)

arq_listas = open('data.csv', 'r')
lista = arq_listas.read().split('\n')
arq_listas.close()

for i in lista:
    cnpj = i.split(';')[0]
    endereco = i.split(';')[1]

    endereco_completo = endereco #"RUA+SEBASTIAO+CORREIA+DA+ROCHA+953+TABUL+DOS+MARTINS+MACEIO+AL"

    response = requests.get("https://maps.google.com/maps/api/geocode/json?address=" + endereco_completo + "&components=country:BR&key=AIzaSyASbvXwmcLqLAZ4xNDOtlw9fRvYgjJSfU4", verify=True)
    y = json.loads(response.content)
    if(len(y["results"]) > 0):

        w.writerow([cnpj, y["results"][0]["geometry"]["location"]["lat"], y["results"][0]["geometry"]["location"]["lng"]])
        print(cnpj)
    #print(y["results"][0]["geometry"]["location"]["lat"])
    #print(y["results"][0]["geometry"]["location"]["lng"])
w.close()
print("concluido")