from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

#importando pillow
from PIL import ImageTk, Image

#tk calendar
from tkcalendar import Calendar, DateEntry
from datetime import date

# importando Registro de aluno
from Registro import *

#cores
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca
co2 = "#e5e5e5"  # grey
co3 = "#00a095"  # Verde
co4 = "#403d3d"   # letra
co6 = "#003452"   # azul
co7 = "#ef5350"   # vermelha

co6 = "#146C94"   # azul
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde


# criando janela
janela = Tk()
janela.title("")
janela.geometry("810x535")
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")

# Criando Frames
frame_logo = Frame(janela, width=850, height=52, bg=co6)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW, columnspan=5)

frame_botoes = Frame(janela, width=100, height=200, bg=co1, relief=RAISED)
frame_botoes.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_details = Frame(janela, width=800, height=100, bg=co1, relief=SOLID)
frame_details.grid(row=1, column=1, pady=1, padx=10, sticky=NSEW)

frame_tabela = Frame(janela, width=800, height=100, bg=co1, relief=SOLID)
frame_tabela.grid(row=3, column=0, pady=0, padx=10, sticky=NSEW, columnspan=5)

# Trabalhando no frame logo
global imagem, imagem_string, l_imagem

app_lg = Image.open("logo.png")
app_lg = app_lg.resize((50,50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text="  Sistema de Registro de Alunos", width=850, compound=LEFT, anchor=NW, font=("Verdana 15"), bg=co6, fg=co1)
app_logo.place(x=5, y=0)

#abrindo a imagem

imagem = Image.open('logo.png')
imagem = imagem.resize((130, 130))
imagem = ImageTk.PhotoImage(imagem)
l_imagem = Label(frame_details, image=imagem, bg=co1, fg=co4)
l_imagem.place(x=390, y=10)

# --------------------criando funcoes para CRUD ---------------------
# função adicionar
def adicionar():
    global imagem, imagem_string, l_imagem

    # obtendo os valores
    nome = e_nome.get()
    email = e_email.get()
    tel = e_fone.get()
    sexo = c_sexo.get()
    data = data_nascimento.get()
    endereco = e_end.get()
    curso = c_curso.get()
    img = imagem_string

    lista = [nome, email, tel, sexo, data, endereco, curso, img]

    # varificado se a lista contem valor vazio
    for i in lista:
        if i == '':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return

    # registrando os valores
    sistema_de_registro.register_student(lista)

    # limpando os campos de entrada
    e_nome.delete(0,END)
    e_email.delete(0,END)
    e_fone.delete(0,END)
    c_sexo.delete(0,END)
    data_nascimento.delete(0,END)
    e_end.delete(0,END)
    c_curso.delete(0,END)

    # mostrando os valores da tabela
    mostrar_alunos()

# função procurar aluno
def procurar():
    global imagem, imagem_string, l_imagem

    # obtendo o id
    id_aluno = int(e_procurar.get())

    # procurando por aluno
    dados = sistema_de_registro.search_student(id_aluno)

    # limpando os campos de entrada
    e_nome.delete(0, END)
    e_email.delete(0, END)
    e_fone.delete(0, END)
    c_sexo.delete(0, END)
    data_nascimento.delete(0, END)
    e_end.delete(0, END)
    c_curso.delete(0, END)

    # inserir valores os campos de entradas
    e_nome.insert(END,dados[1])
    e_email.insert(END,dados[2])
    e_fone.insert(END,dados[3])
    c_sexo.insert(END,dados[4])
    data_nascimento.insert(END,dados[5])
    e_end.insert(END,dados[6])
    c_curso.insert(END,dados[7])

    imagem = dados[8]
    imagem_string = imagem

    imagem = Image.open(imagem)
    imagem = imagem.resize((130, 130))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frame_details, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=390, y=10)

