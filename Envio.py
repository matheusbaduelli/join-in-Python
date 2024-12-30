# import pandas as pd
# import sqlite3


# lista_tecnica = pd.read_excel('Lista tecnica.xlsx')
# lista_pedidos = pd.read_excel('Lista de pedidos.xlsx')



# conn = sqlite3.connect('Lista.db')
# cursor = conn.cursor()

# # lista_tecnica.to_sql('lista_tecnica', conn, if_exists='replace', index=False)
# # lista_pedidos.to_sql('lista_de_pedidos',conn,if_exists='replace',index=False)
# query = "SELECT lista_de_pedidos.Pedido,lista_tecnica.Produto,lista_tecnica.cod1,lista_tecnica.Qtde1,lista_tecnica.cod2,lista_tecnica.Qtde2,lista_tecnica.cod3,lista_tecnica.Qtde3 FROM lista_de_pedidos INNER JOIN lista_tecnica ON lista_de_pedidos.Codigo = lista_tecnica.Produto;"
# # lista_tecnica = pd.read_sql_query(query, conn)
# # lista_tecnica.to_excel('resultado.xlsx', index=False)

# # cursor.execute("CREATE VIEW IF NOT EXISTS lista_final AS SELECT lista_de_pedidos.Pedido,lista_tecnica.Produto,lista_tecnica.cod1,lista_tecnica.Qtde1,lista_tecnica.cod2,lista_tecnica.Qtde2 FROM lista_de_pedidos INNER JOIN lista_tecnica ON lista_de_pedidos.Codigo = lista_tecnica.Produto;")


# query2 = (query)
# lista_tecnica = pd.read_sql_query(query, conn)
# result = cursor.execute(query)


# lista_nova = []
# for resultado in result.fetchall():
#     text = f'{resultado[0]}{resultado[1]}{resultado[2]}'
#     lista = [{"1":resultado[0],"2":text}]
#     lista_nova.append(lista)


# # print(lista_nova)
# df = pd.DataFrame(lista_nova)

# print(df)
    
    
#     # print(lista)

# #     lista_unica = []
# #     for item in lista:
# #         if item not in lista_unica:
# #             lista_unica.append(item)
# #     listagem = pd.DataFrame(lista_unica)
    

# df.to_excel('resultado.xlsx', index=False)
# # listagem = pd.DataFrame(lista_unica)
# # # listagem.to_excel('resultado.xlsx', index=False)

# # print(listagem)
    
#     # result.append(lista)

# # print(resultado)






# # for listagem in result2:
# #     concatenar = listagem[0] + " " + listagem[1]
# #     print(concatenar)
    

# # for listagem in result2:
# #     print(listagem)


# # dados = [
# #     ["João", "Silva"],
# #     ["Maria", "Souza"],
# #     ["Carlos", "Oliveira"]
# # ]

# # Adicionando uma nova coluna com valores concatenados (nome completo)
# # for linha in dados:
# #     nome_completo = linha[0] + " " + linha[1]
# #     linha.append(nome_completo)

# # Exibindo o resultado
# # for linha in dados:
# #     print(linha)

# conn.commit()
# conn.close()





print(3*2)

# # l = lista[1]
# print(lista)

# print(lista)









    

