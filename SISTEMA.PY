import time
import math
import os
import gspread
import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import ttk
from itertools import cycle
from tkinter import filedialog
from selenium import webdriver
from google.auth import exceptions
from google.auth.transport.requests import Request
from google.oauth2 import service_account
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service

nomes_arquivos_salvos = []
# Escopo de acesso para leitura e escrita em planilhas
scope = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

# Credenciais do arquivo JSON obtido do Console de APIs do Google Cloud
creds1 = service_account.Credentials.from_service_account_file('automacaomanuais-6aa.json', scopes=scope)
creds2 = service_account.Credentials.from_service_account_file('automacaomanuais-99.json', scopes=scope)
creds3 = service_account.Credentials.from_service_account_file('automacaomanuais-67f.json', scopes=scope)
creds4 = service_account.Credentials.from_service_account_file('automacaomanuais-7ad.json', scopes=scope)
creds5 = service_account.Credentials.from_service_account_file('automacaomanuais-734d.json', scopes=scope)

# Use the 'open_by_key' method to open a spreadsheet by its key
bots = [
    gspread.service_account(filename='automacaomanuais-6aa4.json'),
    gspread.service_account(filename='automacaomanuais-990c8.json'),
    gspread.service_account(filename='automacaomanuais-67f5.json'),
    gspread.service_account(filename='automacaomanuais-7ade.json'),
    gspread.service_account(filename='automacaomanuais-73.json')
]
''' ===================================================================================='''
''' ===================================================================================='''
''' ===================================================================================='''
''' ====================================FUNCOES========================================='''
linha_atual = 1
def menu():
    # Simulando a entrada do usuário
    opcao = input("Digite a opção desejada \n1 para distribuir listas, \n2 para disparar, \n3 para criar a planilha de consulta no drive, \n4 para atualizar a planilha dos individuais no drive): ")

    # Verifica a opção selecionada e executa a ação correspondente
    if opcao == '1':
        print("Distribuir as listas")
        distribuir(df_concatenado)

    elif opcao == '3':
        print("Atualizar as planilhas dos individuais")
        consulta()
        
    elif opcao == '4':
        print("Atualizar as planilhas dos individuais")
        individuais()

    elif opcao == '5':
        print("Dados da lista")
        dados()

    else:
        print("Opção inválida. Por favor, escolha 1, 2 ou 3.")



