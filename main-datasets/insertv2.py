import csv
import mysql.connector
from datetime import datetime

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'agencia_turismo'
}

def create_database():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS agencia_turismo")
    conn.commit()
    conn.close()

def create_table_clientes():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id AUTOINCREMENT PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            email VARCHAR(255),
            telefone VARCHAR(20),
            genero VARCHAR(10) NOT NULL,
            cpf VARCHAR(14) NOT NULL,
            endereco VARCHAR(255) NOT NULL,
            data_nasc DATE NOT NULL,
            senha VARCHAR(255) NOT NULL,
            updated_at TIMESTAMP,
            deleted_at TIMESTAMP,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def create_table_servicos():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS servicos (
            id AUTOINCREMENT PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            tipo_servico VARCHAR(255) NOT NULL,
            valor DECIMAL(10, 2) NOT NULL,
            endereco VARCHAR(255),
            data DATE,
            descricao TEXT,
            tipo_pagamento VARCHAR(255),
            updated_at TIMESTAMP,
            deleted_at TIMESTAMP,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def create_table_itens():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS itens (
            id AUTOINCREMENT PRIMARY KEY,
            id_servico INT,
            id_cliente INT,
            FOREIGN KEY (id_servico) REFERENCES servicos(id),
            FOREIGN KEY (id_cliente) REFERENCES clientes(id),
            valor_produto FLOAT NOT NULL,
            updated_at TIMESTAMP,
            deleted_at TIMESTAMP,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def create_table(nome_tabela, cabecalho):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    colunas = ', '.join([f'{nome_coluna} VARCHAR(255)' for nome_coluna in cabecalho])
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {nome_tabela} ({colunas})")
    conn.commit()

    conn.close()

def insert_data(nome_tabela, caminho_csv):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    with open(caminho_csv, 'r') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        cabecalho = next(leitor_csv)

        # Adiciona 'created_act' ao cabeçalho
        cabecalho.append('created_act')

        create_table(nome_tabela, cabecalho)

        for linha in leitor_csv:
            if len(linha) < len(cabecalho):
                linha.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

            linha = linha[:len(cabecalho)]

            try:
                valores = ', '.join(['%s' for _ in linha])
                query = f"INSERT INTO {nome_tabela} VALUES ({valores})"
                cursor.execute(query, linha)
            except Exception as e:
                print(f"Erro ao inserir linha {linha} na tabela {nome_tabela}: {e}")

    conn.commit()
    conn.close()

def main():
    create_database()
    create_table_clientes()
    create_table_servicos()
    create_table_itens()
    
    #insert_data('clientes', './clientes.csv')
    #insert_data('fornecedores', './fornecedores.csv')
    #insert_data('servicos', './servicos.csv')

    print('Tabelas e dados importados com sucesso!')

main()
