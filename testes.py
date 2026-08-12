import getpass

nome = input("Digite seu nome: ")
email = input("Digite seu e-mail: ")
senha = getpass.getpass("Digite uma senha: ")
confirmacao = getpass.getpass("Confirme sua senha: ")

print("Cadastro realizado com sucesso!")
print("Bem-vindo(a),", nome)
