#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 14:07:07 2023

@author: eduardo
"""

import openai

openai.api_key = "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"

def generate_response(prompt):
    model_engine = "text-davinci-003"
    prompt = (f"{prompt}")

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()
    
    
while True:
    #user_input = input("User: ")
    user_input = "Me faça um resumo baseado em: A meta de Cobertura do Atendimento (M.E e EPP) em Dezembro é 20 e o realizado 25, com um percentual de atingimento em 125%."
    user_input += "A meta de Pequenos Negócios atendidos (MEI, M.E e EPP) em Dezembro é 30.000 e o realizado 49.530, com um percentual de atingimento em 165,10%."
    user_input += "A meta de Pequenos Negócios atendidos com soluções de inovação em Dezembro é 4.000 e o realizado 5.777, com um percentual de atingimento em 144,42%."
    user_input += "A meta de Clientes atendidos por meio de serviços digitais em Dezembro é 45.000 e o realizado 73.243, com um percentual de atingimento em 162,76%."
    user_input += "A meta de Clientes com garantia do FAMPE assistidos na fase pós-crédito em Dezembro é 70 e o realizado 95, com um percentual de atingimento em 135,71%."
    user_input += "A meta de Professores atendidos em soluções de educação empreendedora em Dezembro é 4.000 e o realizado 4.966, com um percentual de atingimento em 124,15%."
    user_input += "A meta de Recomendação do Sebrae (NPS) em Dezembro é 80 e o realizado 86, com um percentual de atingimento em 107,50%."
    
    if user_input == "exit":
        break
    response = generate_response(user_input)
    print("Chatbot:", response)