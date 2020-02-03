import sqlite3
import base64


def encode_senha(senha):
	senha_v = senha.encode()
	base_encode = base64.b64encode(senha_v)
	return base_encode


def decode_senha(senha):
	try:
		#caso a senha nao venha encodada
		senha_v2 = senha.encode()
		base_decode = base64.b64decode(senha_v2)
		return base_decode
	except:
		#caso a senha ja venha encodada
		senha_v2 = senha.decode()
		base_decode2 = base64.b64decode(senha_v2)
		return base_decode2


def coletar_dados():
	print('para voltar sem salvar nada: ctrl+c')
	info = []
	confirm = ''	
	
	while confirm != 'y':
		site = input('Site: ')
		user_email = input('User/Email: ')
		senha = input('Senha: ')
		confirm = str(input('Confirm n/y: ')).lower()
	#vai encoda a senha para salvar no banco de dados
	
	senhaEncodada = encode_senha(senha)
	dados = (site, user_email, senhaEncodada.decode())
	info.append(dados)
	return info


def conectar_dataBase():
	conex = sqlite3.connect('info.db')
	cursor = conex.cursor()
	return conex, cursor 


def create_tables(conex, cursor):
	try:
		cursor.execute(''' 
			CREATE TABLE info_site(
			site TEXT NOT NULL,
			User_Email TEXT NOT NULL,
			senhaEncode TEXT NOT NULL)''')
		print('ATENÇAO BANCO DE DADOS CONFIGURADO Reinicie! ')
	except:
		return 1


def save_dados(conex, cursor, dados_save):
	try:
		cursor.executemany(''' 
			INSERT INTO info_site(site, User_Email, senhaEncode)
			VALUES (?,?,?)''', dados_save)
		conex.commit()
		print('Dados Salvos')
	except:
		print('ERROR: alguma coisa aconteceu ao salvar as info! ')


def exibir_senha(conex, cursor):
	
	#vai seleciona todos os itens da coluna
	cursor.execute('''
	SELECT * FROM info_site ''')

	#fetchall() vai retorna o resultado do select
	#dois laço um para linha e outro para o conteudo da linha
	for linha in cursor.fetchall():
		cont = 0
		print('='*30)
		for info in linha:
			if cont == 0:
				print(f'Site: {info}')
			elif cont == 1:
				print(f'Email/Usuario: {info}')
			elif cont == 2:
				senhaD = decode_senha(info)
				print(f'Senha Encodada: {info}')
				print(f'Senha Decode: {senhaD.decode()}')

			cont += 1

	conex.close()










	
