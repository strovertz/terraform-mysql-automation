import csv
import mysql.connector

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'agencia_turismo'
}

def create_database():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute("CREATE DATABASE agencia_turismo")
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
        create_table(nome_tabela, cabecalho)

        for linha in leitor_csv:
            valores = ', '.join(['%s' for _ in linha])
            query = f"INSERT INTO {nome_tabela} VALUES ({valores})"
            cursor.execute(query, linha)

    conn.commit()
    conn.close()

def main():
    create_database()
    insert_data('clientes', '/tmp/clientes.csv')
    insert_data('fornecedores', '/tmp/fornecedores.csv')
    insert_data('servicos', '/tmp/servicos.csv')
    insert_data('pedidos', '/tmp/pedidos.csv')
    insert_data('itens_pedido', '/tmp/itens_pedido.csv')
    print('Dados importados com sucesso!')

main()
