# FUNCIONANDO
# EXERCÍCIO 1

PROG1 = []
PROG2 = []
PROG3 = []
irregulares = []

for i in range(5):
    aluno = int(input("Digite a matricula do aluno que esta matriculado em PROG1: "))
    PROG1.append(aluno)

for j in range(7):
    aluno = int(input("Digite a matricula do aluno que esta matriculado em PROG2: "))
    PROG2.append(aluno)

for k in range(7):
    aluno = int(input("Digite a matricula do aluno que esta matriculado em PROG3: "))
    PROG3.append(aluno)


for l in range(len(PROG1)):
    for m in range(len(PROG2)):
        for n in range(len(PROG3)):
            if PROG1[l] == PROG3[n] and PROG2[m] == PROG3[n]:
                irregulares.append(PROG3[n])

for aluno in irregulares:
    print(f"Aluno {aluno} irregular")

print(f"Total de alunos irregulares = {len(irregulares)}")
