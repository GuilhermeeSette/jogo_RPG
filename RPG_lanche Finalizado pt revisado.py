'''
Projeto - Jogo RPG
Autores : Guilherme Araujo Sette / José Eduardo Guimaraes / Luiz Henrique Carvalho
07/09/2017
'''
import math

#Título
print("                                                                      DISHONORED WARRIOR                                                                            ")
print("\n \nBem vindo ao melhor jogo de sua vida!\n \n")
#Resumo da história

#Parágrafo 1
print("O jogo vai ser um RPG com tema de mitologia nórdica. Na mitologia nórdica os guerreiros que\nmorrem em batalha são levados para Valhalla pois a morte em batalha demonstra um sinal\nde honra para os deuses, um lugar onde guerreiros bebem e lutam entre si pela eternidade.\nVocê é uma guerreiro experiente nórdico filho de um chefe de uma tribo nórdica\ncom um irmão mais velho.")
print("                                  ")
input("Pressione Enter para continuar")
#Parágrafo 2
print("")
print("Ambos morreram antes de você em uma batalha e agora a sua última\ntarefa como novo chefe da tribo é ir em uma peregrinação para achar uma terra melhor \npara seu povo e assim lidera-los e morrer em batalha como todo um bom viking assim \ngarantindo o seu lugar ao lado de seu pai e seu irmão em Valhalla, um majestoso e enorme\nsalão com 504 portas, situado em Asgard, dominado pelo deus dos deuses Odin, onde todos\nos guerreiros com morte honrosa vão comemorar pela eternidade comendo, bebendo e\nlutando entre sí sem medo da morte.")
print("                                  ")
input("Pressione Enter para continuar")
#Parágrafo 3
print("")
print("Mas, durante sua peregrinação você morre fora de batalha em uma tempestade no mar e seu\nlugar em Valhalla não foi concedido por não ter provado seu valor na morte em batalha. Mas\nagora você recebe uma chance para mostrar aos deuses o seu valor. E como você vai fazer\nisso? Os deuses indicam 5 seres da mitologia nórdica para você enfrentar.\nEles serão chamados de Gudom. (Significa divindade em Sueco, os vikings usavam a língua escandinava\npara se comunicar e a área q a Escandinávia abrangia ocupava hoje em dia os países\neuropeus Suécia, Noruega, Finlândia e Dinamarca).\n")
print("                                   ")
print("                                   ")

#Escolha de gênero
genero = str(input("Escolha, homem ou mulher?"))

#Pequena interatividade com o usuário, não interfere muito no código.
while genero.upper() != "HOMEM" or genero.upper() != "MULHER":
    if genero.upper() == "HOMEM":
        print("Seja bem vindo guerreiro, a sua honra e de sua familía está em suas mãos!")
        print(" ")
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        break
    elif genero.upper() == "MULHER":
        print("Seja bem vinda guerreira, a sua honra e de sua familía está em suas mãos!")
        print(" ")
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        break
    print("Gênero incorreto, digite novamente")
    genero = str(input("Esolha, homem ou mulher?"))
    
#Manual e instruções
print("Manual e instruções.")
print("                                   ")
print("                                   ")
print("O lugar que você passará no pós morte tem 5 níveis e eles serão determinados pela \nquantidade de Gudom que você derrotar e até onde você chegara no seu progresso.")
print("                                   ")
print("Nas batalhas teremos pontuações. A pontuação pode ser determinada com uma vida base de \n1000 pontos. Ao longo do caminho com ataques de Gudom você pode perder os pontos de \nvida ou até morrer e receber um final de acordo com seu progresso. Os Gudom serão \ndescritos antes da batalha e pela lógica você deve tomar a decisão correta para não perder \npontos chegando até o final do jogo vivo/a. Se você fizer o progresso perfeito e não perder \npontos de vida você recebe o final especial de 100%.")
print("                                   ")
print("Opções cruciais e básicas de vida ou morte vão determinar se você morre e tem sua alma \nperdida.")
print("")
input("Pressione Enter para continuar")
print("                                   ")
print("Isso pode ser determinado pela seguinte maneira: quando seu personagem na história morreu \nele foi mandado para Nilflheim, o mundo desabitado de gelo, neblina e névoa. Seu primeiro \nobjetivo será escolher um caminho seguro com opções básicas de vida ou morte para poder \nsair desse reino e começar a sua jornada para derrotar os 5 Gudom.")
print(" ")
print("As classificações serão essas:",
      "\n0% a 19% = Iniciante",
      "\n20% a 39% = Semiprofissional",
      "\n40% a 59% = Profissional",
      "\n60%  a 79% = Mestre",
      "\n80% a 99% = Grão-mestre",
      "\n100% = Gudom")
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")

#porcentagem relacionada ao progresso de chefes do jogo conquistados
    
      

#Separei os parágrafos com prints vazios para ficar mais visível para o usuário

'''Colocarei as variáveis de jogo e de batalha. As de jogo seguirão por todo o jogo, como é o caso do sangue e ataque do jogador.
As de batalha serão como o sangue e o ataque de cada Gudom. '''

#variaveis do jogo
sangue_player = 1000.00 # Define que a barra de saúde do jogador terá um total de 1000
atk_player = 450.00 # O poder de ataque do jogador terá um dano de 450 pontos no adversário
pontuacao = 0
''' Colocarei como base 3 opções:
-Atacar 
-Desviar
-Defender
Cada uma deve conter uma das três pontuações; 50, 25 ou 0.
OBS: Caso queiram adicionar opções não se esqueçam de ajustar as pontuações para a batalha." '''

