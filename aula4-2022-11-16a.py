# 1º passo: importar biblioteca sqlite3
import sqlite3

#2º passo: Vamos estabelecer uma conexção com o banco de dados
conexao = sqlite3.connect("dc_universe.db")

#3º passo: Criar um objeto do tipo cursosr
cursor = conexao.cursor()

#4º passo:Comando SQL do banco
sql = "SELECT pessoa_id, nome, nome_civil, tipo FROM pessoas"

#5º passo: Executar o comando SQÇ no SQLlite (no cursor)
cursor.execute(sql)

#6º passo: Exibir a consulta com todos os nomes de heróis e vilões do banco de dados
pessoas = cursor.fetchall()
for pessoa in pessoas:
  print(pessoa)