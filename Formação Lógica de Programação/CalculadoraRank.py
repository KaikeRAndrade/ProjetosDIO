def calculadora(vitorias, derrotas):
	saldo = vitorias - derrotas
	if saldo < 0:
		return saldo, "Ferro"
	ranks =  [(0, 10, "Ferro"), (11, 20, "Bronze"), (21, 50, "Prata"), (51, 80, "Ouro"), (81, 90, "Diamante"), (91, 100, "Lendário")]
	for minimo, maximo, rank in ranks:
		if minimo <= saldo <= maximo:
			return saldo, rank
	return saldo, "Imortal"
vitorias = int(input("Digite o número de vitorias: "))
derrotas = int(input("Digite o número de derrotas: "))
saldo, rank = calculadora (vitorias, derrotas)
print(f"O seu saldo é {saldo} e o seu rank é {rank}")