def distribuir(df):
    nomes = ['A**** G****', 'E********** B******', 'H***** S******', 'I****** ** C****', 'R***** M***',
    'M**** V******', 'M***** B*****', 'M***** M****', 'G****** O*******', 'P**** H********',
    'R***** M*******', 'S***** M****', 'S*** L*****',

    'B**** S****', 'C*** N*******','D**** K****', 'D****** E*******', 'G****** S****', 'G********* A******', 'I****** A*****',
    'Í**** R****', 'L*** M*****', 'M****** O*******', 'M******* B*******', 'P**** A****',
    'S*** C****',

    'B**** O******', 'B**** K********', 'D***** S****', 'E****** K******',
    'G******* B*************', 'J***** S******', 'M***** A******', 'M***** L****', 'R***** S****',
    'R***** B*********', 'R****** R********', 'T****** R****', 'T******* C****', 'T***** S********'
    ]
        
    
    # Contando quantos 'INSS' e 'CDC' existem na coluna 'lista' do DataFrame
    qtd_inss = (df['lista'] == 'INSS').sum()
    qtd_cdc = ((df['lista'] == 'CDC').sum())

    # Calculando a quantidade média por nome e arredondando para baixo
    qtd_media_inss = math.floor(qtd_inss / len(nomes))
    qtd_media_cdc = math.floor(qtd_cdc/len(nomes))
    
    informacoes_atendentes = [

            {"nome": "I******* A*****", "quantidade": 300, "lista": "CDC", "tipo": "MANUAL"},
            {"nome": "J*** B******", "quantidade": 300, "lista": "CDC", "tipo": "MANUAL"},
            {"nome": "J*** P****", "quantidade": 300, "lista": "CDC", "tipo": "MANUAL"},
            {"nome": "A**** C*****", "quantidade": 300, "lista": "CDC", "tipo": "MANUAL"},
            {"nome": "P******* V*****", "quantidade": 300, "lista": "CDC", "tipo": "MANUAL"},
            {"nome": "K****** K****", "quantidade": 300, "lista": "CDC", "tipo": "MANUAL"},
            {"nome": "B**** S****", "quantidade": 300, "lista": "CDC", "tipo": "MANUAL"},

            {"nome": "I****** ** C****", "quantidade": 200, "lista": "CDC", "tipo": "MANUAL"},
            {"nome": "C**** L****", "quantidade": 300, "lista": "CDC", "tipo": "MANUAL"},
            {"nome": "S*** L*****", "quantidade": 300, "lista": "CDC", "tipo": "MANUAL"},
            {"nome": "H***** S******", "quantidade": 300, "lista": "CDC", "tipo": "MANUAL"},
            {"nome": "E****** R****", "quantidade": 300, "lista": "CDC", "tipo": "MANUAL"},
            {"nome": "R***** S****", "quantidade": 300, "lista": "CDC", "tipo": "MANUAL"},
            {"nome": "M***** L****", "quantidade": 300, "lista": "CDC", "tipo": "MANUAL"},

            {"nome": "A**** G****", "quantidade": 300, "lista": "CDC", "tipo": "MANUAL"},
            {"nome": "M***** B*****", "quantidade": 300, "lista": "CDC", "tipo": "MANUAL"},
            {"nome": "M***** M****", "quantidade": 200, "lista": "CDC", "tipo": "MANUAL"},
            {"nome": "S***** M****", "quantidade": 300, "lista": "CDC", "tipo": "MANUAL"},
            {"nome": "E********** B******", "quantidade": 200, "lista": "CDC", "tipo": "MANUAL"},
            {"nome": "G****** O*******", "quantidade": 300, "lista": "CDC", "tipo": "MANUAL"},
            {"nome": "R***** M***", "quantidade": 300, "lista": "CDC", "tipo": "MANUAL"},

            {"nome": "B**** O******", "quantidade": 100, "lista": "CDC", "tipo": "MANUAL"},
            {"nome": "V***** A******", "quantidade": 300, "lista": "CDC", "tipo": "MANUAL"},
            {"nome": "L**** G****", "quantidade": 300, "lista": "CDC", "tipo": "MANUAL"},

            {"nome": "I****** K*******", "quantidade": 0, "lista": "CDC", "tipo": "MANUAL"},
            {"nome": "T****** R****", "quantidade": 300, "lista": "CDC", "tipo": "MANUAL"},
            {"nome": "V***** C****", "quantidade": 300, "lista": "CDC", "tipo": "MANUAL"},
            {"nome": "E**** V****", "quantidade": 0, "lista": "CDC", "tipo": "MANUAL"},
            {"nome": "C*** N******", "quantidade": 300, "lista": "CDC", "tipo": "MANUAL"},
            {"nome": "J***** S******", "quantidade": 300, "lista": "CDC", "tipo": "MANUAL"},
            {"nome": "T******* C****", "quantidade": 300, "lista": "CDC", "tipo": "MANUAL"},

            {"nome": "B**** S****", "quantidade": "0", "lista": "INSS", "tipo": "MANUAL"},
            {"nome": "I******* A*****", "quantidade": "0", "lista": "INSS", "tipo": "MANUAL"},
            {"nome": "J*** B******", "quantidade": "0", "lista": "INSS", "tipo": "MANUAL"},

            {"nome": "J*** P****", "quantidade": "0", "lista": "INSS", "tipo": "MANUAL"},
            {"nome": "B**** O******", "quantidade": "0", "lista": "INSS", "tipo": "MANUAL"},
            {"nome": "V***** A******", "quantidade": 0, "lista": "INSS", "tipo": "MANUAL"},
            {"nome": "L**** G****", "quantidade": 0, "lista": "INSS", "tipo": "MANUAL"},
            {"nome": "T***** S****", "quantidade": 0, "lista": "INSS", "tipo": "MANUAL"},

            {"nome": "A**** G****", "quantidade": "50", "lista": "INSS", "tipo": "MANUAL"},
            {"nome": "M***** B*****", "quantidade": "0", "lista": "INSS", "tipo": "MANUAL"},
            {"nome": "M***** M****", "quantidade": "50", "lista": "INSS", "tipo": "MANUAL"},
            {"nome": "S***** M****", "quantidade": "0", "lista": "INSS", "tipo": "MANUAL"},
            {"nome": "E********** B******", "quantidade": "50", "lista": "INSS", "tipo": "MANUAL"},
            {"nome": "G****** O*******", "quantidade": "0", "lista": "INSS", "tipo": "MANUAL"},
            {"nome": "R***** M***", "quantidade": "0", "lista": "INSS", "tipo": "MANUAL"},

            {"nome": "I****** ** C****", "quantidade": "50", "lista": "INSS", "tipo": "MANUAL"},
            {"nome": "Í**** R****", "quantidade": "0", "lista": "INSS", "tipo": "MANUAL"},
            {"nome": "S*** L*****", "quantidade": "0", "lista": "INSS", "tipo": "MANUAL"},
            {"nome": "H***** S******", "quantidade": "0", "lista": "INSS", "tipo": "MANUAL"},
            {"nome": "E****** R****", "quantidade": "50", "lista": "INSS", "tipo": "MANUAL"},
            {"nome": "R***** S****", "quantidade": "0", "lista": "INSS", "tipo": "MANUAL"},
            {"nome": "M***** L****", "quantidade": "0", "lista": "INSS", "tipo": "MANUAL"},

            {"nome": "I****** K*******", "quantidade": 0, "lista": "INSS", "tipo": "MANUAL"},
            {"nome": "T****** R****", "quantidade": 0, "lista": "INSS", "tipo": "MANUAL"},
            {"nome": "V***** C****", "quantidade": 0, "lista": "INSS", "tipo": "MANUAL"},
            {"nome": "E**** V****", "quantidade": 0, "lista": "INSS", "tipo": "MANUAL"},
            {"nome": "C*** N******", "quantidade": 0, "lista": "INSS", "tipo": "MANUAL"},
            {"nome": "J***** S******", "quantidade": 0, "lista": "INSS", "tipo": "MANUAL"},
            {"nome": "T******* C****", "quantidade": 0, "lista": "INSS", "tipo": "MANUAL"}
    ]

    
    total_cdc = 0
    total_inss = 0

    for atendente in informacoes_atendentes:
        if atendente['lista'] == 'CDC':
            if atendente['tipo'] == 'ASSERTIVA':
                total_cdc += int(atendente['quantidade'])
            elif atendente['tipo'] == 'MANUAL':
                total_cdc +=  int(atendente['quantidade'])
        elif atendente['lista'] == 'INSS' and atendente['tipo'] == 'ASSERTIVA':
            total_inss +=  int(atendente['quantidade'])
            
    # Contando os valores na coluna 'lista'
    contagem_lista = df_concatenado['lista'].value_counts()

    # Exibindo a contagem de cada valor
    print("Contagem de valores na coluna 'lista':")
    print(contagem_lista)
    print(f"Total alocado para CDC: {total_cdc}")
    print(f"Total alocado para INSS: {total_inss}")

    # Iterar sobre as informações dos atendentes
    for atendente_info in informacoes_atendentes:
        nome_atendente = atendente_info['nome']
        quantidade = atendente_info['quantidade']
        tipo_lista = atendente_info['lista']
        tipo_atendimento = atendente_info['tipo']

        # Filtrar o DataFrame por tipo de lista e atendente não atribuído
        filtro = (df_concatenado['lista'] == tipo_lista) & (df_concatenado['atendente'] == '')
        indices_disponiveis = df_concatenado[filtro].index

        # Verificar se a quantidade é maior que os índices disponíveis
        if quantidade and int(quantidade) > len(indices_disponiveis):
            print(f"Quantidade insuficiente para '{nome_atendente}' na lista '{tipo_lista}'.")
            continue

        # Selecionar os primeiros índices para o atendente respeitando a quantidade desejada
        indices_selecionados = indices_disponiveis[:int(quantidade)]

        # Atribuir o nome do atendente e tipo 'manual' nas linhas selecionadas
        df_concatenado.loc[indices_selecionados, 'atendente'] = nome_atendente
        df_concatenado.loc[indices_selecionados, 'tipo'] = tipo_atendimento

    # Exibir o DataFrame atualizado
    print("DataFrame com os atendentes e tipos atribuídos em ordem:")
    print(df_concatenado)

    # Mapear atendentes ao time correspondente
    mapeamento_atendente_time = {
        'A**** G****': 'N*******',
        'E********** B******': 'N*******',
        'H***** S******': 'N*******',
        'I****** ** C****': 'N*******',
        'R***** M***': 'N*******',
        'M**** V******': 'N*******',
        'D***** K****': 'N*******',
        'M***** B*****': 'N*******',
        'M***** M****': 'N*******',
        'G****** O*******': 'N*******',
        'P**** H********': 'N*******',
        'R***** M*******': 'N*******',
        'S***** M****': 'N*******',
        'S*** L*****': 'N*******',
        'E****** R****': 'N*******',
        
        'B**** S****': 'R******',
        'C*** N*******': 'R******',
        'D****** E*******': 'R******',
        'I******* A*****': 'R******',
        'Í**** R****': 'R******',
        'L*** M*****': 'R******',
        'M****** O*******': 'R******',
        'P**** A****': 'R******',
        'S*** C****': 'R******',
        'G****** R*****': 'R******',
        'J*** P****': 'R******',
        'J*** B******': 'R******',
        'M****** ** S****': 'R******',
        
        'B**** O******': 'A**',
        'D***** S****': 'A**',
        'J***** S******': 'A**',
        'M***** L****': 'A**',
        'R***** S****': 'A**',
        'R***** B********': 'A**',
        'R****** R********': 'A**',
        'T****** R****': 'A**',
        'T******* C****': 'A**',
        'T***** S********': 'A**',
        'A**** A*****': 'A**',
        'I****** K*******': 'A**',
        'G********* C****': 'A**',
        'M***** C*****': 'A**',
        'V***** C****': 'A**',
        'E**** V****': 'A**'
    }


    # Iterar sobre os atendentes e atribuir ao time correspondente
    for atendente_info in informacoes_atendentes:
        nome_atendente = atendente_info['nome']
        time_atendente = mapeamento_atendente_time.get(nome_atendente)

        # Atribuir o time ao atendente no DataFrame
        filtro_atendente = df_concatenado['atendente'] == nome_atendente
        df_concatenado.loc[filtro_atendente, 'time'] = time_atendente

    # Exibir o DataFrame atualizado
    print("DataFrame com os times atribuídos aos atendentes:")
    print(df_concatenado)
    
    df_concatenado.to_excel(f"lista_consulta{data}.xlsx", index=False)

    # Lista de atendentes únicos
    atendentes_unicos = df_concatenado['atendente'].unique()

    # Lista de tipos únicos
    tipos_unicos = df_concatenado['tipo'].unique()

    # Criar um dicionário para armazenar os DataFrames de cada combinação de atendente e tipo
    dfs_por_combinacao = {}

    # Iterar sobre cada combinação de atendente e tipo
    for atendente in atendentes_unicos:
        for tipo in tipos_unicos:
            # Filtrar o DataFrame para cada combinação de atendente e tipo
            filtro = (df_concatenado['atendente'] == atendente) & (df_concatenado['tipo'] == tipo)

            # Verificar se há dados correspondentes ao filtro
            if df_concatenado.loc[filtro].shape[0] > 0:
                if tipo == 'ASSERTIVA':
                    # Se o tipo for 'assertiva', filtrar apenas as colunas 'nome' e 'celular'
                    df_temp = df_concatenado.loc[filtro, ['nome', 'celular']]
                else:
                    # Caso contrário, manter todas as colunas
                    df_temp = df_concatenado[filtro].copy()  # Copiar para evitar a referência ao DataFrame original

                # Nome da chave para o dicionário
                chave = f"{atendente}_{tipo}"

                # Adicionar o DataFrame ao dicionário
                dfs_por_combinacao[chave] = df_temp

    # Exibir os DataFrames criados para cada combinação de atendente e tipo
    for chave, df in dfs_por_combinacao.items():
        print(f"DataFrame para {chave}:")
        print(df)

    # Exibir os DataFrames criados para cada combinação de atendente e tipo
    for chave, df in dfs_por_combinacao.items():
        print(f"DataFrame para {chave}:")
        print(df)


    global nomes_arquivos_salvos
    # Iterar sobre os DataFrames criados para cada combinação de atendente e tipo
    for chave, df in dfs_por_combinacao.items():
        # Nome do arquivo Excel baseado na chave (nome_atendente_tipo)
        nome_arquivo = f"{data}{chave}.xlsx"

        # Verificar se o tipo é 'ASSERTIVA'
        if 'ASSERTIVA' in chave:
            # Salvar o DataFrame em um arquivo Excel
            df.to_excel(nome_arquivo, index=False)
            nomes_arquivos_salvos.append(nome_arquivo)
            print(f"DataFrame para {chave} salvo em '{nome_arquivo}'")
            # Chamar a função carteira para manipular os dados
            

        else:
            
            # Obtém o índice da coluna 'nome'
            index_nome = df.columns.get_loc('nome')
        
            # Move a coluna 'lista' para antes da coluna 'nome'
            df.insert(index_nome, 'lista', df.pop('lista'))

            # Salva o DataFrame no arquivo Excel
            df.to_excel(nome_arquivo, index=False)
            nomes_arquivos_salvos.append(nome_arquivo)
            print(f"DataFrame para {chave} salvo em '{nome_arquivo}'")

    # Criar um arquivo txt com os nomes dos arquivos salvos
    with open('nomes_arquivos_salvos.txt', 'w') as file:
        file.write('\n'.join(nomes_arquivos_salvos))
    menu()