# função atualizar
def atualizar():
    global imagem, imagem_string, l_imagem

    # obtendo o id
    id_aluno = int(e_procurar.get())

    # obtendo os valores
    nome = e_nome.get()
    email = e_email.get()
    tel = e_fone.get()
    sexo = c_sexo.get()
    data = data_nascimento.get()
    endereco = e_end.get()
    curso = c_curso.get()
    img = imagem_string

    lista = [nome, email, tel, sexo, data, endereco, curso, img, id_aluno]

    # varificado se a lista contem valor vazio
    for i in lista:
        if i == '':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return

    # registrando os valores
    sistema_de_registro.update_student(lista)

    # limpando os campos de entrada
    e_nome.delete(0,END)
    e_email.delete(0,END)
    e_fone.delete(0,END)
    c_sexo.delete(0,END)
    data_nascimento.delete(0,END)
    e_end.delete(0,END)
    c_curso.delete(0,END)

    # abrindo a imagem
    imagem = Image.open('logo.png')
    imagem = imagem.resize((130, 130))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frame_details, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=390, y=10)

    # mostrando os valores da tabela
    mostrar_alunos()

# função deletar
def deletar():
    global imagem, imagem_string, l_imagem

    # obtendo o id
    id_aluno = int(e_procurar.get())

    # deletando o aluno
    sistema_de_registro.delete_student(id_aluno)

    # limpando os campos de entrada
    e_nome.delete(0,END)
    e_email.delete(0,END)
    e_fone.delete(0,END)
    c_sexo.delete(0,END)
    data_nascimento.delete(0,END)
    e_end.delete(0,END)
    c_curso.delete(0,END)

    e_procurar.delete(0,END)

    # abrindo a imagem
    imagem = Image.open('logo.png')
    imagem = imagem.resize((130, 130))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frame_details, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=390, y=10)

    # mostrando os valores da tabela
    mostrar_alunos()



# Criando os campos de entrada ---------------------------------------

