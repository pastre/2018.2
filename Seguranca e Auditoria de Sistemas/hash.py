import hashlib
import json
import itertools


FILE_PATH = 'users.json'
ALFABETO ='abcdefghijklmnopqrstuvwxyz' #ABCDEFGHIJKLMNOPQRSTUVWXYX0123456789'

def hash(string):
	 return hashlib.md5(string.encode('utf-8')).hexdigest()

def persist_data(data):
	open(FILE_PATH, 'w').write(json.dumps(data, indent = 4))

def load_data():
	try:
		return json.loads(open(FILE_PATH, 'r').read())
	except FileNotFoundError:
		return {}

def cadastra_usuario(usuario, senha):
	data = load_data()
	if usuario in data.keys():
		print('Usuario ja cadastrado')
		return
	data[usuario] = hash(senha)
	persist_data(data)
	print('Usuario cadastrado com sucesso')

def autentica_usuario(usuario, senha):
	h = hash(senha)
	data = load_data()
	if data[usuario] == h: print(f'Bem vindo, {usuario}')
	else: print('Ops! Senha errada!')

def bruteforce_usuario(usuario):
	data = load_data()
	if not usuario in data.keys():
		print('Usuario nao encontrado')
		return
	possibilities =list(itertools.product('abcdefghijklmnopqrstuvwxyz', repeat=4)) # 3 is the length of your result.
	for p in possibilities:
		s = ''.join(p)
		if data[usuario] == hash(s):
			print(f'A senha para {usuario} é {s}')
			return
	print('Nao encontrei a senha!')


def popula_base():
	cadastra_usuario('aaaa', 'aaaa')
	cadastra_usuario('aaab', 'aaab')
	cadastra_usuario('aaac', 'aaac')
# bruteforce_usuario('aaab')

def main():
    while 1:
        print('Escolha uma opcao:\n\t1)Cadastrar usuario\n\t2)Autenticar usuario\n\t3) Encontrar senha\n\t9)Sair')
        opt = input()
        if opt == '1':
            usr, pwd = input('Digite um usuario: '), input('Digite uma senha: ')
            cadastra_usuario(usr, pwd)
        elif opt == '2':
            usr, pwd = input('Digite um usuario: '), input('Digite uma senha: ')
            autentica_usuario(usr, pwd)
        elif opt == '3':
            usr = input('Digite um usuario: ')
            bruteforce_usuario(usr)
        elif opt == '9':
            break
        else: print('Opcao desconhecida! Tente novamente')
        
# autentica_usuario('aaab', 'aaab')
# popula_base()
main()
