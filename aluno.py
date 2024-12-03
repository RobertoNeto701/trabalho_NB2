from entrada import *

def ler_dados_aluno(lista_de_alunos):
    """Função que lê os dados de um aluno e retorna um dicionário."""
    nome = input("Digite o nome do aluno: ")
    peso = float(input("Digite o peso do aluno (kg): "))
    altura = float(input("Digite a altura do aluno (m): "))
    id_aluno = len(lista_de_alunos) + 1  # Gerando um ID simples baseado no tamanho da lista
    return {'id': id_aluno, 'nome': nome, 'peso': peso, 'altura': altura}

def imprimir_alunos(lista_alunos):
    """Função que imprime todos os alunos na tela."""
    if not lista_alunos:
        print("Nenhum aluno cadastrado.")
        return
    print("Lista de Alunos:")
    for aluno in lista_alunos:
        print(f"ID: {aluno['id']}, Nome: {aluno['nome']}, Peso: {aluno['peso']} kg, Altura: {aluno['altura']} m")

def buscar_aluno_por_id(lista_alunos, id):
    """Busca um aluno por ID e apresenta seus dados se existir."""
    for aluno in lista_alunos:
        if aluno.get('id') == id:
            print(f"Aluno encontrado: ID: {aluno['id']}, Nome: {aluno['nome']}, Peso: {aluno['peso']} kg, Altura: {aluno['altura']} m")
            return
    print("Aluno não encontrado.")

def calcular_imc(aluno):
    """Calcula o IMC do aluno."""
    return aluno['peso'] / (aluno['altura'] ** 2)

def filtrar_alunos_por_imc(lista_alunos, imc_minimo):
    """Exibe uma lista de alunos com IMC acima do valor mínimo especificado."""
    alunos_filtrados = []
    
    for aluno in lista_alunos:
        imc = calcular_imc(aluno)
        if imc >= imc_minimo:
            alunos_filtrados.append(aluno)

def salvar_dados_e_perguntar(lista_alunos):
    """Salva os dados dos alunos e pergunta se o usuário deseja sair do programa."""
    print("Dados dos alunos salvos com sucesso!")
    
    while True:
        resposta = input("Deseja sair do programa? (s/n): ").strip().lower()
        if resposta in ['s', 'sim']:
            print("Saindo do programa...")
            return True
        elif resposta in ['n', 'não']:
            print("Continuando o programa...")
            return False
        else:
            print("Resposta inválida. Por favor, digite 's' para sim ou 'n' para não.")
