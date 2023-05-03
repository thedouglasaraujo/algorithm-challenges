setores = int(input())
torcedores_str = input().split()

torcedores = []
for i in torcedores_str:
    torcedores.append(int(i))

numero_fotografados = [0] * setores
numero_fotografados[0] = torcedores[0]

if setores > 1:
    if torcedores[0] > torcedores[1]:
        numero_fotografados[1] = torcedores[0]
    else:
        numero_fotografados[1] = torcedores[1]

for i in range(2, setores):
    anterior1 = numero_fotografados[i-1]
    anterior2 = numero_fotografados[i-2] + torcedores[i]
    if anterior1 > anterior2:
        numero_fotografados[i] = anterior1
    else:
        numero_fotografados[i] = anterior2

print(f"{numero_fotografados[setores-1]} torcedores podem ser fotografados.")
