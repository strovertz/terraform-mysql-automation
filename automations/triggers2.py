import mysql.connector

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'agencia_turismo'
}

def create_additional_triggers():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # clientesz- Auditoria
    cursor.execute("""
        CREATE TRIGGER clientes_before_insert_audit
        BEFORE INSERT ON clientes
        FOR EACH ROW
        BEGIN
            SET NEW.created_at = NOW();
            SET NEW.updated_at = NOW();
        END;
    """)

    # aalidar dados
    cursor.execute("""
        CREATE TRIGGER servicos_before_update_validate
        BEFORE UPDATE ON servicos
        FOR EACH ROW
        BEGIN
            -- Impede a atualização se o tipo de serviço for vazio
            IF NEW.tipo_servico IS NULL OR NEW.tipo_servico = '' THEN
                SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = 'Tipo de serviço não pode ser vazio.';
            END IF;
        END;
    """)

    # Trigger para a tabela itens - Atualizaç automática de valores
    cursor.execute("""
        CREATE TRIGGER itens_before_insert_auto_update
        BEFORE INSERT ON itens
        FOR EACH ROW
        BEGIN
            -- Atualiza automaticamente o valor do produto para o do serviço associado
            SELECT valor INTO NEW.valor_produto FROM servicos WHERE id = NEW.id_servico;
        END;
    """)

    # tabela itens - Atualização automatica dps da atualização do serviço associado
    cursor.execute("""
        CREATE TRIGGER servicos_after_update_auto_update_items
        AFTER UPDATE ON servicos
        FOR EACH ROW
        BEGIN
            -- Atualiza automaticamente o valor do produto nos itens associados
            UPDATE itens SET valor_produto = NEW.valor WHERE id_servico = NEW.id;
        END;
    """)

    # Tatualiza um campo com base em outra tabela
    cursor.execute("""
        CREATE TRIGGER clientes_after_insert_update_servicos
        AFTER INSERT ON clientes
        FOR EACH ROW
        BEGIN
            UPDATE servicos SET tipo_servico = 'Serviço Padrão' WHERE id = NEW.id;
        END;
    """)

    # garante que o valor do serviço não seja negativo
    cursor.execute("""
        CREATE TRIGGER servicos_before_insert_check_valor
        BEFORE INSERT ON servicos
        FOR EACH ROW
        BEGIN
            IF NEW.valor < 0 THEN
                SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = 'Não é permitido inserir serviços com valor negativo.';
            END IF;
        END;
    """)

    # registra a exclusão de itens em um log
    cursor.execute("""
        CREATE TRIGGER itens_after_delete_log
        AFTER DELETE ON itens
        FOR EACH ROW
        BEGIN
            INSERT INTO itens_deleted_log (id, valor_produto, deleted_at)
            VALUES (OLD.id, OLD.valor_produto, NOW());
        END;
    """)

    #impedir a atualização do CPF na tabela clientes
    cursor.execute("""
        CREATE TRIGGER clientes_before_update_cpf
        BEFORE UPDATE ON clientes
        FOR EACH ROW
        BEGIN
            IF NEW.cpf <> OLD.cpf THEN
                SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = 'Não é permitido alterar o CPF do cliente.';
            END IF;
        END;
    """)

    conn.commit()
    conn.close()

def main():
    create_additional_triggers()

    print('Triggers adicionais criados com sucesso!')

main()
