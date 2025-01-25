import random

print('Seja bem vindo ao jogo de pedra, papel e tesoura!')
while True:
    print('Regras:')
    print('1.Pedra ganha de tesoura')
    print('2.Papel ganha de pedra')
    print('3.Tesoura ganha de papel')
    print('Digite sair a qualquer momento para encerrar')
    print('Escolha uma opção:')
    print('1.papel')
    print('2.pedra')
    print('3.tesoura')

    jogador = input('Escolha a sua opção:')

    opcoes = ["pedra" , "papel" ,"tesoura"]
    maquina = random.choice(opcoes)
    print(f"Você escolheu : {jogador}")
    print(f"A maquina escolheu: {maquina}")
    
    if jogador == maquina :
        print("Empate!")
    elif (jogador == "pedra" and maquina == "tesoura") or\
         (jogador == "papel" and maquina =="pedra") or\
        (jogador == "tesoura" and maquina == "papel") :
        print("Você ganhou esta rodada!")    
    else :
        print("Você perdeu esta rodada !")
        
    pergunta = input("Você Deseja jogar novamente ? (sim/não): ").strip().lower()
    if pergunta != "sim":
        print("Obrigado por jogar! Até a próxima!")
        break  
    













    
    

    


        