def carregar_arquivo_excel():
    # Inicializar o Tkinter
    root = tk.Tk()

    # Abrir a janela de seleção de arquivo
    nome_do_arquivo = filedialog.askopenfilename(title="Selecione o arquivo Excel", filetypes=[("Arquivos Excel", "*.xlsx")])

    # Verifica se um arquivo foi selecionado
    if nome_do_arquivo:
        # Carregar o arquivo Excel
        xl = pd.ExcelFile(nome_do_arquivo)
        print("Arquivo carregado com sucesso!")
        root.destroy()  # Fecha a janela do Tkinter
        return xl
    else:
        print("Nenhum arquivo selecionado.")
        root.destroy()  # Fecha a janela do Tkinter se nenhum arquivo for selecionado
        return None



def consulta():
    # Pergunta ao usuário o nome da planilha
    nome_planilha = input("Digite o nome da planilha: ")

    # Cria uma nova planilha com o nome fornecido
    new_sheet = bots[0].create(nome_planilha)
    print(f"Planilha '{nome_planilha}' criada com sucesso!")

    # Lista de e-mails dos supervisores
    emails_supervisores = [
    'r*******@gmail.com',
    'n*******@gmail.com',
    'a*********@gmail.com',
    'a***@gmail.com',
    ]


    # Combine todas as contas de e-mail em uma única lista
    todos_emails = emails_supervisores

    # Verificar e compartilhar a planilha com todos os e-mails em uma única chamada
    for email in todos_emails:
        try:
            existing_permissions = new_sheet.list_permissions()
            existing_emails = [perm.get('emailAddress') for perm in existing_permissions]

            if email not in existing_emails:
                new_sheet.share(email, perm_type='user', role='writer')
                print(f"Permissão concedida para {email}")
            else:
                print(f"{email} já tem permissão para acessar a planilha.")
        except Exception as e:
            print(f"Erro ao verificar/per conceder permissão para {email}: {e}")


    #carregar o arquivo em um DataFrame:
    data = input("digite a data da lista:")
    data_frame = pd.read_excel(f"lista_consulta{data}.xlsx")
    # Remover pontos decimais dos valores e converter para inteiros
    data_frame['celular'] = data_frame['celular'].astype(str).str.replace('.0', '')
    data_frame['tel1'] = data_frame['tel1'].astype(str).str.replace('.0', '')
    data_frame['tel2'] = data_frame['tel2'].astype(str).str.replace('.0', '')
    data_frame['tel3'] = data_frame['tel3'].astype(str).str.replace('.0', '')
    data_frame['tel4'] = data_frame['tel4'].astype(str).str.replace('.0', '')

    # Carregar o DataFrame na planilha
    planilha_atual = new_sheet.get_worksheet(0)  # Obtém a primeira aba da planilha

    # Limpando a planilha antes de inserir novos dados
    planilha_atual.clear()

    # Carregar o DataFrame na planilha
    data_frame_str = data_frame.astype(str)  # Convertendo todos os dados para strings
    data = [data_frame_str.columns.values.tolist()] + data_frame_str.values.tolist()

    # Atualizar os dados na planilha
    planilha_atual.update(data)
    print("DataFrame carregado na planilha com sucesso!")

    # Obtendo o link da planilha
    link_planilha = new_sheet.url
    print(f"Link da planilha: {link_planilha}")
    menu()


