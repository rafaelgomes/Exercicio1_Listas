from lista import *
#teste
#######################################################################
## Codigo main
#######################################################################

classeLista = Lista()

print "1 - Criar Lista"
print "2 - Ler Lista"
opcao = raw_input ("Informe a opcao: ")

if (opcao == "1"):
	lista = raw_input ("Informe a lista: ")
	if (lista.startswith('[')):
		lista = lista [1:]
	
	if (lista.endswith(']')):
		lista = lista[:-1]

	listaParOrdenada = classeLista.gerarListaParOrdenada (lista)

	if (listaParOrdenada != None):	
		print "Lista Salva com sucesso"
		print listaParOrdenada

elif (opcao == "2"):
	listaParOrdenada = classeLista.obterListaSalva()
	print listaParOrdenada
	

else:
	print "Opcao invalida"
	