l_nome = Label(frame_details, text="Nome *", anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
l_nome.place(x=4, y=10)
e_nome = Entry(frame_details, width=30, justify="left", relief="solid")
e_nome.place(x=7, y=40)

l_email = Label(frame_details, text="Email *", anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
l_email.place(x=4, y=70)
e_email = Entry(frame_details, width=30, justify="left", relief="solid")
e_email.place(x=7, y=100)

l_fone = Label(frame_details, text="Telefone *", anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
l_fone.place(x=4, y=130)
e_fone = Entry(frame_details, width=15, justify="left", relief="solid")
e_fone.place(x=7, y=160)

l_sexo = Label(frame_details, text="Sexo *", anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
l_sexo.place(x=127, y=130)
c_sexo = ttk.Combobox(frame_details, width=7, font=("Ivy 8 bold"), justify='center')
c_sexo['values'] = ('M', 'F')
c_sexo.place(x=130, y=160)

l_data_nascimetno = Label(frame_details, text="Data de Nascimetno *", anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
l_data_nascimetno.place(x=220, y=10)
data_nascimento = DateEntry(frame_details, width=18, justify='center', background='darkblue', foreground='white', borderwidth=2, year=2024, date_pattern='dd/mm/yyyy')
data_nascimento.place(x=224, y=40)

l_end = Label(frame_details, text="Endereço *", anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
l_end.place(x=220, y=70)
e_end = Entry(frame_details, width=20, justify="left", relief="solid")
e_end.place(x=224, y=100)

cursos = ['Engenharia', 'Medicina', 'Social', 'Informática', 'Matemática']

l_curso = Label(frame_details, text="Cursos *", anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
l_curso.place(x=220, y=130)
c_curso = ttk.Combobox(frame_details, width=20, font=("Ivy 8 bold"), justify='center')
c_curso['values'] = (cursos)
c_curso.place(x=224, y=160)

# escolher imagem
def escolher_imagem():
    global imagem, imagem_string, l_imagem

    imagem = fd.askopenfilename()
    imagem_string=imagem

    imagem = Image.open(imagem_string)
    imagem = imagem.resize((130, 130))
    imagem = ImageTk.PhotoImage(imagem)
    l_imagem = Label(frame_details, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=390, y=10)

    botao_carregar['text'] = 'Trocar de foto'

botao_carregar = Button(frame_details, command=escolher_imagem, text='Carregar Foto'.upper(), width=20, compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=("Ivy 7 bold"), bg=co1, fg=co0)
botao_carregar.place(x=390, y=160)

#Tabela Alunos
def mostrar_alunos():

    #criando uma treeview com barras de rolagem duplas
    list_header = ['id', 'Nome', 'email', 'Telefone', 'sexo', 'Data', 'Endereço', 'Curso']

    # ver todos os alunos
    df_list = sistema_de_registro.view_all_students()

    tree_aluno = ttk.Treeview(frame_tabela, selectmode="extended", columns=list_header, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_aluno.yview)
    # horizontal scrollbar
    hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_aluno.xview)

    tree_aluno.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree_aluno.grid(column=0, row=1, sticky='nsew')
    vsb.grid(column=1, row=1, sticky='ns')
    hsb.grid(column=0, row=2, sticky='ew')
    frame_tabela.grid_rowconfigure(0, weight=12)

    hd=["nw", "nw", "nw", "center", "center","center", "center","center"]
    h=[40,150,150,70,70,70,120,100,100]
    n=0

    for co1 in list_header:
        tree_aluno.heading(co1, text=co1.title(), anchor=NW)
        # ajusta a largura da coluna de acordo com a string do cabeçalho
        tree_aluno.column(co1, width=h[n], anchor=hd[n])

        n+=1

    for item in df_list:
        tree_aluno.insert('', 'end', values=item)

# procurar aluno

frame_procurar = Frame(frame_botoes, width=40, height=50, bg=co1, relief=RAISED)
frame_procurar.grid(row=0, column=0, pady=10, padx=10, sticky=NSEW)

l_nome = Label(frame_procurar, text="Procurar aluno[Entra ID]", anchor=NW, font=("Ivy 10"), bg=co1, fg=co4)
l_nome.grid(row=0, column=0, pady=8, padx=0, sticky=NSEW)
e_procurar = Entry(frame_procurar, width=5, justify="center", relief="solid", font=("Ivy 10"))
e_procurar.grid(row=1, column=0, pady=9, padx=0, sticky=NSEW)

botao_procurar = Button(frame_procurar, command=procurar, text='Procurar', width=9, anchor=CENTER, overrelief=RIDGE, font=("Ivy 7 bold"), bg=co1, fg=co0)
botao_procurar.grid(row=1, column=1, pady=10, padx=0, sticky=NSEW)

# Botoes

app_img_adicionar = Image.open("add.png")
app_img_adicionar = app_img_adicionar.resize((25,25))
app_img_adicionar = ImageTk.PhotoImage(app_img_adicionar)
app_adicionar = Button(frame_botoes, command=adicionar, image=app_img_adicionar, text=' Adicionar', width=100, compound=LEFT, overrelief=RIDGE, font=("Ivy 11"), bg=co1, fg=co0)
app_adicionar.grid(row=1, column=0, pady=5, padx=10, sticky=NSEW)

app_img_atualizar = Image.open("atualizar.png")
app_img_atualizar = app_img_atualizar.resize((25,25))
app_img_atualizar = ImageTk.PhotoImage(app_img_atualizar)
app_atualizar = Button(frame_botoes, command=atualizar, image=app_img_atualizar, text=' Atualizar', width=100, compound=LEFT, overrelief=RIDGE, font=("Ivy 11"), bg=co1, fg=co0)
app_atualizar.grid(row=2, column=0, pady=5, padx=10, sticky=NSEW)

app_img_delete = Image.open("delete.png")
app_img_delete = app_img_delete.resize((25,25))
app_img_delete = ImageTk.PhotoImage(app_img_delete)
app_delete = Button(frame_botoes, command=deletar, image=app_img_delete, text=' Deletar', width=100, compound=LEFT, overrelief=RIDGE, font=("Ivy 11"), bg=co1, fg=co0)
app_delete.grid(row=3, column=0, pady=5, padx=10, sticky=NSEW)

# Linha separatoria
l_linha = Label(frame_botoes, relief=GROOVE, width=1, height=123, anchor=NW, font=("Ivy 1"), bg=co1, fg=co1)
l_linha.place(x=227, y=15)

# chamar tabela
mostrar_alunos()

janela.mainloop()