def individuais():
    # ID da planilha
    urls_planilhas = [
    'https://docs.google.com/spreadsheets/d/1xEz_znwOy-***********/edit#gid=1928279899',
    'https://docs.google.com/spreadsheets/d/1LGKZlpeWIf***********/edit#gid=1508820274',
    'https://docs.google.com/spreadsheets/d/1to95Vd-Zk***********/edit#gid=1834052228',
    'https://docs.google.com/spreadsheets/d/1VpEX0Eov2s***********/edit#gid=1225424645',
    'https://docs.google.com/spreadsheets/d/1sf4F59wvp1***********/edit#gid=1886942996',
    'https://docs.google.com/spreadsheets/d/1EXiCM3rXl***********/edit#gid=234136030',
    ]

    
    global data
    nome_do_arquivo = f"lista_consulta{data}.xlsx"
        # Loop para verificar permissões de edição para cada bot
    
    for url in urls_planilhas: 


        for bot in bots:
            spreadsheet_id = url.split('/')[-2]
            planilha = bot.open_by_key(spreadsheet_id)
            permissions = planilha.list_permissions()
            for permission in permissions:
                email = permission.get('emailAddress')
                role = permission.get('role')
                if email == bot.auth._service_account_email:
                    print(f"Permissão de {role} para editar a planilha.")
                    break
            else:
                print("Bot não tem permissão para editar a planilha.")
                
                
        
        # Substitua 'nome_do_arquivo.xlsx' pelo nome do arquivo Excel que você fez upload
        

        # Carregar o arquivo Excel para um DataFrame usando Pandas
        df = pd.read_excel(nome_do_arquivo)

        # Remover pontos decimais dos valores e converter para inteiros
        df['celular'] = df['celular'].astype(str).str.replace('.0', '')
        df['tel1'] = df['tel1'].astype(str).str.replace('.0', '')
        df['tel2'] = df['tel2'].astype(str).str.replace('.0', '')
        df['tel3'] = df['tel3'].astype(str).str.replace('.0', '')
        df['tel4'] = df['tel4'].astype(str).str.replace('.0', '')

        # Filtrar os clientes cujo tipo seja "MANUAL"
        clientes_manual = df#[df['tipo'] == 'MANUAL']
        # Agrupar os clientes pelo atendente
        grupos_atendentes = clientes_manual.groupby('atendente')

        # Criar um dicionário de DataFrames, onde cada chave é o nome do atendente e o valor é o DataFrame dos clientes desse atendente
        dicionario_df = {atendente: grupo for atendente, grupo in grupos_atendentes}

        # Exibir os nomes dos atendentes presentes no dicionário
        nomes_atendentes = list(dicionario_df.keys())
        print("Nomes dos Atendentes:", nomes_atendentes)

        escritas_realizadas = 0
        escritas_por_minuto = 0
        tempo_inicio = time.time()
        x = 0

        # Seu código para definição de variáveis e estruturas de dados

        # Defina um tamanho de lote para operações em lotes (batch)
        tamanho_lote = 8000  # Experimente diferentes tamanhos para encontrar o mais eficiente
    
        for atendente, dados_atendente in dicionario_df.items():
            try:
                proxima_linha = 2 
                proxima_coluna = 1
                batch_data = []
                planilha_individual = bots[x].open_by_key(spreadsheet_id)
                aba_atendente = planilha_individual.worksheet(atendente)
                # Encontrar a última linha ocupada na planilha
                last_row = len(aba_atendente.get_all_values())
                proxima_linha = last_row + 1  # Iniciar na linha após a última ocupada
                for row_idx, row in enumerate(dados_atendente[['data','nome', 'cpf', 'agencia', 'conta','tel1','tel2','tel3','tel4', 'celular','tipo']].astype(str).values, start=0):
                    batch_values = []
                    for col_idx, value in enumerate(row, start=0):
                        
                        batch_values.append({"range": f"{gspread.utils.rowcol_to_a1(proxima_linha + row_idx, proxima_coluna + col_idx)}", "values": [[value]]})



                    
                    batch_data.extend(batch_values)

                    if len(batch_data) >= tamanho_lote:
                        try:
                            planilha_individual = bots[x].open_by_key(spreadsheet_id)
                            aba_atendente = planilha_individual.worksheet(atendente)
                            
                            aba_atendente.batch_update(batch_data)
                            batch_data = []  # Limpa os dados do lote depois de enviá-los em lote

                            # Atualização do índice do bot para alternar entre os 5 bots
                            x = (x + 1) % 5  
                            
                            # Medindo a quantidade a cada escrita (opcional)
                            escritas_realizadas += len(batch_values)
                            print(f"Escritas realizadas até o momento: {escritas_realizadas}")

                            # Medição de escritas por minuto (opcional)
                            tempo_decorrido = time.time() - tempo_inicio
                            if tempo_decorrido > 0:
                                escritas_por_minuto = round(escritas_realizadas / (tempo_decorrido / 60), 0)
                                print(f"Escritas por minuto: {escritas_por_minuto}")

                        except gspread.exceptions.APIError as api_error:
                            print(f"Erro ao processar o atendente {atendente}: {str(api_error)}")
                            continue

                # Verifica se ainda há dados no lote para enviar
                if batch_data:
                    try:
                        planilha_individual = bots[x].open_by_key(spreadsheet_id)
                        aba_atendente = planilha_individual.worksheet(atendente)
                        aba_atendente.batch_update(batch_data)
                        
                        # Atualização do índice do bot para alternar entre os 5 bots
                        x = (x + 1) % 5  
                        
                        # Medindo a quantidade a cada escrita (opcional)
                        escritas_realizadas += len(batch_data)
                        print(f"Escritas realizadas até o momento: {escritas_realizadas}")

                        # Medição de escritas por minuto (opcional)
                        tempo_decorrido = time.time() - tempo_inicio
                        if tempo_decorrido > 0:
                            escritas_por_minuto = round(escritas_realizadas / (tempo_decorrido / 60), 0)
                            print(f"Escritas por minuto: {escritas_por_minuto}")

                    except gspread.exceptions.APIError as api_error:
                        print(f"Erro ao processar o atendente {atendente}: {str(api_error)}")
                        continue

                print(f"Escritas para o atendente {atendente} concluídas.")

            except Exception as e:
                print(f"Erro ao processar o atendente {atendente}: {str(e)}")
                continue
        

        #carregar o arquivo em um DataFrame:
        
        data_frame = pd.read_excel(f"lista_consulta{data}.xlsx")
        
        data_frame['celular'] = data_frame['celular'].astype(str).str.replace('.0', '')
        data_frame['tel1'] = data_frame['tel1'].astype(str).str.replace('.0', '')
        data_frame['tel2'] = data_frame['tel2'].astype(str).str.replace('.0', '')
        data_frame['tel3'] = data_frame['tel3'].astype(str).str.replace('.0', '')
        data_frame['tel4'] = data_frame['tel4'].astype(str).str.replace('.0', '')

        # Carregar o DataFrame na planilha
        planilha_atual = planilha_individual.worksheet('LISTA')  # Obtém a primeira aba da planilha

        # Limpando a planilha antes de inserir novos dados
        planilha_atual.clear()
        
        # Carregar o DataFrame na planilha
        data_frame_str = data_frame.astype(str)  # Convertendo todos os dados para strings
        data1 = [data_frame_str.columns.values.tolist()] + data_frame_str.values.tolist()

        # Atualizar os dados na planilha
        planilha_atual.update(data1)
        print("LISTA DO DIA carregado na planilha com sucesso!")
    menu()

