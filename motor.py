import pandas as pd
import sqlite3
from sklearn.linear_model import LogisticRegression

def procesar_datos_y_entrenar():
    # 1. Conectar a Base de Datos
    conn = sqlite3.connect('mundial.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS equipos (nombre TEXT PRIMARY KEY, elo REAL)')
    
    # 2. Leer el historial de partidos
    df = pd.read_csv('datos.csv')
    
    # 3. Diccionario para calcular ELO
    elos = {}
    def obtener_elo(equipo):
        return elos.get(equipo, 1500.0)

    diff_elos = []
    resultados = []

    # 4. Calcular el ELO partido a partido
    for index, row in df.iterrows():
        local = row['local']
        visitante = row['visitante']
        gl = row['goles_local']
        gv = row['goles_visitante']
        
        elo_l = obtener_elo(local)
        elo_v = obtener_elo(visitante)
        
        diff_elos.append(elo_l - elo_v)
        
        if gl > gv: res_l = 1
        elif gl == gv: res_l = 0.5
        else: res_l = 0
        
        resultados.append(1 if gl > gv else 0)
        
        prob_l = 1 / (1 + 10 ** ((elo_v - elo_l) / 400))
        k = 40
        
        elos[local] = elo_l + k * (res_l - prob_l)
        elos[visitante] = elo_v + k * ((1 - res_l) - (1 - prob_l))

    # 5. Guardar en la base de datos
    for equipo, elo in elos.items():
        cursor.execute('INSERT OR REPLACE INTO equipos (nombre, elo) VALUES (?, ?)', (equipo, elo))
    conn.commit()
    
    # 6. Entrenar el modelo de Machine Learning
    X = pd.DataFrame({'diff_elo': diff_elos})
    y = pd.Series(resultados)
    
    modelo = LogisticRegression()
    modelo.fit(X, y)
    
    return modelo, conn

def predecir(modelo, conn, local, visitante):
    cursor = conn.cursor()
    cursor.execute('SELECT elo FROM equipos WHERE nombre = ?', (local,))
    res_l = cursor.fetchone()
    elo_l = res_l[0] if res_l else 1500.0
    
    cursor.execute('SELECT elo FROM equipos WHERE nombre = ?', (visitante,))
    res_v = cursor.fetchone()
    elo_v = res_v[0] if res_v else 1500.0
    
    diff = [[elo_l - elo_v]]
    probabilidad = modelo.predict_proba(diff)[0][1]
    
    return probabilidad, elo_l, elo_v
