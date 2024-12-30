import pandas as pd
import sqlite3


lista_tecnica = pd.read_excel('Lista tecnica.xlsx')
lista_pedidos = pd.read_excel('Lista de pedidos.xlsx')



conn = sqlite3.connect('Lista.db')
cursor = conn.cursor()

lista_tecnica.to_sql('lista_tecnica', conn, if_exists='replace', index=False)
lista_pedidos.to_sql('lista_de_pedidos',conn,if_exists='replace',index=False)

cursor.execute("SELECT lista_de_pedidos.Pedido,lista_tecnica.Produto,lista_tecnica.cod1,lista_tecnica.Qtde1,lista_tecnica.cod2,lista_tecnica.Qtde2,lista_tecnica.cod3,lista_tecnica.Qtde3,lista_de_pedidos.Qtd FROM lista_de_pedidos INNER JOIN lista_tecnica ON lista_de_pedidos.Codigo = lista_tecnica.Produto;")



nova_lista = []
for linha in cursor.fetchall():
    concatenado = f'{linha[0]}{linha[1]}{linha[2]}'
    lista = {"Pedido":linha[0],"Produto":linha[1],"Cod1":linha[2],"Qtde1":linha[3],"Cod2":linha[4],"Qtde2":linha[5],"Cod3":linha[6],"Qtde3":linha[7],"Qtd total":float(linha[8]),"CodConcatenado":concatenado}
    nova_lista.append(lista)
    
df =  pd.DataFrame(nova_lista)
df.drop_duplicates(subset=['CodConcatenado']).to_excel("resultado.xlsx",index=False)



conn.commit()
conn.close()