def dados():
    print("Por favor, escolha o arquivo da lista.")
    xl = carregar_arquivo_excel()

    # Obter a lista de abas (ou planilhas)
    abas = xl.sheet_names

    # Mostrar o número de abas
    print(f'O arquivo possui {len(abas)} aba(s) ou planilha(s).')
    print(f'Nomes das abas: {abas}')

    # Verificar novamente e carregar abas em DataFrames separados
    if 'Consignados' in xl.sheet_names:
        aba_inss = xl.parse('Consignados')
        aba_inss['lista'] = 'INSS'
    else:
        aba_inss = None  # Ou None, dependendo do que você deseja fazer

    if 'Cdc' in xl.sheet_names:
        aba_cdc = xl.parse('Cdc')
        aba_cdc['lista'] = 'CDC'
    else:
        aba_cdc = None
        
    # Concatenar os DataFrames
    df_concatenado = pd.concat([aba_inss, aba_cdc], ignore_index=True)
    print(df_concatenado)

    # Renomeia as colunas em minúsculas
    df_concatenado.columns = df_concatenado.columns.str.lower()

    # Convertendo todas as colunas para strings
    df_concatenado = df_concatenado.astype(str)

    # Adicionar novas colunas vazias
    df_concatenado['atendente'] = ''
    df_concatenado['tipo'] = ''
    df_concatenado['time'] = ''
    df_concatenado.insert(0, 'data', data)

    print("Colunas do DataFrame:")
    print(df_concatenado.columns)

    # Excluir linhas com células vazias na coluna 'celular'
    df_concatenado = df_concatenado.dropna(subset=['celular'])

    # Remover pontos decimais dos valores e converter para inteiros
    df_concatenado['celular'] = df_concatenado['celular'].astype(str).str.replace('.0', '')

    # Verifique se a coluna vazia existe
    if '(nenhum nome de coluna)' in df_concatenado.columns:
        # Deleta a coluna vazia
        df_concatenado.drop('(nenhum nome de coluna)', axis=1, inplace=True)
        print("Coluna vazia removida com sucesso!")
    else:
        print("A coluna vazia não existe no DataFrame.")

    # Exibindo o DataFrame após a exclusão das linhas vazias na coluna 'celular'
    print("DataFrame com os valores e colunas ajustados:")
    print(df_concatenado)

    print("Colunas do DataFrame:")
    print(df_concatenado.columns)

    # Contando os valores na coluna 'lista'
    contagem_lista = df_concatenado['lista'].value_counts()

    # Exibindo a contagem de cada valor
    print("Contagem de Clientes validos:")
    print(contagem_lista)

    # Definindo as equipes
    equipes = ['Nicollas', 'Bruna', 'Ana','Ivanete','Breno']

    # Inicializar uma lista para armazenar o número de atendentes por equipe
    atendentes_por_equipe = [7,5,9,6,5]

    # Verificação para INSS
    try:
        total_clientes_INSS = contagem_lista['INSS']
    except KeyError:
        total_clientes_INSS = 0

    # Verificação para CDC
    try:
        total_clientes_CDC = contagem_lista['CDC']
    except KeyError:
        total_clientes_CDC = 0

    # Calcular a divisão ponderada com base na quantidade de atendentes por equipe
    clientes_por_atendente_INSS = total_clientes_INSS / sum(atendentes_por_equipe)
    clientes_por_atendente_CDC = total_clientes_CDC / sum(atendentes_por_equipe)

    # Inicializar uma lista para armazenar a distribuição de clientes corrigida
    clientes_equipe = []

    # Calcular a distribuição de clientes para cada equipe
    for atendentes in atendentes_por_equipe:
        clientes_equipe.append({
            'INSS': min(round(clientes_por_atendente_INSS * atendentes), total_clientes_INSS),
            'CDC': min(round(clientes_por_atendente_CDC * atendentes), total_clientes_CDC)
        })

        # Reduzir a contagem total disponível para evitar ultrapassar o total
        total_clientes_INSS -= clientes_equipe[-1]['INSS']
        total_clientes_CDC -= clientes_equipe[-1]['CDC']

    # Exibindo a contagem de cada valor
    print("Contagem de valores na coluna 'lista':")
    print(contagem_lista)

    # Imprimir a distribuição para cada equipe
    for i, equipe in enumerate(clientes_equipe):
        print(f"Equipe {equipes[i]}:")
        print(f"INSS: {equipe['INSS']} clientes")
        print(f"CDC: {equipe['CDC']} clientes")



    menu()


    
