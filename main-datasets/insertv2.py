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
            id INT NOT NULL PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            email VARCHAR(255),
            telefone VARCHAR(20),
            genero VARCHAR(10) NOT NULL,
            cpf VARCHAR(14) NOT NULL,
            endereco VARCHAR(255) NOT NULL,
            data_nasc DATE NOT NULL,
            created_act TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_act TIMESTAMP,
            deleted_act TIMESTAMP
        )
    """)
    conn.commit()

    conn.close()

def create_table_servicos():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS servicos (
            id INT NOT NULL PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            tipo_servico VARCHAR(255) NOT NULL,
            valor DECIMAL(10, 2) NOT NULL,
            endereco VARCHAR(255),
            data DATE,
            descricao TEXT,
            created_act TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_act TIMESTAMP,
            deleted_act TIMESTAMP
        )
    """)
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
            # Adiciona o timestamp atual para 'created_act'
            linha.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

            valores = ', '.join(['%s' for _ in linha])
            query = f"INSERT INTO {nome_tabela} VALUES ({valores})"
            cursor.execute(query, linha)

    conn.commit()
    conn.close()

def main():
    create_database()
    create_table_clientes()
    create_table_servicos()

    insert_data('clientes', './clientes.csv')
    insert_data('servicos', './servicos.csv')

    print('Tabelas e dados importados com sucesso!')

main()
