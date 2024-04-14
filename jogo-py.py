from copy import deepcopy
from os import system, name
from time import sleep

def inicializa_tabuleiro():
    return [['*' for i in range(3)] for i in range(3)]

def inicializa_estado():
    tabuleiro = inicializa_tabuleiro()
    estado = {'tab': tabuleiro, 'vitX': 0, 'vitO': 0, 'empt': 0}

    return estado

def altera_placar(estado, vitX=None, vitO=None):
    novo_estado = deepcopy(estado)  
    if (vitX):
        novo_estado['vitX'] += 1
    elif (vitO):
        novo_estado['vitO'] += 1
    else:
        novo_estado['empt'] += 1

    return novo_estado

def altera_tabuleiro(estado, posicao=None, x_ou_o=None):
    novo_estado = deepcopy(estado)
    tabuleiro = novo_estado['tab']
    tabuleiro[int(posicao[0]) - 1][int(posicao[1]) - 1] = x_ou_o
    novo_estado['tab'] = tabuleiro

    return novo_estado

def get_tabuleiro(tabuleiro):
    tab = ""
    for i in range(3):
        tab += f" {tabuleiro[i][0]} | {tabuleiro[i][1]} | {tabuleiro[i][2]} \n"
        tab += f"{'-' * 11}\n"
    
    return tab

def get_placar(estado):
    placar = ""
    placar += f"vitorias de X: {estado['vitX']} | "
    placar += f"vitorias de O: {estado['vitO']} | " 
    placar += f"empates: {estado['empt']}"

    return placar

def get_empate_msg(estado):
    msg = ""
    msg += f"{'=' * 15}\nEMPATE\n{'=' * 15}\n"
    msg += f"\n{get_placar(estado)}\n"
    msg += f"\n{get_tabuleiro(estado['tab'])}"

    return msg

def get_vitoria_msg(estado, x_ou_o):
    msg = ""
    msg += f"{'=' * 15}\nVITORIA DE {x_ou_o}\n{'=' * 15}\n"
    msg += f"\n{get_placar(estado)}\n"
    msg += f"\n{get_tabuleiro(estado['tab'])}"

    return msg

def get_msg_inicial(estado, x_ou_o):
    msg = ""
    msg += f"{get_placar(estado)}\n"
    msg += f"\n{get_tabuleiro(estado['tab'])} \n"
    msg += f"Jogador da vez: {x_ou_o}"

    return msg

def verifica_linha_igual(tabuleiro):
    for linha in range(3):
        if tabuleiro[linha][0] != "*":
            if tabuleiro[linha][0] == tabuleiro[linha][1] and tabuleiro[linha][1] == tabuleiro[linha][2]:
                return True
    
    return False

def verifica_coluna_igual(tabuleiro):
    for coluna in range(3):
        if tabuleiro[0][coluna] != "*":
            if tabuleiro[0][coluna] == tabuleiro[1][coluna] and tabuleiro[1][coluna] == tabuleiro[2][coluna]:
                return True
    
    return False

def verifica_diagonais(tabuleiro):
    if tabuleiro[0][0] != "*":
        if tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][2]:
            return True
        
    #verificar vitoria diagonal secundaria
    if tabuleiro[0][2] != "*":
        if tabuleiro[0][2] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][0]:
            return True
        
    return False

def verifica_vitoria(tabuleiro):
    if verifica_linha_igual(tabuleiro):
        return True
    elif verifica_coluna_igual(tabuleiro):
        return True
    elif verifica_diagonais(tabuleiro):
        return True
    else:
        return False

def verifica_empate(tabuleiro):
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == "*":
                return False
    
    return True

def define_ganhador(estado, jogador_da_vez):
    if jogador_da_vez == 'X':
        return altera_placar(estado, True, False)            
    else:
        return altera_placar(estado, False, True)

def limpar_tela():
    system('cls' if name == 'nt' else 'clear')

def main(estado=None):
    x_ou_o = 'X'
    if (estado is None):
        estado = deepcopy(inicializa_estado())
    
    while (True):
        limpar_tela()
        print(f"{get_msg_inicial(estado, x_ou_o)}")
        
        posicao = input("Insira a posicao(de 1 a 3 | linha coluna) da jogada(q para sair): ")
        if posicao.strip() == "q":
            print(f"{get_placar(estado)}")
            break
        
        estado = deepcopy(altera_tabuleiro(estado, posicao.split(" "), x_ou_o))
                
        if verifica_vitoria(estado['tab']):
            estado = deepcopy(define_ganhador(estado, x_ou_o))
            limpar_tela()
            print(f"{get_vitoria_msg(estado, x_ou_o)}")
            
            estado['tab'] = inicializa_tabuleiro()
            sleep(6)
            return main(estado)

        elif verifica_empate(estado['tab']):
            estado = deepcopy(altera_placar(estado, False, False))
            limpar_tela()
            print(f"{get_empate_msg(estado)}")
            
            estado['tab'] = inicializa_tabuleiro()
            sleep(6)
            return main(estado)
        
        else:
            x_ou_o = "X" if x_ou_o == "O" else "O"

main()