''' ===================================================================================='''
''' ===================================================================================='''
''' ===================================================================================='''
''' ===================================================================================='''

# Mensagem para o usuário escolher o arquivo
data = input("digite a data da lista:")
print("Por favor, escolha o arquivo da lista.")
xl = carregar_arquivo_excel()


# Obter a lista de abas (ou planilhas)
abas = xl.sheet_names
# Mostrar o número de abas
print(f'O arquivo possui {len(abas)} aba(s) ou planilha(s).')
print(f'Nomes das abas: {abas}')
# Verificar novamente e carregar abas em DataFrames separados
if any(sheet_name.lower() in ['inss', 'consignados'] for sheet_name in xl.sheet_names):
    for sheet_name in xl.sheet_names:
        if sheet_name.lower() in ['inss', 'consignados']:
            aba_inss = xl.parse(sheet_name)
            aba_inss['lista'] = 'INSS'
            break
else:
    aba_inss = None

if any(sheet_name.lower() == 'cdc' for sheet_name in xl.sheet_names):
    for sheet_name in xl.sheet_names:
        if sheet_name.lower() == 'cdc':
            aba_cdc = xl.parse(sheet_name)
            aba_cdc['lista'] = 'CDC'
            break
else:
    aba_cdc = None
        
# Concatenar os DataFrames
df_concatenado = pd.concat([aba_inss, aba_cdc], ignore_index=True)
print(df_concatenado)

