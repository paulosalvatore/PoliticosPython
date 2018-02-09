from politica import Politicos, Partidos

joao = Politicos(
	"João de Souza Oliveira",
	"111.222.333-44"
)

maria = Politicos(
	"Maria Pereira Albuquerque",
	"555.666.777-88"
)

jose = Politicos(
	"José Bonifácio da Silva",
	"333.222.111-44",
	"Jota"
)

pr = Partidos(
	"Partido da República",
	"PR",
	22,
	1000
)

pr.adicionar_politicos(joao, maria)

pt = Partidos(
	"Partido dos Trabalhadores",
	"PT",
	13,
	1500
)

pt.adicionar_politicos(jose, joao)

pt.realizar_doacao_politicos()
joao.exibir_dinheiro()
jose.exibir_dinheiro()
