heroi = input('Digite o nome do herói: ')
xp = int(input('Digite o nível do seu herói: '))

faixas = [
    (1000, 'Ferro'),
    (2000, 'Bronze'),
    (5000, 'Prata'),
    (7000, 'Ouro'),
    (8000, 'Platina'),
    (9000, 'Ascendente'),
    (10000, 'Imortal'),
]

for limite, faixa in faixas:
    if xp <= limite:
        xp = faixa
        break
    if xp > 10000:
        xp = 'Radiante'
        break

print(f'O herói de nome {heroi}, está no nível de {xp}.')