# Renomeia as colunas em minúsculas
df_concatenado.columns = df_concatenado.columns.str.lower()

# Convertendo todas as colunas para strings
df_concatenado = df_concatenado.astype(str)

# Adicionar novas colunas vazias
df_concatenado['atendente'] = ''
df_concatenado['tipo'] = ''
df_concatenado['time'] = ''
df_concatenado.insert(0, 'data', data)

print("Colunas do DataFrame:")
print(df_concatenado.columns)

# Substituir strings vazias por NaN
df_concatenado['celular'].replace('', np.nan, inplace=True)


# Excluir linhas com células vazias na coluna 'celular'
df_concatenado = df_concatenado.dropna(subset=['celular'])

# Remover pontos decimais dos valores e converter para inteiros
df_concatenado['celular'] = df_concatenado['celular'].astype(str).str.replace('.0', '')
# Filtrar linhas onde o terceiro caractere da coluna 'celular' é "2", "3", "4", ou "5"
df_concatenado = df_concatenado[~df_concatenado['celular'].str[2].isin(['2', '3', '4', '5'])]


# Verifique se a coluna vazia existe
if '(nenhum nome de coluna)' in df_concatenado.columns:
    # Deleta a coluna vazia
    df_concatenado.drop('(nenhum nome de coluna)', axis=1, inplace=True)
    print("Coluna vazia removida com sucesso!")
