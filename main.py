from academia import Academia

while True:
    acao = int(input("O que você deseja fazer: \n 1 - Cadastro \n 2 - Sair \n"))

    if acao == 1:
        cpf = input("Digite seu cpf: ")
        nome = input("Digite seu nome: ")
        idade = int(input("Digite sua idade: "))
        sexo = 0
        while sexo == 0:
            sexo = int(input("Selecione seu sexo: \n 1 - Masculino \n 2 - Feminino \n"))
            if sexo > 2 or sexo < 1:
                sexo = 0
                print("Selecione uma opção válida.")
        telefone = input("Digite seu telefone: ")
        email = input("Digite seu email: ")
        peso = float(input("Digite seu peso em kg: "))
        altura = float(input("Digite sua altura em metros: "))
        nvTreino = 0
        while nvTreino == 0:
            nvTreino = int(input("Selecione seu nível de treino: \n 1 - Iniciante \n 2 - Intermediário \n 3 - Avançado \n"))
            if nvTreino > 4 or nvTreino < 1:
                nvTreino = 0
                print("Selecione uma opção válida.")

        objTreino = 0
        while objTreino == 0:
            objTreino = int(input("Selecione seu objetivo de treino: \n 1 - Hipertrofia \n 2 - Emagrecimento \n"))
            if objTreino > 3 or objTreino < 1:
                objTreino = 0
                print("Selecione uma opção válida.")

        plano = 0
        while plano == 0:
            plano = int(input("Selecione seu plano de treino: \n CONSIDERE QUE NOSSA ACADEMIA ESTARÁ EM FUNCIONAMENTO DE SEGUNDA A SEXTA FEIRA, COM EXCEÇÃO DE FERIADOS! \n 1 - 3 dias de treino (50,00 R$) \n 2 - 4 dias de treino (60,00 R$) \n 3 - 5 dias de treino (70,00 R$) \n"))
            if plano > 4 or plano < 1:
                plano = 0
                print("Selecione uma opção válida.")
        
        
                
            print("\nCadastro realizado com sucesso!")
            
            academia = Academia(cpf,nome,idade,sexo,telefone,email,peso,altura,nvTreino,objTreino,plano,)
            print()
            print("Nossa academia possui atividades alternativas já inclusas em todos os planos (ZUMBA E JUMP), mais informações abaixo!")
            print()
            academia.valor()
            print()
            academia.zumba()
            print()
            academia.jump()
            print()  
            academia.treino()
            print()

    elif acao == 2:
        print("Saindo...")
        break
    else:
        print("Ação não reconhecida, digite um número válido.")