#1ª Batalha, a Deusa da morte e cuidadora de almas, Hella
#Variáveis da batalha
sangue_hella = 1350.00 #Define barra de saúde de Hella
atk_hella = 100.00 #Poder de ataque de hella
#A variavel de vida do boss está sendo colocada como um numero divisivel por 450 que é o ataque do jogador

print("Você começa o jogo com 1000 pontos de saúde e seu poder de ataque é de 450 pontos.\nDure até onde puder!")
print(" ")
print("Se prepare guerreiro(a), ai está seu primeiro desafio!")
print("                                   ")
print("Hella, a Deusa da morte e cuidadora das almas que não morreram em batalha.\nSeus ataques são rápidos porem não tem tanto impacto.")
print(" ")
print("VAMOS COMEÇAR!")
print(" ")

#início da batalha
'''
Nessa batlha, segue a pontuação das alternativas:
-Quando Hella ataca:
    Atacar = 0
    Desviar = 25
    Defender = 50
-Quando Hella está cansada:
    Atacar = 50
    Desviar = 0
    Defender = 0
'''
print("Hella quer acabar com isso logo, ela é rápida no ataque! \nEla vai pra cima de você!")
print(" ")
#IMPORTANTE O while sera utilizado para a batalha contra o chefe e deve ter um break na condição caso o player morra para parar o programa
#Para o programa continuar funcionando pós batalha pedir para o usuario colocar um numero para uma variavel. Mais explicações depois da batalha contra o primeiro chefe.
#Esse while é um laço que faz o sistema repetir todos os if's até que a condicão do sangue do Godum ou do Player ser <= 0, isso evita de escrevermos 1000 linhas de código.
while sangue_hella - atk_player > -1 and sangue_player - atk_hella > -1:

    #Entrada em que o usuário escolhe uma das opções pelo número das mesmas.
    opcao = int(input("Você deve escolher uma das opções: \n1-Atacar \n2-Desviar \n3-Defender \nEscolha!"))
    print(" ")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
   #Esse print cheio de hífens serve para separar as etapas da batalha a cada momento que o jogo pede para você fazer algo

    #Escolha errada
    if opcao == 1:
        sangue_player = sangue_player - atk_hella #Barra de sangue de jogador, subtrai o sangue dele pelo ataque do Gudom
        pontuacao += 0
        print("Uh, Hella é mais rápida que você! \nVocê foi atingido.")
        print(" ")
        print("Barra de sangue: \nHella:",sangue_hella,"/ Player:",sangue_player)#Mostra o sangue do Gudom e do Player
        print(" ")
        print("A Deusa te ataca novamente!!")
        
    #Escolha média
    elif opcao == 2:
        sangue_player = sangue_player - (atk_hella / 2) #Pega de raspão, então o ataque do Gudom tem seu valor reduzido pela metade.
        pontuacao +=25 
        print("Você tentou, mas Hella é rápida e te acertou de raspão.\nPorém isso cansou Hella")
        print(" ")
        print("Barra de sangue: \nHella:",sangue_hella,"/ Player:",sangue_player)#Mostra o sangue do Gudom e do Player
        opcao = int(input("Você deve escolher uma das opções: \n1-Atacar \n2-Desviar \n3-Defender \nEscolha!"))
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        #Escolha correta
        if opcao == 1:
            sangue_hella = sangue_hella - atk_player #Sangue do Gudom menos o ataque do player
            pontuacao += 50
            print("Boa! \nSeu ataque acertou em cheio.")
            print(" ")
            print("Barra de sangue: \nHella:",sangue_hella,"/ Player:",sangue_player)#Mostra o sangue do Gudom e do Player
        #Escolha errada
        elif opcao == 2:
            #Não acontece nada
            pontuacao += 0
            print("Você desviou, mas Hella não havia te atacado.")
            print(" ")
            print("Barra de sangue: \nHella:",sangue_hella,"/ Player:",sangue_player)#Mostra o sangue do Gudom e do Player
            print(" ")
            print("Ela te ataca novamente!")
        #Escolha errada, 
        elif opcao == 3:
            #Não acontece nada
            pontuacao += 0
            print("Você defendeu, mas Hella não havia te atacado.")
            print(" ")
            print("Barra de sangue: \nHella:",sangue_hella,"/ Player:",sangue_player)#Mostra o sangue do Gudom e do Player
            print(" ")
        elif opcao<=0 or opcao>3:
            print("Opção invalida, escolha de novo! A Deusa vem para o ataque!\nVocê deve escolher uma das opções: \n1-Atacar \n2-Desviar \n3-Defender \nEscolha!")
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(" ")
        print("A Deusa te ataca novamente!!") 
            
    #Escolha correta
    elif opcao == 3:
        #O sangue do player não altera
        pontuacao += 50
        print("Boa guerreiro(a)! \nO ataque de Hella não teve efeito, ela apenas se cansou.\nContinue assim!")
        print(" ")
        print("Barra de sangue: \nHella:",sangue_hella,"/ Player:",sangue_player)#Mostra o sangue do Gudom e do Player
        print(" ")
        print("Hella recua por conta de seu último movimento.")
        print("Sua hora de agir!")
        print(" ")
        opcao = int(input("Você deve escolher uma das opções: \n1-Atacar \n2-Desviar \n3-Defender \nEscolha!"))
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        #Escolha correta
        if opcao == 1:
            sangue_hella = sangue_hella - atk_player #Sangue do Gudom menos o ataque do player
            pontuacao += 50
            print("Boa! \nSeu ataque acertou em cheio.")
            print(" ")
            print("Barra de sangue: \nHella:",sangue_hella,"/ Player:",sangue_player)#Mostra o sangue do Gudom e do Player
            #Escolha errada
        elif opcao == 2:
            #Não acontece nada
            pontuacao += 0
            print("Você desviou, mas Hella não havia te atacado.")
            print(" ")
            print("Barra de sangue: \nHella:",sangue_hella,"/ Player:",sangue_player)#Mostra o sangue do Gudom e do Player
            print(" ")
            print("A Deusa te ataca novamente!!")
        #Escolha errada
        elif opcao == 3:
            #O sangue do player não altera
            pontuacao += 0
            print("Você defendeu, mas Hella não havia te atacado.")
            print(" ")
            print("Barra de sangue: \nHella:",sangue_hella,"/ Player:",sangue_player)#Mostra o sangue do Gudom e do Player
            print(" ")
        elif opcao<=0 or opcao>3:
            print("Opção invalida, escolha de novo! A Deusa vem para o ataque!\nVocê deve escolher uma das opções: \n1-Atacar \n2-Desviar \n3-Defender \nEscolha!")
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            #Se Hella se cansou vai para o if em que Hella está cansada
        print(" ")
        print("A Deusa te ataca novamente!!")