else:
    print("A coluna vazia não existe no DataFrame.")

# Exibindo o DataFrame após a exclusão das linhas vazias na coluna 'celular'
print("DataFrame com os valores e colunas ajustados:")
print(df_concatenado)

print("Colunas do DataFrame:")
print(df_concatenado.columns)

# Contando os valores na coluna 'lista'
contagem_lista = df_concatenado['lista'].value_counts()

# Exibindo a contagem de cada valor
print("Contagem de Clientes validos:")
print(contagem_lista)

# Definindo as equipes
equipes = ['N*******', 'B****', 'A**', 'I******', 'B****']

# Inicializar uma lista para armazenar o número de atendentes por equipe
atendentes_por_equipe = [7,5,9,6,5]

# Verificação para INSS
try:
    total_clientes_INSS = contagem_lista['INSS']
except KeyError:
    total_clientes_INSS = 0

# Verificação para CDC
try:
    total_clientes_CDC = contagem_lista['CDC']
except KeyError:
    total_clientes_CDC = 0

# Calcular a divisão ponderada com base na quantidade de atendentes por equipe
clientes_por_atendente_INSS = total_clientes_INSS / sum(atendentes_por_equipe)
clientes_por_atendente_CDC = total_clientes_CDC / sum(atendentes_por_equipe)

# Inicializar uma lista para armazenar a distribuição de clientes corrigida
clientes_equipe = []

# Calcular a distribuição de clientes para cada equipe
for atendentes in atendentes_por_equipe:
    clientes_equipe.append({
        'INSS': min(round(clientes_por_atendente_INSS * atendentes), total_clientes_INSS),
        'CDC': min(round(clientes_por_atendente_CDC * atendentes), total_clientes_CDC)
    })

    # Reduzir a contagem total disponível para evitar ultrapassar o total
    total_clientes_INSS -= clientes_equipe[-1]['INSS']
    total_clientes_CDC -= clientes_equipe[-1]['CDC']

# Exibindo a contagem de cada valor
print("Contagem de valores na coluna 'lista':")
print(contagem_lista)

# Imprimir a distribuição para cada equipe
for i, equipe in enumerate(clientes_equipe):
    print(f"Equipe {equipes[i]}:")
    print(f"INSS: {equipe['INSS']} clientes")
    print(f"CDC: {equipe['CDC']} clientes")

    # Calcular e imprimir a quantidade de clientes por atendente (arredondado para baixo)
    clientes_por_atendente_inss = equipe['INSS'] / atendentes_por_equipe[i]
    clientes_por_atendente_cdc = equipe['CDC'] / atendentes_por_equipe[i]

    clientes_por_atendente_inss_arredondado = math.floor(clientes_por_atendente_inss)
    clientes_por_atendente_cdc_arredondado = math.floor(clientes_por_atendente_cdc)
    print(f"Clientes por atendente (INSS): {clientes_por_atendente_inss_arredondado} clientes")
    print(f"Clientes por atendente (CDC): {clientes_por_atendente_cdc_arredondado} clientes")    
menu()



