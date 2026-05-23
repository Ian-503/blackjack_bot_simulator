import random

CARTA_VIRADA = (
    "-------\n"
    "|#####|\n"
    "|#####|\n"
    "|#####|\n"
    "-------"
)

baralho_21 = {
    "-------\n| A     |\n|   ♦   |\n|     A |\n-------": [1, 11],
    "-------\n| 2     |\n|   ♦   |\n|     2 |\n-------": 2,
    "-------\n| 3     |\n|   ♦   |\n|     3 |\n-------": 3,
    "-------\n| 4     |\n|   ♦   |\n|     4 |\n-------": 4,
    "-------\n| 5     |\n|   ♦   |\n|     5 |\n-------": 5,
    "-------\n| 6     |\n|   ♦   |\n|     6 |\n-------": 6,
    "-------\n| 7     |\n|   ♦   |\n|     7 |\n-------": 7,
    "-------\n| 8     |\n|   ♦   |\n|     8 |\n-------": 8,
    "-------\n| 9     |\n|   ♦   |\n|     9 |\n-------": 9,
    "-------\n| 10    |\n|   ♦   |\n|    10 |\n-------": 10,
    "-------\n| J     |\n|   ♦   |\n|     J |\n-------": 10,
    "-------\n| Q     |\n|   ♦   |\n|     Q |\n-------": 10,
    "-------\n| K     |\n|   ♦   |\n|     K |\n-------": 10
}

lista_cartas = list(baralho_21.keys())

def addCarta(mao):
    carta = random.choice(lista_cartas)
    mao.append(carta)

def contar(mao):
    total = 0
    asses = 0
    
    for carta in mao:
        if "A" in carta:
            asses += 1
        else:
            total += baralho_21[carta]
            
    for _ in range(asses):
        if total + 11 <= 21:
            total += 11
        else:
            total += 1
            
    return total

def acaoBot(botMao, suaMao, pontos_bot, pontos_suas):
    oquefazer = random.randint(1, 2)
    
    match oquefazer:
        case 1:
            if pontos_suas <= 21:
                primeira_carta_sua = suaMao[0]
                valor_primeira_sua = baralho_21[primeira_carta_sua]
                
                if isinstance(valor_primeira_sua, list):
                    valor_primeira_sua = 11
                    
                alvo_do_bot = valor_primeira_sua + 10
                

                while pontos_bot < alvo_do_bot:
                    addCarta(botMao)
                    pontos_bot = contar(botMao)
                    print("O Bot decidiu comprar mais uma carta...")
                    
                    if pontos_bot > 21:
                        break
                        
        case 2:
            while pontos_bot < 17 and pontos_suas <= 21:
                print("O Bot decidiu comprar mais uma carta...")
                addCarta(botMao)
                pontos_bot = contar(botMao)
                
    return pontos_bot
dinheiro = 100
dobrar=1

while 0 <= dinheiro < 10000:
    suaMao = []
    botMao = []
    
    addCarta(suaMao)
    addCarta(suaMao)
    addCarta(botMao)
    addCarta(botMao)
    
    jogando = True
    while jogando:
        print("\n=== SUA MÃO ===")
        for carta in suaMao:
            print(carta)
        print(f"Seus pontos atuais: {contar(suaMao)}")
        
        if contar(suaMao) > 21:
            print("Você estourou 21!")
            jogando = False
            break

        print("\n=== MÃO DO BOT ===")
        print(botMao[0])     
        print(CARTA_VIRADA)  
        
        acao = int(input("\nO que você quer fazer? \n1 - Adicionar outra carta\n2 - Encerrar rodada\n3 - Dobrar a aposta (compra só mais uma e encerra)\n> "))
        
        match acao:
            case 1:
                addCarta(suaMao)
            case 2:
                jogando = False
            case 3:
                dobrar = dobrar * 2
                addCarta(suaMao)
                jogando = False 

    seusPontos = contar(suaMao)
    pontos_bot = contar(botMao)
    
    pontos_bot_final=acaoBot(botMao, suaMao, pontos_bot, seusPontos)
        
    print("\n=== MÃO FINAL DO BOT ===")
    for carta in botMao:
        print(carta)

    print("\n====== RESULTADO DA RODADA ======")
    print(f"Seus pontos: {seusPontos} | Pontos do Bot: {pontos_bot_final}")
    
    if seusPontos > 21:
        print("Você perdeu! Estourou 21.")
        dinheiro = dinheiro - (20 * dobrar)
    elif pontos_bot_final > 21:
        print("Você ganhou! O bot estourou.")
        dinheiro = dinheiro + (20 * dobrar)
    elif seusPontos > pontos_bot_final:
        print("Você ganhou!")
        dinheiro = dinheiro + (20 * dobrar)
    elif seusPontos < pontos_bot_final:
        print("Você perdeu!")
        dinheiro = dinheiro - (20 * dobrar)
    else:
        print("Empate!")

    print(f"Seu saldo atual: ${dinheiro}")
    
    if dinheiro <= 0:
        print("Você faliu! Fim de jogo.")
        break
        
    continuar = input("\nQuer jogar mais uma rodada? (s/n): ")
    dobrar=1
    if continuar.lower() != 's':
        break

print("\nObrigado por jogar!")
