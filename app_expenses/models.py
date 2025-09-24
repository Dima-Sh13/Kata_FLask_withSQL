import sqlite3
from app_expenses import ORIGIN_DATA

def select_all():
    conexion = sqlite3.connect(ORIGIN_DATA)
    cur = conexion.cursor()
    res = cur.execute("SELECT * from movements;")
    filas = res.fetchall()#datos de columnas (2025-09-01, Nomina,1800),(2025-09-05,Mercado,-100)
    columnas = res.description#nombre de columnas en las primeras filas (id,0000),(date,000)

    lista_diccionario= []
    
    for f in filas:
        posicion = 0
        diccionario = {}
        for c in columnas:
            diccionario[c[0]] =  f[posicion]
            posicion+=1
        lista_diccionario.append(diccionario)

    conexion.close()
    
    return lista_diccionario

def insert(registroForm):
    conexion = sqlite3.connect(ORIGIN_DATA)
    cur = conexion.cursor()
    res = cur.execute("INSERT INTO movements (date, concept, amount) VALUES (?,?,?);",registroForm)
    conexion.commit()#funcion para validar el registro antes de guardarlo

    conexion.close()

def select_by(id):
    conexion= sqlite3.connect(ORIGIN_DATA)
    cur = conexion.cursor()
    res = cur.execute(f"SELECT * from movements WHERE id={id};")
    result = res.fetchall()
    return result[0]



