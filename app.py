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

#Atualizar os livros

def atualizar_livros(id_livro, novo_titulo, novo_autor, novo_ano ):
  conexao = conectar()
  cursor = conexao.cursor()
  
  sql = """
    UPDATE livros
    SET titulo = %s, autor = %s, ano_pubicacao = %s
    WHERE id %s
  """
  valores = (novo_titulo, novo_autor, novo_ano, id_livro)
  
  cursor.execute(sql, valores)
  conexao.commit()
  conexao.close()
  print("Livro atualizado com sucesso!!!")
  
  ##DELETE - EXCLUIR UM LIVRO
  
  def excluir_livro(id_livro):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM livros  WHERE id = %s", (id_livro,))
    conexao.commit()
    conexao.close()
    
    print("Livro excluido com sucesso")

    
    ##MENU 
    def menu():
      while true:
        print("=== SISTEMA DE BIBLIOTECA ===")
        print("1 - Adicionar")
        print("2 - Listar Livros")
        print("3 - Atualizar Livros")
        print("4 - Excluir Livros")
        print("0 - Sair")

        opcao = input("Escolha uma opção")
        
        #Cadastrar livro
        if opcao == "1":
          titulo = input("Título: ")
          autor = input("Autor: ")
          ano = input("Ano de publicação: ")
          adicionar_livro(titulo,autor,ano)
          
    