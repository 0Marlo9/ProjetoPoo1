class Academia:
    def __init__(self,cpf,nome,idade,sexo,telefone,email,peso,altura,nvTreino,objTreino,plano,):
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.telefone = telefone
        self.email = email
        self.peso = peso
        self.altura = altura
        self.nvTreino = nvTreino
        self.plano = plano
        self.__valor = 0
        self.objTreino = objTreino

    def valor(self):
        if self.plano == 1:
            self.__valor = 50
            print('Valor da mensalidade: {}R$ (Reais)'.format(self.__valor))
        elif self.plano == 2:
            self.__valor = 60
            print('Valor da mensalidade: {}R$ (Reais)'.format(self.__valor))
        elif self.plano == 3:
            self.__valor = 70
            print('Valor da mensalidade: {}R$ (Reais)'.format(self.__valor))
    
    def zumba(self):
        print("Os treinos de zumba ocorrem toda terça e quinta feira, das 18:30 até as 19:30")

    def jump(self):
        print("Os treinos de jump ocorrem toda segunda e quarta feira, das 18:30 até as 19:30")
            
    def treino(self):
        
        if self.nvTreino == 1 and self.objTreino == 1:
            print ('HIPERTROFIA - INICIANTE --> ',
                   '\n1: Agachamento livre - 3 séries de 12 repetições.',  
                   '\n2: Levantamento terra - 3 séries de 12 repetições.', 
                   '\n3: Supino reto - 3 séries de 12 repetiçõe.s', 
                   '\n4: Remada curvada - 3 séries de 12 repetições.', 
                   '\n5: Desenvolvimento com halteres - 3 séries de 12 repetições.', 
                   '\n6: Rosca direta com barra - 3 séries de 12 repetições.', 
                   '\n7: Tríceps francês com halteres - 3 séries de 12 repetições.', 
                   '\n8: Elevação lateral com halteres - 3 séries de 12 repetições.', 
                   '\n9: Abdominal supra - 3 séries de 20 repetições.', 
                   '\n10: Prancha abdominal - 3 séries de 30 segundos.')


 
        elif self.nvTreino == 2 and self.objTreino == 1:
            print ('HIPERTROFIA - INTERMEDIÁRIO --> ',
                   '\n\n1: Agachamento com barra - 4 séries de 10 repetições.', 
                   '\n2: Levantamento terra - 4 séries de 10 repetições.', 
                   '\n3: Supino inclinado com halteres - 4 séries de 10 repetições.',
                   '\n4: Barra fixa - 4 séries de 10 repetições.', 
                   '\n5: Desenvolvimento com barra - 4 séries de 10 repetições.',
                   '\n6: Rosca bíceps alternada com halteres - 4 séries de 10 repetições.',
                   '\n7: Tríceps paralelas - 4 séries de 10 repetições.', 
                   '\n8: Elevação lateral com halteres - 4 séries de 10 repetições.', 
                   '\n9: Abdominal infra - 4 séries de 20 repetições.', 
                   '\n10: Prancha lateral - 4 séries de 30 segundos (cada lado).')
        
        elif self.nvTreino == 3 and self.objTreino == 1:
            print ('HIPERTROFIA - AVANÇADO --> ',
                   '\n\n1: Agachamento com barra - 5 séries de 8 repetições.', 
                   '\n2: Levantamento terra - 5 séries de 8 repetições.',
                   '\n3: Supino reto com barra - 5 séries de 8 repetições.', 
                   '\n4: Remada curvada - 5 séries de 8 repetições.', 
                   '\n5: Desenvolvimento militar com barra - 5 séries de 8 repetições.', 
                   '\n6: Rosca bíceps com barra - 5 séries de 8 repetições.', 
                   '\n7: Tríceps testa com barra - 5 séries de 8 repetições.', 
                   '\n8: Elevação lateral com halteres - 5 séries de 8 repetições.', 
                   '\n9: Abdominal infra - 5 séries de 20 repetições.', 
                   '\n10: Prancha abdominal com peso - 5 séries de 30 segundos.')
            

        elif self.nvTreino == 1 and self.objTreino == 2:
            print ('ESMAGRECIMENTO - INICIANTE --> ',
                   '\n\n1: Caminhada rápida - 5 minutos.', 
                   '\n2: Agachamento - 3 séries de 10 repetições.', 
                   '\n3: Flexão de braço - 3 séries de 10 repetições.', 
                   '\n4: Polichinelo - 3 séries de 30 segundos.',
                   '\n5: Avanço - 3 séries de 10 repetições para cada perna.', 
                   '\n6: Abdominal crunch - 3 séries de 10 repetições.', 
                   '\n7: Jumping jack - 3 séries de 30 segundos.', 
                   '\n8: Prancha - 3 séries de 30 segundos.', 
                   '\n9: Elevação de panturrilha - 3 séries de 10 repetições.', 
                   '\n10: Jump rope - 3 séries de 30 segundos.')


        elif self.nvTreino == 2 and self.objTreino == 2:
            print ('ESMAGRECIMENTO - INTERMEDIÁRIO --> ',
                   '\n\n1: Corrida leve - 5 minutos', 
                   '\n2: Agachamento com salto - 3 séries de 10 repetições.', 
                   '\n3: Flexão de braço com apoio nos joelhos - 3 séries de 10 repetições.', 
                   '\n4: Burpee - 3 séries de 10 repetições.', 
                   '\n5: Avanço com salto - 3 séries de 10 repetições para cada perna.', 
                   '\n6: Abdominal reverso - 3 séries de 10 repetições.', 
                   '\n7: Mountain climber - 3 séries de 30 segundos.', 
                   '\n8: Prancha lateral - 3 séries de 30 segundos para cada lado.', 
                   '\n9: Elevação de panturrilha com peso - 3 séries de 10 repetições.', 
                   '\n10: Corrida estacionária - 3 séries de 30 segundos.')


        elif self.nvTreino == 3 and self.objTreino == 2:
            print ('ESMAGRECIMENTO - AVANÇADO --> ',
                   '\n\n1: Corrida intervalada - 5 minutos (30 segundos de corrida rápida seguidos por 30 segundos de caminhada.', 
                   '\n2: Agachamento com salto e peso - 3 séries de 10 repetições.', 
                   '\n3: Flexão de braço com apoio nos dedos dos pés - 3 séries de 10 repetições.', 
                   '\n4: Kettlebell swing - 3 séries de 10 repetições.', 
                   '\n5: Avanço com salto e peso - 3 séries de 10 repetições para cada perna.', 
                   '\n6: Abdominal bicicleta - 3 séries de 10 repetições.', 
                   '\n7: Plank com elevação alternada de braço e perna - 3 séries de 30 segundos.',
                   '\n8: Prancha com toque no ombro - 3 séries de 30 segundos.', 
                   '\n9: Elevação de panturrilha com salto - 3 séries de 10 repetições.', 
                   '\n10: Box jump - 3 séries de 10 repetições.')
            
          
class TreinosAlt:
    def __init__(self,treinoAltt):
        self.treinoAltt = treinoAltt

class Zumba (TreinosAlt):
    def zumbaa(self):
        print("Os treinos de zumba ocorrem toda terça e quinta feira, das 18:30 até as 19:30")

class Jump (TreinosAlt):
    def jumpp(self):
        print("Os treinos de jump ocorrem toda segunda e quarta feira, das 18:30 até as 19:30")