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

    # Trigger para Atualizar Total do Pedido
    cursor.execute('''
    CREATE TRIGGER atualizar_total_pedido AFTER INSERT ON itens_pedido
    FOR EACH ROW
    BEGIN
        UPDATE pedidos
        SET total = (SELECT SUM(servicos.valor * itens_pedido.quantidade)
                     FROM itens_pedido
                     JOIN servicos ON itens_pedido.servico_id = servicos.id
                     WHERE itens_pedido.pedido_id = NEW.pedido_id)
        WHERE pedidos.id = NEW.pedido_id;
    END;
    ''')

    # Trigger para Impedir Exclusão de Clientes com Pedidos
    cursor.execute('''
    CREATE TRIGGER impedir_excluir_cliente BEFORE DELETE ON clientes
    FOR EACH ROW
    BEGIN
        DECLARE pedidos_associados INT;
        SELECT COUNT(*) INTO pedidos_associados FROM pedidos WHERE pedidos.cliente_id = OLD.id;
        IF pedidos_associados > 0 THEN
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Não é possível excluir um cliente com pedidos associados';
        END IF;
    END;
    ''')

    conn.commit()
    conn.close()

def main():
    create_triggers()
    print('Triggers criados com sucesso!')

main()
