# AINDA EM TESTE
# EXERCICIO 2

vet = []
pos = []
semrep = []

for i in range(2):
    num = int(input("Digite os números a serem analisados: "))
    vet.append(num)
    if num >= 0:
        pos.append(num)

for j in pos:
    cont = 0
    for k in semrep:
        if j == semrep:
            cont += 1
        if cont == 0:
            semrep.append(j)

print(f"vet = {vet}")
print(f"pos = {pos}")
print(f"semrep = {semrep}")