#Esse if da a mensagem final, e tem a dentação relacionada com o while que representa um ciclo de batalha
        #Caso o jogador coloque um numero que não seja valido
    elif opcao<=0 or opcao>3:
        print("Opção invalida, escolha de novo! A Deusa vem para o ataque!\nVocê deve escolher uma das opções: \n1-Atacar \n2-Desviar \n3-Defender \nEscolha!")
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    if sangue_player <= 0:
        print("Você não foi capaz de honrar sua família.\nReceberá o destino que você merece.")
        print(" ")
        print("Vai para Helheim, um lugar governado por Hella, a deusa da morte e cuidadora \nonde apenas almas que não tiveram uma morte honrosa em batalha na terra, \nhabitam. O seu valor não foi provado para os deuses.")
        #O destino caso você morra em determinada parte está escrito no arquivo do word
        print("Você concluiu entre 0% a 19% do jogo, portanto você é um iniciante!!",)
        print("Sua vida pós batalha é: ",sangue_player)
        print("Sua potuação foi de ,",pontuacao)
        print("Fim de jogo")
        #Este print com asteriscos serve para mostrar o fim do jogo para o jogador
        print("******************************************************************************************************************************************************************")
        break
    #O BREAK NESSE IF é importante. Ele vai parar o programa caso o player morra.
    elif sangue_hella == 0:
        print("Mas ao tentar atacar Hella cai exausta\nBoa guerreiro, você venceu a Deusa da morte. \nVamos para a próxima etapa")
#IMPORTANTE: o programa ainda printa que Hella vai atacar mesmo estando morta. Por isso coloquei que ao tentar atacar ela cai exausta.
#Esse print serve apenas pra conferirmos a variavel pontuação, elaq que nos ajudará a avaliar as escolhas do player no final do jogo.
#Deixei como comentário, tirem caso precisem verificar
#print(pontuacao)
        print(" ")
       
        print("Sua vida pós batalha é: ",sangue_player)
#Lembrando que o print tem que ficar dentro da dentação para depois de vencer a batalha mostrar os pontos e a vida do jogador

#Mas agora é preciso de uma continuação para o programa, todos esse loops fazem que: ou o programa pare ou ele continue rodando mas sem conclusão para a história
#E para isso vou adcionar uma variavel e pedir para o usuario digitar qualquer numero

        progresso=int(input("Para continuar a história digite qualquer número (Não texto): "))
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")

#
#
#
#2° batalha, o Deus da mentira e da trapaça, Loki. 
#Variaveis de batalha.
sangue_loki=1800 #Pontos de vida de Loki
atk_loki=150 #pontos de ataque de Loki
#Vida e ataque do 2° chefe aumentada para ficar mais dificil porem seu estilo de batalha é parecido com o 1° chefe

#Não há necessidade de vincular o progresso, o progresso só serve para pedir um input e continuar a história
if sangue_player>0:
#esse if serve para a continuação da narração
    print("\nApós a derrota de Hella voce guerreiro(a) comemora, porem Loki o pai de Hella chega\na Helheim, vê sua filha derrotada e se enfurece.Loki o meio gigante de gelo e Deus da trapaça e\nda mentira te desafia!")
    print(" ")
    print("O SEU SEGUNDO DESAFIO COMEÇA!")
    print(" ")
    print("Loki está furioso como um mero mortal pode derrotar sua filha.\nEle tem como arma principal suas diversas ilusões e vai para cima!")
    print(" ")

    '''A descricao de Loki como meio gigante de gelo faz com que o jogador tenha que pensar bem e chegar a conclusão de que ele não é tão rápido como Hella'''
