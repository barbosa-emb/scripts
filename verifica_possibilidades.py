from itertools import combinations

print("Verificando possibilidades: ")
valores = [
   497.58, 497.58, 185, 10, 140, 315

]

def encontrar_combinacoes(valores, alvo):
    combinacoes = []
    for i in range(1, len(valores) + 1):
        for combo in combinations(valores, i):
            if sum(combo) == alvo:
                combinacoes.append(combo)
    return combinacoes

combinacoes_86980 = encontrar_combinacoes(valores, 869.80)

for combo in combinacoes_86980:
    print(combo)