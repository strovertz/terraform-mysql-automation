import mysql.connector

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'agencia_turismo'
}
def create_triggers():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Trigger para a tabela clientes
    cursor.execute("""
        DELIMITER //
        CREATE TRIGGER clientes_before_update
        BEFORE UPDATE ON clientes
        FOR EACH ROW
        BEGIN
            -- da block naa atualização se o email for alterado
            IF NEW.email <> OLD.email THEN
                SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = 'Não é permitido alterar o email do cliente.';
            END IF;
        END;
        //
        DELIMITER ;
    """)

    # Trigger para a tabela servicos
    cursor.execute("""
        DELIMITER //
        CREATE TRIGGER servicos_before_insert
        BEFORE INSERT ON servicos
        FOR EACH ROW
        BEGIN
            -- n deixa que ocorra a inserção de serviços com valor igual a zero
            IF NEW.valor = 0 THEN
                SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = 'Não é permitido inserir serviços com valor igual a zero.';
            END IF;
        END;
        //
        DELIMITER ;
    """)

    # Trigger para a tabela itens
    cursor.execute("""
        DELIMITER //
        CREATE TRIGGER itens_before_delete
        BEFORE DELETE ON itens
        FOR EACH ROW
        BEGIN
            -- nao deixa acontecer a exclusão se o valor do produto for maior que 100
            IF OLD.valor_produto > 100 THEN
                SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = 'Não é permitido excluir itens com valor maior que 100.';
            END IF;
        END;
        //
        DELIMITER ;
    """)

    conn.commit()
    conn.close()

def main():
    create_triggers()
    
    print('triggers criados com sucesso!')

main()