'''
Nesta batalha, segue a pontuação das alternativas:
-Quando Loki ataca:
    Atacar = 0
    Desviar = 50
    Defender = 25
    
-Quando Loki está perdido, cansado ou atordoado:
    Atacar = 50
    Desviar = 0
    Defender = 0
'''
#
#
#
#
#Usando o while de novo para um novo ciclo de batalha
while sangue_loki - atk_player > -1 and sangue_player - atk_loki > -149:
#Pode usar a mesma variavel de opcao para outro ciclo de batalha
    opcao = int(input("Você deve escolher uma das opções: \n1-Atacar \n2-Desviar \n3-Defender \nEscolha!"))
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print(" ")
    #Escolha errada
    if opcao == 1:
        sangue_player = sangue_player - atk_loki #Subtração de ataque do chefe na vida do jogador
        pontuacao += 0
        print("Argh, você acertou uma ilusão de Loki! \n Loki te esfaqueia pelas costas.")
        print(" ")
        print("Barra de sangue: \nLoki:",sangue_loki,"/ Player:",sangue_player)
        print("O Deus te ataca novamente!!")
    #Escolha media
    elif opcao == 3:
        sangue_player = sangue_player - (atk_loki/2) #Voce defende e por estar em uma estancia de defesa o ataque do Gudom acerta voce mas tem menos efeito
        pontuacao += 25
        print("Loki te acerta, mas como voce estava em uma posição de defesa o ataque tem menos efeitos\n Loki esta atordoado e suas ilusoes sumiram por voce ter parado parcialmente seu ataque")
        print(" ")
        print("Barra de sangue: \nLoki:",sangue_loki,"/ Player:",sangue_player)
        opcao = int(input("Você deve escolher uma das opções: \n1-Atacar \n2-Desviar \n3-Defender \nEscolha!"))
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        #Escolha correta
        if opcao == 1:
            sangue_loki = sangue_loki - atk_player
            pontuacao += 50
            print("Boa! \nSeu ataque acertou em cheio.")
            print(" ")
            print("Barra de sangue: \nLoki:",sangue_loki,"/ Player:",sangue_player)
        #Escolha errada
        elif opcao == 2:
            #Nao acontece nada
            pontuacao += 0
            print("Você desviou, mas Loki estava atordoado e não atacou.")
            print(" ")
            print("Barra de sangue: \nLoki:",sangue_loki,"/ Player:",sangue_player)
            print(" ")
            print("Loki se recupera, cria suas ilusões e te ataca novamente!")
        #Escolha errada
        elif opcao == 3:
            pontuacao += 0
            print("Você defendeu, mas Loki estava atordoado e não atacou.")
            print(" ")
            print("Barra de sangue: \nLoki:",sangue_loki,"/ Player:",sangue_player)
        elif opcao<=0 or opcao>3:
            print("Opção invalida, escolha de novo! O Deus vem para o ataque!\nVocê deve escolher uma das opções: \n1-Atacar \n2-Desviar \n3-Defender \nEscolha!")
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            #O sangue do player n se altera, respeitar essa dentação de print mais a esquerda
        print(" ")
        print("Loki se recupera, cria suas ilusões e te ataca novamente!")
    #Escolha correta
    elif opcao == 2:
        pontuacao += 50
        print("Boa guerreiro(a)! \n Voce desviou dos ataques de Loki e de suas ilusões e isso fez ele se perder no seu próprio jogo de ilusões\nContinue assim!")
        print(" ")
        print("Barra de sangue: \nLoki:",sangue_loki,"/ Player:",sangue_player)
        print("Loki é obrigado a retirar suas ilusões e agora você pode ver o verdadeiro Deus, é a sua hora de agir!")
        print(" ")
        opcao = int(input("Você deve escolher uma das opções: \n1-Atacar \n2-Desviar \n3-Defender \nEscolha!"))
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        #Escolha correta
        if opcao == 1:
            sangue_loki = sangue_loki - atk_player
            pontuacao += 50
            print("Boa seu ataque acertou em cheio!")
            print(" ")
            print("Barra de sangue: \nLoki:",sangue_loki,"/ Player:",sangue_player)
            #Escolha errada
        elif opcao == 2:
            #Não acontece nada
            pontuacao += 0
            print("Voce desviou, mas Loki estava ainda perdido e nada aconteceu")
            print(" ")
            print("Barra de sangue: \nLoki:",sangue_loki,"/ Player:",sangue_player)
            print(" ")
            print("O Deus finalmente te encontra, cria suas ilusões e te ataca novamente!")
        #Escolha errada
        elif opcao == 3:
            #O sangue do player não se altera
            pontuacao += 0
            print("Voce defendeu, mas Loki estava ainda perdido e nada aconteceu")
            print(" ")
            print("Barra de sangue: \nLoki:",sangue_loki,"/ Player:",sangue_player)
            print(" ")
        elif opcao<=0 or opcao>3:
            print("Opção invalida, escolha de novo! O Deus vem para o ataque!\nVocê deve escolher uma das opções: \n1-Atacar \n2-Desviar \n3-Defender \nEscolha!")
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            #Respeitar essa dentação de print mais a esquerda
        print(" ")
        print("Loki se recupera, cria suas ilusões e ataca novamente!")
#if com dentação relacionada ao while da batalha
    elif opcao<=0 or opcao>3:
        print("Opção invalida, escolha de novo! O Deus vem para o ataque!\nVocê deve escolher uma das opções: \n1-Atacar \n2-Desviar \n3-Defender \nEscolha!")
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    if sangue_player<=0:
        print("Voce não foi capaz de honrar sua familia.\nRecebera o destino que merece")
        print(" ")
        print("Seu corpo é preservado, mas ainda vai para Helheim um lugar governado por Hella,\na Deusa da morte e cuidadora onde apenas almas que não tiveram uma morte honrosa em batalha na terra habitam,\n por preservar seu corpo você vai servir a Hella para ajudar a capturar as almas\n que tiveram uma morte não honrosa.")
        print("Você concluiu entre 20% a 39% do jogo, portanto você é um semiprofissional")
        print("Sua vida pós batalha é: ",sangue_player)
        print("Sua potuação foi de ,",pontuacao)
        print("Fim do jogo")
        print("******************************************************************************************************************************************************************")
        break
    elif sangue_loki == 0:
        print("Mas ao tentar atacar cai no chão e derrotado.\nBoa guerreiro(a), voce derrotou o 2° Gudom, Loki o Deus da trapaça e da mentira!")
    #Use a criatividade porque aqui também printa que Loki mesmo morto vai atacar, por isso ele "cai no chão". Igual Hella.
    #A batalha segue o mesmo esquema da primeira. O intuito agora é dificultar as batalhas fazendo apenas uma opção ser a certa
    #As outras opções farão o jogador perder a vida pelo ataque completo. Não havera pontuação média a partir de agora.
    #Lembrar de sempre printar pós batalha a vida do jogador e sua pontuação até agora
        
        print("Sua vida pós batalha é: ",sangue_player)

        progresso_2= float(input("Para continuar a historia digite qualquer numero: "))
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
#Adcionando uma nova variavel para continuar a historia
#3° batalha contra o exército de Anões
#Variaveis que vão ser utilizadas na batalha
sangue_anoes = 2700
atk_anoes = 200
#ataque aumentado dificultando o jogador




