import sqlite3  # Importa o módulo SQLite para manipulação de banco de dados local
import os       # Importa o módulo OS para verificar existência de arquivos e caminhos

DBFILENAME = "comidasdb.sqlite"  # Nome do arquivo do banco de dados

def getconnection():
    """Abre uma conexão com o banco de dados SQLite."""

    # Estabelece comunicação com o arquivo do banco de dados
    conn = sqlite3.connect(DBFILENAME)

    # Define que o resultado de SELECT será retornado como dicionário (nome da coluna)
    conn.row_factory = sqlite3.Row

    # Garante que restrições de chave estrangeira estejam ativas
    conn.execute("PRAGMA foreign_keys = ON")

    # Retorna o objeto de conexão para uso nas funções do sistema
    return conn

def ensuredb():
    """
    Garante que o banco exista.
    Se não existir, cria usando o arquivo db_init.sql.
    """

    # Verifica se o arquivo do banco de dados já existe
    if not os.path.exists(DBFILENAME):
        # Caminho completo para o arquivo db_init.sql, mesmo diretório do script
        scriptpath = os.path.join(os.path.dirname(__file__), "db_init.sql")
        if os.path.exists(scriptpath):
            # Cria o banco com base no script SQL de inicialização
            with getconnection() as conn:
                with open(scriptpath, "r", encoding="utf-8") as f:
                    conn.executescript(f.read())
        else:
            # Gera erro explicativo caso o arquivo db_init.sql não esteja disponível
            raise FileNotFoundError("db_init.sql não encontrado. Coloque db_init.sql na mesma pasta.")
