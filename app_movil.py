import pandas as pd
from motor import procesar_datos_y_entrenar, predecir

def main():
    print("Iniciando sistema y entrenando la IA...\n")
    modelo, conn = procesar_datos_y_entrenar()
    
    # Extraer equipos disponibles
    equipos_df = pd.read_sql_query("SELECT nombre FROM equipos ORDER BY nombre", conn)
    lista_equipos = equipos_df['nombre'].tolist()
    
    print("======================================")
    print("   🏆 PREDICTOR MUNDIAL DE FÚTBOL 🏆  ")
    print("======================================")
    
    while True:
        print("\nEquipos disponibles:")
        print(", ".join(lista_equipos))
        print("-" * 38)
        
        # Pedir datos al usuario
        local = input("Escribe el equipo LOCAL (o 'salir' para cerrar): ").strip()
        if local.lower() == 'salir':
            print("Cerrando la aplicación...")
            break
            
        visitante = input("Escribe el equipo VISITANTE: ").strip()
        
        # Validar que los equipos existan
        if local not in lista_equipos or visitante not in lista_equipos:
            print("\n⚠️ ERROR: Uno de los equipos no está en la lista.")
            print("Asegúrate de escribir el nombre exactamente igual (respetando mayúsculas).")
            continue
            
        if local == visitante:
            print("\n⚠️ ERROR: Seleccionaste el mismo equipo dos veces.")
            continue
            
        # Hacer la predicción
        probabilidad, elo_l, elo_v = predecir(modelo, conn, local, visitante)
        
        # Mostrar el resultado
        print("\n" + "=" * 38)
        print("          📊 RESULTADOS 📊          ")
        print("=" * 38)
        print(f"PUNTUACIÓN ELO: {local} ({elo_l:.0f}) vs {visitante} ({elo_v:.0f})")
        print(f"📈 Probabilidad de que {local} GANE: {probabilidad:.2%}")
        print(f"📉 Probabilidad de EMPATE/Derrota: {1 - probabilidad:.2%}")
        print("======================================\n")

if __name__ == "__main__":
    main()
