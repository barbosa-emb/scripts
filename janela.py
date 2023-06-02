''''
import requests
import json


url = "https://api.checkin.hml.sebrae.al/gpt/question"
data = {"question": "anything now. Escreva em um estilo coloquial e relacionável e responda essa pergunta como se fosse analista do SEBRAE Alagoas, de forma fácil de ser entendida. Envolva o tema empreendedorismo e mundo empresarial na resposta e Use linguagem natural. Segue a pergunta: A meta de Cobertura do Atendimento foi 25 e o realizado 16", "role":"user"} # corpo da solicitação em formato de dicionário
api_key = "Api-Key 0i912ANk.fMeoIHbfsgOs4NE3Bl2KGvISfntBV7Mf"

headers = {"authorization": api_key} # cabeçalho HTTP que inclui a api-key

response = requests.post(url, json=data, headers=headers, timeout=20)

a = response.json()
print(a)
'''


import requests
from json import loads

tarball_url = 'http://ia.hml.sebrae.al/api/gpt/question'
r = requests.get(tarball_url,json={"question":"anything now. Escreva em um estilo coloquial e relacionável e responda essa pergunta como se fosse analista do SEBRAE Alagoas, de forma fácil de ser entendida. Envolva o tema empreendedorismo e mundo empresarial na resposta e Use linguagem natural. Segue a pergunta: como aumentar o faturamento da minha empresa ?"},headers={"API-Key":"73a1102abc4047e4ab836903d2aadc90"})

for chunk in r:
        # Processar o fluxo de dados chunk por chunk
        
        # Exemplo: enviar o chunk de áudio para a resposta da Alexa
        speech_chunk = "<speak>{}</speak>".format(chunk.decode('utf-8'))
        print(speech_chunk)