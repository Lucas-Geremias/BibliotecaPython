import mysql.connector


def conectar():
  conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="biblioteca"
  )
  return conexao


def adicionar_livro(titulo, autor, ano_publicacao):
  conexao = conectar()
  cursor = conexao.cursor()

  sql = "INSERT INTO livros(titulo, autor, ano_publicacao) VALUES (%s, %s, %s)"
  
  valores = (titulo, autor, ano_publicacao)
  cursor.execute(sql,valores)
  conexao.commit()
  conexao.close()
  print("Livro Adicionado com sucesso!!!!")
  
def listar_livros():
  conexao = conectar()
  cursor = conexao.cursor()
  
  cursor.execute("SELECT * FROM livros")
  livros = cursor.fetchall #pega todos os resultados 
  conexao.close()
  
  if livros:
    print("lista de livros: ")
    for livro in livros:
      print(f"ID: {livro[0]} | Título: {livro[1]} | Autor: {livro[2]} | Ano: {livro[3]}")
  else:
    print("Nenhum livro encontrado.")
