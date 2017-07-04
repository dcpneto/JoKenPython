import random
import time
#Atribuição numérica#
pedra = 1
papel = 2
tesoura = 3 
#Contador de vitórias
vitorias = 0
derrotas = 0
#Inicio-------------------------------------------------------------------------
print('Bem vindo ao Pedra/Papel/Tesoura 0.1 alpha version')
print()
print()
print()
#Inicio jogo--------------------------------------------------------------------
def main(): 
    global vitorias
    global derrotas
    global running
    
#Escolha/resultado--------------------------------------------------------------
    choices = ['pedra', 'papel', 'tesoura'] 
    
    
    print('Faça sua escolha')
    choice = input().lower() 
    print() 
    
 
    print('Pedra!')
    time.sleep(.7)

    print('Papel!')
    time.sleep(.7)

    print('Tesoura!')
    time.sleep(.7)

    print('Vai!')
    print() 
#contagem aleatoria-------------------------------------------------------------
    comp = random.randint(1, 3)
#Inicio escolha-----------------------------------------------------------------
    if choice == 'pedra':
                if comp == 1:
                    print('Pedra vs. Pedra...Emapatou!')
                    print()
                    
                elif comp == 2:
                    print('Pedra vs Papel. Você perdeu! HAHAHAHAHA!')
                    print()
                    derrotas = derrotas + 1
                elif comp == 3:
                    print('Pedra vs Tesoura. Você venceu!')
                    print()
                    vitorias = vitorias + 1

    elif choice == 'papel':
                if comp == 1:
                    print('Papel vs Pedra. Você venceu!')
                    print()
                    vitorias = vitorias + 1
                elif comp == 2:
                    print('Papel vs Papel. Temos um empate.')
                    print()
                elif comp == 3:
                    print('Papel vs Tesoura, perdeu! HAHAHAHA!')
                    print()
                    derrotas = derrotas + 1
#Elif para fim de jogo com auto-win--------------------------------------------               
    elif choice == 'chuck norris':
        print('Você ganha automaticamente e o computador junto ao mundo se auto-destroi')
        print()
        vitorias = vitorias + 100000
        chuck = random.randint(1,10)
        if chuck == 1:
            print('#1: Chuck Norris contou ao infinito 2x sendo a segunda de tras para frente')
            print()
        elif chuck == 2:
            print('#2: Chuck norris é capaz de nadar no asfalto')
            print()
        elif chuck == 3:
            print('#3: Chuck Norris perdeu sua virgindade antes dos seus pais')
            print()
        elif chuck == 4:
            print('#4: Chuck Norris pode curar o cancer com suas lagrimas, mas ele nunca chora')
            print()
        elif chuck == 5:
            print('#5: Aquecimento global é resultado de Chuck Norris saindo da academia')
            print()
        elif chuck == 6:
            print('#6: Chuck Norris teve um ataque cardíaco, seu coração perdeu.')
            print()
        elif chuck == 7:
            print('#7: Chuck Norris é Chuck Norris porque ele é Chuck Norris')
            print()
        elif chuck == 8:
            print('#8: Chuck Norris foi esfaqueado no olho em sua juventude, a faca ficou cega')
            print()
        elif chuck == 9:
            print('#9: Chuck Norris já jogou jokenpo contra ele mesmo no espelho e ganhou')
            print()
        elif chuck == 10:
            print('#10: Chuck Norris pode viajar no tempo')
            print()
            
        running = 0

    elif choice == 'tesoura':
                if comp == 1:
                    print('Tesoura vs Pedra. Você perde! HAHAHAHAHA!')
                    print()
                    derrotas = derrotas + 1
                elif comp == 2:
                    print('Tesoura vs Papel. Você venceu!')
                    print()
                    vitorias = vitorias + 1
                elif comp == 3:
                    print('Tesoura vs Tesoura, temos um empate.')
                    print()

    elif choice == 'sair':
        print('Seu placar foi de: ')
        print()
        print('Você obteve:', vitorias, 'vitória(s)')
        print('Você obteve:', derrotas, 'derrota(s)')
        
        running = 0
        
#Fim---------------------------------------------------------------------------
running = 1
while running == 1:
    
    main()
    if running == 0:
        print('O jogo acabou!!!')
        print()
    else:
#Resultados--------------------------------------------------------------------    
     print('Vitórias: ')
     print(vitorias)
     print()
    
     print('Derrotas: ')
     print(derrotas)
     print()

