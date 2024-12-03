from aluno import *
from entrada import *
from navegabilidade import *

# Variáveis de controle dos dados na memória
id = 1
alunos = []  # Lista de dicionários que armazena as abstrações de alunos

while True:
    imprimir_cabecalho()
    exibir_menu()
    opc = ler_inteiro("Opção: ")

    # Navegabilidade
    if opc == 1:
        aluno = ler_dados_aluno(alunos)  # Passa a lista de alunos como argumento
        alunos.append(aluno)  # Adiciona o dicionário na lista de alunos
    elif opc == 2:
        imprimir_alunos(alunos)  # Chama a função para imprimir todos os alunos
    elif opc == 3:
        id_aluno = int(input("Digite o ID do aluno que deseja buscar: "))
        buscar_aluno_por_id(alunos, id_aluno)  # Chama a função para buscar um aluno por ID
    elif opc == 4:
        imc_minimo = float(input("Digite o valor mínimo de IMC para filtrar: "))
        filtrar_alunos_por_imc(alunos, imc_minimo)  # Chama a função para filtrar alunos por IMC
    elif opc == 5:
        if salvar_dados_e_perguntar(alunos):  # Chama a função para salvar dados e pergunta se deseja sair
            break
    else:
        print("Opção inválida!")

    limpar_tela()