if sangue_player>0:
    print("Após a derrota de Loki o Deus da trapaça e da mentira você consegue sair de Helheim")
    print(" ")
    print("O SEU TERCEIRO DESAFIO COMEÇA!")
    print(" ")
    print("Agora segue para Nidavellir onde existem enormes campos porem sem muita claridade")
    print("Nidavellir é a terra dos anões, eximios ferreiros e conhecidos por pelas suas habilidades na forja")
    print("os deuses te indicam como próximo desafio o exercito de 600 ferreiros anões.")
    print("Ao andar um pouco mais para frente já pode ouvir os inumeros passos dos ferreiros envolta de você")
    print("os anões são muitos, te cercam e se preparam para atacar de todas as direções.")
    print("Cerca de 100 anões pulam diretamente para você de todas as direções")

'''Ao ser cercado pelos anões não resta muitas opções para o jogador a não ser atacar sem parar até acabar com todos os anões'''
'''
    Nesta batalha as opções não são vastas, ou você ataca ou toma dano:
    -Quando os anões atacarem:
        Atacar = 50
        Defender = 0
        Desviar = 0
'''
#Usando while para um ciclo de batalha
#Nesta batalha terão menos anotações para a visualização do código estar mais fácil
while sangue_anoes - atk_player > -1 and sangue_player - atk_anoes > -199:
    opcao = int(input("Você deve escolher uma das opções: \n1-Atacar \n2-Desviar \n3-Defender \nEscolha!"))
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print(" ")
    if opcao==1:
        sangue_anoes = sangue_anoes - atk_player
        pontuacao += 50
        print("O seu ataque é fantástico! Consegue derrotar muitos anões de uma só vez!")
        print(" ")
        print("Barra de vida\nAnões: ",sangue_anoes,"Player: ",sangue_player)
        print("Os anões se preparam para atacar novamente!")
    elif opcao==2:
        sangue_player = sangue_player - atk_anoes
        pontuacao += 0
        print("Você tenta desviar mas não consegue por não ter para onde desviar e toma diversos ataques dos anões de todas as direções")
        print(" ")
        print("Barra de vida\nAnões: ", sangue_anoes,"Player: ",sangue_player)
        print("Os anões se preparam para atacar novamente!")
    elif opcao==3:
        sangue_player = sangue_player - atk_anoes
        pontuacao += 0
        print("Você tenta defender mas não consegue por não conseguir proteger o corpo inteiro e toma diversos ataques dos anões pelas costas")
        print(" ")
        print("Barra de vida\nAnões: ",sangue_anoes,"Player: ",sangue_player)
        print("Os anões se preparam para atacar novamente!")
    elif opcao<=0 or opcao>3:
        print("Opção invalida, escolha de novo! O Deus vem para o ataque!\nVocê deve escolher uma das opções: \n1-Atacar \n2-Desviar \n3-Defender \nEscolha!")
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
#Este if não tem problema em ser colocado aqui pois determina o fim do ciclo while de batalha
    if sangue_player<=0:
        print("Voce morreu e não foi capaz de honrar sua familia.\nRecebera o destino que merece")
        print(" ")
        print("O seu destino é trabalhar com os anões em Nidavellir, 'os campos escuros,'\né a terra dos anões na mitologia nórdica. Os anões são exímios ferreiros\n com habilidades incríveis, porem são gananciosos perante metais preciosos.\nVivem na escuridão pois a luz do Sol os transforma em pedra. O seu destino é trabalhar como\n um ferreiro(a) com eles pela eternidade.")
        print("Você concluiu 40% a 59% do jogo, portanto você é um profissional!!")
        print("Sua vida pós batalha é: ",sangue_player)
        print("Sua potuação foi de ,",pontuacao," e sua porcentagem exata é ",pontuacao//29,"%")
        print("Fim do jogo")
        print("******************************************************************************************************************************************************************")
        break
    elif sangue_anoes == 0:
        print("Mas ao ver os anões chegando para um próximo ataque todos foram lentamente\nparando e se transformando em pedra. O 3° Gudom,exercito de anões, foi derrotado pois os deuses\nviram que você já tinha lutado demais contra o exército incansavel deles e\nabriram os Céus dos campos escuros de Nidavellir. A luz do Sol transforma\nos anões em pedra e agora você tem a oportunidade de ir para o seu próximo desafio")
        print("Agora o 3° Gudom, o exercito de anões de Nidavellir está derrotado")
        
        print("Sua vida pós batalha é: ",sangue_player)

        progresso_3= float(input("Para continuar a historia digite qualquer numero: "))
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
#Agora para continuar o programa lembrar de colocar a variavel para o jogador digitar algo e sua condição interligada com AND com a vida do player.
#NESTA BATALHA EXISTE UM BUG. MESMO COM 0 DE VIDA O JOGADOR TEM DIREITO A UMA AÇÃO.
#Pelo menos com qualquer ação tomada resulta na morte dele no próximo print e com sua classificação e destinos corretos
#O problema é que houveram testes em que a vida do jogador primeiro chega a 0 e de Jera no proximo ataque chega a 0. Mas isso ainda resulta na morte e fim do jogo pro jogador
sangue_jera= 3600
atk_jera = 500
atk_player_novo=900
if sangue_player>0:
    print("Após derrotar o exército de anões, você vai para Alfheim",
          "\n",
          "\nO SEU QUARTO DESAFIO COMEÇA!",
          "\n",
          "\nNo caminho de Alfheim, os deuses decidem ter dar um presente, uma espada poderosa que aumenta o seu dano, subindo de 450 para 900"
          "\nNeste mundo existe um ser gigante em forma de mulher, Jera"
          "\nEla possui 4 tentáculos e ela é feita de madeira mágica que pode ser retorcida e maleada como ela quiser",
          "\nOs deuses te indicam ela como seu quarto desafio!"
          "\nAo chegar perto dela, ela se enfurece e parte para batalha"
          "\nPara derrota-la, você terá que cortar os 4 tentáculos dela!!")
"""
modelo de batalha:
-Quando Jera ataca:
    Atacar = 0
    Desviar = 50
    Defender = 0
-Quando Jera está cansada:
    Atacar = 50
    Desviar = 0
    Defender = 0
"""
while sangue_jera - atk_player_novo > -1 and sangue_player - atk_jera > -499:
    opcao = int(input("Você deve escolher uma das opções: \n1-Atacar \n2-Desviar \n3-Defender \nEscolha!"))
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("")
    #Escolha errada
    if opcao == 1:
        sangue_player = sangue_player - atk_jera #Subtração de ataque do chefe na vida do jogador
        pontuacao += 0
        print("Você tenta cortar um dos tentáculos dela, porem seu ataque foi inútil e ela te acerta diretamente!!",
              "\nJera fica mais enfurecida e decide atacar novamente!!",
              "\nBarra de sangue: \nJera:",sangue_jera,"/ Player:",sangue_player)
    #Escolha média, aqui também fui obrigado a mudar pois o jogador pode burlar o sistema caso consiga muitas defesas e sobreviva por muito tempo acumulando pontos de defesa
    elif opcao == 3 and sangue_player >0 :
        sangue_player = sangue_player - (atk_jera/2) #Subtração de ataque do chefe na vida do jogador
        pontuacao += 0
        print("Jera te acerta em cheio, porem como você estava em posição de defesa, o ataque dela causou menos dano!!",
              "\nJera fica cansada!!",
              "\nBarra de sangue: \nJera:",sangue_jera,"/ Player:",sangue_player)
        opcao = int(input("Você deve escolher uma das opções: \n1-Atacar \n2-Desviar \n3-Defender \nEscolha!"))
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        #Escolha certa
        if opcao == 1:
                sangue_jera = sangue_jera - atk_player_novo
                pontuacao += 0
                print("Você mira em um dos tentáculos de Jera e consegue corta-lo!!",
                      "\nJera se enfurece e prepara para o proximo ataque!!",
                      "\nBarra de sangue: \nJera:",sangue_jera,"/ Player:",sangue_player)
        #Escolha errada
        elif opcao == 2:
                #Vida não muda
                pontuacao += 0
                print("Você desvia de Jera, porem ela não estava atacando!!",
                      "\nJera descansa, portanto prepara o proximo ataque!!",
                      "\nBarra de sangue: \nJera:",sangue_jera,"/ Player:",sangue_player)
        #Escolha errada
        elif opcao == 3:
                #Vida não muda
                pontuacao += 0
                print("Você defende de Jera, porem ela não estava atacando!!",
                      "\nJera descansa, portanto prepara o proximo ataque!!",
                      "\nBarra de sangue: \nJera:",sangue_jera,"/ Player:",sangue_player)
    #Escolha certa
    elif opcao == 2:
        #Vida não muda
        pontuacao += 50
        print("Sabia escolha, você desvia totalmente do ataque de Jera!!",
              "\nJera fica cansada!!",
              "\nBarra de sangue: \nJera:",sangue_jera,"/ Player:",sangue_player)
        opcao = int(input("Você deve escolher uma das opções: \n1-Atacar \n2-Desviar \n3-Defender \nEscolha!"))
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        #Escolha certa
        if opcao == 1:
                sangue_jera = sangue_jera - atk_player_novo
                pontuacao += 50
                print("Você mira em um dos tentáculos de Jera e consegue corta-lo!!",
                      "\nJera se enfurece e prepara para o proximo ataque!!",
                      "\nBarra de sangue: \nJera:",sangue_jera,"/ Player:",sangue_player)
        #Escolha errada
        elif opcao == 2:
                #Vida não muda
                pontuacao += 0
                print("Você desvia de Jera, porem ela não estava atacando!!",
                      "\nJera descansa, portanto prepara o proximo ataque!!",
                      "\nBarra de sangue: \nJera:",sangue_jera,"/ Player:",sangue_player)
        #Escolha errada
        elif opcao == 3:
                #Vida não muda
                pontuacao += 0
                print("Você defende de Jera, porem ela não estava atacando!!",
                      "\nJera descansa, portanto prepara o proximo ataque!!",
                      "\nBarra de sangue: \nJera:",sangue_jera,"/ Player:",sangue_player)
#if com dentação relacionada ao while da batalha
    elif opcao<=0 or opcao>3:
        print("Opção invalida, escolha de novo! O Deus vem para o ataque!\nVocê deve escolher uma das opções: \n1-Atacar \n2-Desviar \n3-Defender \nEscolha!")
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    if sangue_player<=0:
        print("Voce não foi capaz de honrar sua familia.\nRecebera o destino que merece",
              "\n",
              "\nVai para Alfheim, o mundo dos elfos luminosos e justos como o Sol.",
              "\nEsse mundo é governado por Freya, a deusa da prosperidade, das boas colheitas e da agricultura, dos casamentos e da fertilidade, da alegria e da paz.",
              "\nPoderá viver uma vida tranquila como ajudante a manter a paz ao lado de Freya mas não pode ir para Asgard e nem para Valhalla e reencontrar sua família.",
              "\nVocê concluiu 60% a 79% do jogo, portanto você é um mestre!!",
              "\nSua vida pós batalha é: ",sangue_player,
              "\nSua potuação foi de ,",pontuacao,
              "\nFim do jogo")
        print("******************************************************************************************************************************************************************")
        #Usar isso em todas as partes de morte e final de jogo "\nA porcentagem que voce fez do jogo",math.ceil((pontuacao/pontuacao_total)*100),"%")
        break
        
                      
    elif sangue_jera == 0:
        print("Você corta o último tentáculo de Jera,",
        "\nEla começa a gritar de dor,",
        "\nVocê vê o corpo de Jera secando, virando cinzas,",
        "\nAgora o 4º Gudom, Jera está derrotado!!",
        
        "\nSua vida pós batalha é: ",sangue_player)

        progresso_4= float(input("Para continuar a historia digite qualquer numero: "))
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
sangue_sutir= 4500
atk_sutir = 1000
if sangue_player>0:
    print("Após derrotar Jera, você é mandado para Muspellheim, a terra dos gigantes de fogo e dos demônios.,"
          "\n",
          "\nO SEU ÚLTIMO DESAFIO COMEÇA!",
          "\nNessa terra existe um Gudom chamado Sutir, gigante de fogo mais forte de todos que está destinado a enfrentar Freya no fim dos tempos, o Ragnarok.",
          "\nOs seus ataques tem uma velocidade média, ele solta rajadas de fogo e tomar um ataque dele é morte instantânea.",
          "\nOs deuses te indicam ele como seu quinto e último desafio!",
          "\nAo se aproximar dele, você percebe que sua espada está quebrada por causa da batalha contra Jera.",
          "\nSeu ataque volta a ser 450.",
          "\nSutir fica furioso por você ter se aproximado dele e começa a preparar seu ataque!!",
          "\nessa terra é cheia de pedras, use-as ao seu favor!!!",
          "\nSutir ataca fisicamente primeiro, depois usa sua bola de fogo!!!",
          "\nEspere o momento certo para poder atacar Sutir e derrota-lo!!")
"""
Como essa batalha ira terminar em  final bom (não perfeito)
Mesmo com a derrota irei fazer somente pontuação positiva,
Menos na parte que Sutir está sobreaquecido,
que sera 0 se escolher opção errada
Modelo de batalha:
-Quando Sutir atacar fisicamente:
    Atacar = 0
    Desviar = 50
    Defender = 0
    Ficar atras da pedra = 0
-Quando Sutir atacar com sua rajada de fogo:
    Atacar = 0
    Desviar = 0
    Defender = 0
    Ficar atras da pedra = 50
-Quando Sutir estiver sobreaquecido:
    Atacar = 50
    Desviar = 0
    Defender = 0
    Ficar atras da pedra = 0

"""
while sangue_sutir - atk_player> -1 and sangue_player - atk_sutir > -999:
    opcao = int(input("Você deve escolher uma das opções: \n1-Atacar \n2-Desviar \n3-Defender \n4-Esconder-se atras de uma pedra \nEscolha!"))
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("")
    #Opção errada
    if opcao == 1:
        sangue_player = sangue_player - atk_sutir
        
        print("Você tenta acerta-lo em cheio, porem ele te acerta antes!!",
              "\nBarra de sangue: \nSutir:",sangue_sutir,"/ Player:",sangue_player)
    #Opção certa
    elif opcao == 2:
        #Vida não muda
        pontuacao += 50
        print("Você tenta desviar de seu ataque e consegue!!",
              "\nSutir prepara seu ataque com bola de fogo!!",
              "\nBarra de sangue: \nSutir:",sangue_sutir,"/ Player:",sangue_player)
        opcao = int(input("Você deve escolher uma das opções: \n1-Atacar \n2-Desviar \n3-Defender \n4-Esconder-se atras de uma pedra \nEscolha!"))
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("")
        #Opção errada
        if opcao == 1:
            sangue_player = sangue_player - atk_sutir
            
            print("Você tenta atacar sutir, porem ele te acerta com sua bola de fogo!!",
                  "\nBarra de sangue: \nSutir:",sangue_sutir,"/ Player:",sangue_player)
        #Opção errada
        elif opcao == 2:
            sangue_player = sangue_player - atk_sutir
            
            print("Você tenta desviar do ataque de sutir, porem ele te acerta com sua bola de fogo!!",
                  "\nBarra de sangue: \nSutir:",sangue_sutir,"/ Player:",sangue_player)
        #Opção errada
        elif opcao == 3:
            sangue_player = sangue_player - atk_sutir
            
            print("Você tenta defender o ataque sutir, porem ele te acerta com sua bola de fogo!!",
                  "\nBarra de sangue: \nSutir:",sangue_sutir,"/ Player:",sangue_player)
        #Opcão certa
        elif opcao == 4:
            #A vida não muda
            pontuacao += 50
            print("Saiba escolha, você escondeu-se atras de uma pedra, prevenindo todo o dano que Sutir iria te causar!!",
                  "\nSutir está sobreaquecido por causa de sua bola de fogo, portanto ficou cansado e não irá atacar!!",
                  "\nBarra de sangue: \nSutir:",sangue_sutir,"/ Player:",sangue_player)
            opcao = int(input("Você deve escolher uma das opções: \n1-Atacar \n2-Desviar \n3-Defender \n4-Esconder-se atras de uma pedra \nEscolha!"))
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("")
            #Opção certa
            if opcao == 1:
                sangue_sutir = sangue_sutir - atk_player
                pontuacao += 50
                print("Seu ataque acerta Sutir em cheio!!",
                      "\nSutir não está mais sobreaquecido, portanto prepara seu próximo ataque físico!!",
                      "\nBarra de sangue: \nSutir:",sangue_sutir,"/ Player:",sangue_player)
            #Opção errada
            elif opcao == 2:
                #Vida não muda
                print("Você tenta desviar de Sutir, porem ele não estava pronto para o ataque, portanto não acontece nada!!",
                      "\nSutir não está mais sobreaquecido, portanto prepara seu próximo ataque físico!!",
                      "\nBarra de sangue: \nSutir:",sangue_sutir,"/ Player:",sangue_player)
            #Opção errada
            elif opcao == 3:
                #Vida não muda
                print("Você tenta defender-se de Sutir, porem ele não estava pronto para o ataque, portanto não acontece nada!!",
                      "\nSutir não está mais sobreaquecido, portanto prepara seu próximo ataque físico!!",
                      "\nBarra de sangue: \nSutir:",sangue_sutir,"/ Player:",sangue_player)
            elif opcao == 4:
                #Vida não muda
                print("Você se esconde atras de uma pedra, porem sutir não estava pronto para o ataque, portanto não acontece nada!!",
                      "\nSutir não está mais sobreaquecido, portanto prepara seu próximo ataque físico!!",
                      "\nBarra de sangue: \nSutir:",sangue_sutir,"/ Player:",sangue_player)
    #Opção errada
    elif opcao == 3:
        sangue_player = sangue_player - atk_sutir
        
        print("Você tenta defender o ataque de Sutir, porem ele te acerta mesmo assim com todo seu poder!!",
              "\nBarra de sangue: \nSutir:",sangue_sutir,"/ Player:",sangue_player)
    elif opcao == 4:
        sangue_player = sangue_player - atk_sutir
        
        print("Você se esconde atras de uma pedra, porem ele destroi a pedra e te acerta com todo seu poder!!",
              "\nBarra de sangue: \nSutir:",sangue_sutir,"/ Player:",sangue_player)
    elif opcao<=0 or opcao>3:
        print("Opção invalida, escolha de novo! O Deus vem para o ataque!\nVocê deve escolher uma das opções: \n1-Atacar \n2-Desviar \n3-Defender \n4-Esconder-se atras de uma pedra \nEscolha!")
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    if sangue_player<=0:
        print("Você morre nessa batalha, porem os Deuses te dão o direito de ir para Valhalla pois Sutir nunca foi derrotado por nenhum humano.",
              "\nVocê consegue reencontar seu pai e irmão!!",
              "\nVocês comemoram pela eternidade!!",
              "\nVocê concluiu 80% a 99% do jogo e é um grão-mestre!!",
              "\nSua vida pós batalha é: ",sangue_player,
              "\nSua potuação foi de ,",pontuacao,
              "\nFim do jogo")
        print("******************************************************************************************************************************************************************")
        break
    elif sangue_sutir == 0 and sangue_player != 1000:
        print("Você consegue derrotar Sutir!!",
              "\nOs Deuses te dão a permissão para viver em Valhalla!!",
              "\nVocê consegue reencontar seu pai e irmão!!",
              "\nVocês comemoram pela eternidade!!",
              "\nVocê concluiu mais de 80% a 99% do jogo, portanto você é um grão-mestre!!",
              "\nSua vida pós batalha é: ",sangue_player,
              "\nSua potuação foi de ,",pontuacao,
              "\nExiste um final secreto para esse jogo!!",
              "\nJogue novamente e tente não perder vida para desbloquear o final secreto!!",
              "\nFim do jogo")
        print("**************************************************************************************************************************************************************************************************************")
        break
    elif sangue_sutir == 0 and sangue_player == 1000:
        print("Você consegue derrotar Sutir!!",
              "\nVocê foi tão bem reconhecido pelos Deuses que eles te dão o poder de um Deus nórdico,"
              "\nPodendo viver ao lado deles em Asgard,",
              "\nUma honra muito maior que os salões de Valhalla.",
              "\nAlém de poder visitar e comemorar com sua família,",
              "\nVocê terá um poder de uma Divindade, o poder de um Gudom!!",
              "\nVocê consegue reencontar seu pai e irmão!!",
              "\nVocês comemoram pela eternidade!!",
              "\nVocê concluiu 100% do jogo, portanto você é um Gudom!!",
              "\nSua vida pós batalha é: ",sangue_player,
              "\nSua potuação foi de ,",pontuacao,
              "\nEste é o final secreto!!",
              "\nParabens por conseguir completar ele!!",
              "\nFim do jogo")
        print("**************************************************************************************************************************************************************************************************************")
        break

        
        

#Lembrar de mostrar a pontuação em porcentagem no final do programa
       
    
    
    
