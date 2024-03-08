import sqlite3
from tkinter import messagebox

class SistemaDeRegistro:
    def __init__(self):
        self.conn = sqlite3.connect('estudante.db')
        self.c = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.c.execute(''' CREATE TABLE IF NOT EXISTS estudantes (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            email TEXT NOT NULL,
                            tel TEXT NOT NULL,
                             sexo TEXT NOT NULL,
                             data_nascimento TEXT NOT NULL,
                             endereco TEXT NOT NULL,
                             curso TEXT NOT NULL,
                             picture TEXT NOT NULL)''')

    def register_student(self, estudante):
        self.c.execute("INSERT INTO estudantes(nome, email, tel, sexo, data_nascimento, endereco, curso, picture) VALUES (?,?,?,?,?,?,?,?)", (estudante))
        self.conn.commit()

        # mostrando mensagem de sucesso
        messagebox.showinfo("Sucesso","Registro com sucesso!")
        print("Registro com sucesso!")

    def view_all_students(self):
        self.c.execute("SELECT * FROM estudantes")
        dados =self.c.fetchall()

        for i in dados:
            print(f'ID: {i[0]} | Nome:{i[1]} | email: {i[2]} | Tel: {i[3]} | Sexo: {i[4]} | Data de Nascimento: {i[5]} | Endereco: {i[6]} | Curso: {i[7]} | Imagem: {i[8]}')

    def search_student(self, id):
        self.c.execute("SELECT * FROM estudantes WHERE id=?", (id,))
        dados = self.c.fetchone()

        print(f'ID: {dados[0]} | Nome:{dados[1]} | email: {dados[2]} | Tel: {dados[3]} | Sexo: {dados[4]} | Data de Nascimento: {dados[5]} | Endereco: {dados[6]} | Curso: {dados[7]} | Imagem: {dados[8]}')

    def update_student(self, novo_valores):
        query = "UPDATE estudantes SET nome=?, email=?, tel=?, sexo=?, data_nascimento=?, endereco=?, curso=?, picture=? WHERE id=?"
        self.c.execute(query, novo_valores)
        self.conn.commit()

        # mostrando mensagem de sucesso
        messagebox.showinfo("Sucesso", f"Estudante com ID:{novo_valores[8]} foi atualizado!")

    def delete_student(self, id):
        self.c.execute("DELETE FROM estudantes WHERE id=?", (id,))
        self.conn.commit()

        # mostrando mensagem de sucesso
        messagebox.showinfo("Sucesso", f" Estudante com ID:{id} foi Deletado!")


# Criando uma instancia do sistema de registro
sistema_de_registro = SistemaDeRegistro()

# informações
#estudante = ('Elena', 'elena@gmail.com', '555', 'f', '02/03/1999', 'Recife,PE', 'Matemática', 'imagem2.png')
#sistema_de_registro.register_student(estudante)

# ver estudantes
todos_alunos = sistema_de_registro.view_all_students()

# procurar aluno
#aluno = sistema_de_registro.search_student(2)

#atualizar aluno
#estudante = ('Elena', 'elena@gmail.com', '3662-3125', 'f', '02/03/1999', 'Recife,PE', 'Matemática', 'imagem2.png', 2)
#aluno = sistema_de_registro.update_student(estudante)

#sistema_de_registro.delete_student(1)
