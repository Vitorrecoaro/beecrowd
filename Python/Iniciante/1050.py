# Problema 1050 - Beecrowd - Iniciante - Nível 2

# Recebe o ddd
ddd = int(input())

# Declaração do dicionário com os ddd's e seus respectivos estados
cidades = {
        61: "Brasilia",
        71: "Salvador",
        11: "Sao Paulo",
        21: "Rio de Janeiro",
        32: "Juiz de Fora",
        19: "Campinas",
        27: "Vitoria",
        31: "Belo Horizonte"
}

# Itera sobre o dicionário em busca do ddd informado
if ddd in cidades:
    print(cidades[ddd])
else:
    print("DDD nao cadastrado")
