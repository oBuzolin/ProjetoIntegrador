import mysql.connector
from mysql.connector import Error

def create_table():
    connection = None  # Inicializa a variável connection
    try:
        # Conectando ao banco de dados MySQL
        connection = mysql.connector.connect(
            host='143.106.241.3',
            database='cl201107',
            user='cl201107',
            password='cl*02032005'
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # SQL para criar a tabela
            create_table_query = '''
            CREATE TABLE IF NOT EXISTS Minerva_Aluno (
                RA INT PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                usuario VARCHAR(255) NOT NULL,
                senha VARCHAR(255) NOT NULL,
                curso VARCHAR(100) NOT NULL,
                UNIQUE (usuario)
                
            );
            '''
            cursor.execute(create_table_query)
            connection.commit()
            print("Tabela 'Minerva_Aluno' criada com sucesso!")

    except Error as e:
        print(f"Erro ao conectar ou criar a tabela no MySQL: {e}")
    
    finally:
        # Verifica se a conexão foi estabelecida antes de tentar fechá-la
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL encerrada.")

if __name__ == "__main__":
    create_table()
