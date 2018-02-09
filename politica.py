class Politicos:
	nome = None
	cpf = None
	nome_politico = None
	dinheiro = None

	def __init__(self, nome, cpf, nome_politico=""):
		self.nome = nome
		self.cpf = cpf
		self.nome_politico = nome_politico
		self.dinheiro = 0

	def adicionar_dinheiro(self, valor):
		self.dinheiro += valor
		print("A quantia de R$ {:.2f} foi adicionada para o político {}.".format(valor, self.pegar_nome()))

	def exibir_dinheiro(self):
		print("{} possui R$ {:.2f}.".format(self.pegar_nome(), self.dinheiro))

	def pegar_nome(self):
		if self.nome_politico != "":
			return self.nome_politico
		else:
			return self.nome


class Partidos:
	nome = None
	sigla = None
	numero = None
	politicos = None
	doacao = None

	def __init__(self, nome, sigla, numero, doacao):
		self.nome = nome
		self.sigla = sigla
		self.numero = numero
		self.politicos = []
		self.doacao = doacao

	def adicionar_politico(self, politico):
		self.politicos.append(politico)
		quantidade_politicos = len(self.politicos)
		plural_politicos = "" if quantidade_politicos == 1 else "s"
		print("O político {} foi adicionado com sucesso ao partido {}.".format(politico.pegar_nome(), self.sigla))
		print("O partido {} possui {} político{}.".format(self.sigla, quantidade_politicos, plural_politicos))

	def adicionar_politicos(self, *politicos):
		for politico in politicos:
			self.adicionar_politico(politico)

	def realizar_doacao_politicos(self):
		for politico in self.politicos:
			politico.adicionar_dinheiro(self.doacao)
