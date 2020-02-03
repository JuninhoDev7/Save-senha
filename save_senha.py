import senha_lib as lib 
import banner as b
#lista com uma tupla

while True:
	b.menu_principal()
	try:
		op = int(input(': '))
		if op == 1:
			conex, cursor = lib.conectar_dataBase()
			
			if lib.create_tables(conex, cursor) == 1:
				print('Pronto para o uso')
				dados = lib.coletar_dados()
				lib.save_dados(conex, cursor, dados)
		
		elif op == 2:
			conex, cursor = lib.conectar_dataBase()
			lib.exibir_senha(conex, cursor)

		elif op ==3:
			print('ATENÇAO digite O nome do site que vc deseja altera as infos!: ')
			conex, cursor = lib.conectar_dataBase()
			print('Digite os novos dados')
			
			new_dados = lib.coletar_dados()
			lib.update_dados(conex, cursor, new_dados)
		
		elif op == 4:
			b.about()
			
		elif op == 5:
			break
		
		else:
			print('ERROR: essa opçao nao existe')
	except:
		print("ERROR: digite somente numeros")
