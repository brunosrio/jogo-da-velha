import time
import os

def atualizar_tabuleiro(tabuleiro):
    tab_string = ""
    for i in range(3):
        tab_string += f" {tabuleiro[i][0]} | {tabuleiro[i][1]} | {tabuleiro[i][2]} \n"
        tab_string += f"{'-' * 11}\n"
    
    return tab_string

def verificar_vitoria(tabuleiro):
    #vericar vitoria pelas linhas
    for linha in range(3):
        if tabuleiro[linha][0] != "*":
            if tabuleiro[linha][0] == tabuleiro[linha][1] and tabuleiro[linha][1] == tabuleiro[linha][2]:
                return True

    #verificar vitoria pelas colunas
    for coluna in range(3):
        if tabuleiro[0][coluna] != "*":
            if tabuleiro[0][coluna] == tabuleiro[1][coluna] and tabuleiro[1][coluna] == tabuleiro[2][coluna]:
                return True    
        
     #verificar vitoria diagonal principal
    if tabuleiro[0][0] != "*":
        if tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][2]:
            return True
    
    #verificar vitoria diagonal secundaria
    if tabuleiro[0][2] != "*":
        if tabuleiro[0][2] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][0]:
            return True

    return False

def main(vitoriasX=0, vitoriasO=0, empates=0, jogador_x=None, jogador_o=None):
    if (jogador_x == None):
        jogador_x = input("jogador X. Digite seu nome: ")
        jogador_o = input("jogador Y. Digite seu nome: ")
    
    num_jogadas = 0
    x_ou_o = "X"
    jogador_da_vez = jogador_x
    tabuleiro = [["*" for i in range(3)] for i in range(3)]
    while (True):
        num_jogadas += 1
        os.system('cls' if os.name == 'nt' else 'clear')

        print(f"{atualizar_tabuleiro(tabuleiro)}")

        print(f"JOGADA {num_jogadas} | JOGADOR DA VEZ: {jogador_da_vez.upper()} -> {x_ou_o}")
        print('=' * 30)
        print(f"Placar: {vitoriasX} vitórias para {jogador_x} | {vitoriasO} vitórias para {jogador_o} | {empates} empates")
        print('=' * 30)
        print("Insira o posição da jogada: linha(de 1 a 3) e depois a coluna(de 1 a 3)")
        
        linha = int(input("linha: "))
        coluna = int(input("coluna: "))
        tabuleiro[linha-1][coluna-1] = x_ou_o
        
        if verificar_vitoria(tabuleiro):
            if x_ou_o == "X":
                vitoriasX += 1
            else:
                vitoriasO += 1
            
            print(f"{'=' * 30}\nVITÓRIA DE {jogador_da_vez.upper()}!\n{'=' * 30}")
            print(f"{atualizar_tabuleiro(tabuleiro)}")
            
            time.sleep(4)
            return main(vitoriasX, vitoriasO, empates, jogador_x, jogador_o)    

        if num_jogadas == 9:
            empates += 1
            print(f"{'=' * 30}\nEMPATE!\n{'=' * 30}")
            print(f"{atualizar_tabuleiro(tabuleiro)}")

            time.sleep(4)
            return main(vitoriasX, vitoriasO, empates, jogador_x, jogador_o)

        x_ou_o= "O" if x_ou_o == "X" else "X"
        jogador_da_vez = jogador_x if jogador_da_vez == jogador_o else jogador_o

main()
