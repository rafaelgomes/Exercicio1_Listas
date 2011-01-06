class Lista:

	def gerarListaParOrdenada (self, lista):
		listaPar = []

		listaInt = self.converterStringLista(lista)
	
		if (listaInt == None):
			print "A lista deve conter apenas numeros inteiros"
			return None

		for n in listaInt:
			if (n % 2 == 0):
				listaPar.append(n)
			
		listaPar.sort()
		listaPar.reverse()

		self.salvarLista(listaPar)	

		return listaPar

	def obterListaSalva (self):
		try:
			arq = open("lista.txt", "r")
			lista = arq.readline()
			return lista
		except IOError:
			return "Nao ha lista salva"

	def converterStringLista (self, lista):
		listaRet = []
		lista = lista.split(",")	
	
		for n in lista:
			try:
				listaRet.append(int(n)) 
			except:
				listaRet = None

		return listaRet

	def salvarLista(self, lista):
		try:
			arq = open("lista.txt", "w")
			arq.write(str(lista))
		except IOError:
			return "Erro salvando Lista"		
