import sqlite3

#criando tabela
#cursor.execute(''' CREATE TABLE usuario (
#                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#                    nome TEXT NOT NULL,
#                    idade INT NOT NULL);''')

#cursor.execute(''' INSERT INTO usuario (nome, idade) VALUES('Jorge', 55) ''')


with sqlite3.connect('usuario.db') as conexao:
    conexao.execute('BEGIN')
    cursor = conexao.cursor()
    cursor.execute(''' INSERT INTO usuario (nome, idade) VALUES('Joaquim', 25) ''')
    cursor.execute(''' INSERT INTO usuario (nome, idade) VALUES('Ana', 29) ''')
    cursor.execute(''' UPDATE usuario SET idade=15 WHERE id=3 ''')

    conexao.commit()

    conexao.rollback()


# Imprimindo os dados
with sqlite3.connect('usuario.db') as conexao:
    cursor = conexao.cursor()
    cursor.execute(''' SELECT * FROM usuario''')
    resultado = cursor.fetchall()

for linha in resultado:
    print(linha)


