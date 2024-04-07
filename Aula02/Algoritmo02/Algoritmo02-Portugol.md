Algoritmo TaxaConsumo

var taxaConsumo: real
      kmPercorrido, combustivel: real

inicio

escreva(“Informe quantos quilômetros foram percorridos: ”)

leia(kmPercorrido)

escreva(“Informe quanto combustível foi consumido: ")

leia(combustivel)

taxaConsumo -> kmPercorrido/combustivel

escreva(“Taxa de consumo =”, Tx)

Se (taxaConsumo <= 8) Então

escreva("O automóvel está consumindo muito combustível")

Senão
	escreva("O consumo de combustível está bom")

Fim se

fimalgoritmo
