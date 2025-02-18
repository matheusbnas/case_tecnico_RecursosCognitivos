import mysql.connector
from mysql.connector import Error


def test_mysql_connection():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",      # Usando IP em vez de hostname
            user="root",
            password="X@drez2214",
            database="escola_manager",
            port=3306
        )

        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"Conectado ao servidor MySQL versão {db_info}")

            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print(f"Conectado ao banco de dados: {record[0]}")

            return True

    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return False

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão MySQL fechada")


if __name__ == "__main__":
    test_mysql_connection()
