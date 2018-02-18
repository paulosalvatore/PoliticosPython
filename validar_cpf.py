def calcular_digito(numeros, fator):
	soma = calcular_soma_fator(numeros, fator)

	divisao, resto = divmod(soma, 11)

	if resto < 2:
		return 0
	else:
		return 11 - resto


def calcular_soma_fator(numeros, fator):
	total = 0
	for numero in numeros:
		numero = int(numero)
		total += numero * fator
		fator -= 1
	return total


def validar_cpf(cpf):
	cpf = cpf.replace(".", "")

	if len(cpf) != 12 or cpf.count("-") != 1:
		return False

	cpf_separado = cpf.split("-")
	numeros = cpf_separado[0].replace(".", "")
	digitos = cpf_separado[1]

	digito1 = calcular_digito(numeros, 10)
	digito2 = calcular_digito(numeros + str(digito1), 11)

	return digito1 == int(digitos[0]) and digito2 == int(digitos[1])


if validar_cpf("430.910.048-13"):
	print("CPF válido.")
else:
	print("CPF inválido.")
