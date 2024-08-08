import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de la página web de estadísticas
url = "https://info.jockeypronosticos.com/estads.php?anioE=2024"

# Realizar la solicitud HTTP
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Analizar el contenido HTML de la página
    soup = BeautifulSoup(response.content, "html.parser")

    # Encontrar las tablas de estadísticas
    tables = soup.find_all("table")

    # Verificar que se encontraron tablas
    if len(tables) >= 2:
        # La primera tabla contiene estadísticas de jockeys
        jockey_table = tables[0]
        # La segunda tabla contiene estadísticas de entrenadores
        trainer_table = tables[1]

        # Función para extraer datos de una tabla HTML
        def extract_table_data(table):
            headers = []
            data = []
            
            # Obtener encabezados
            for th in table.find("tr").find_all("th"):
                headers.append(th.text.strip())
            
            # Obtener filas de datos
            for row in table.find_all("tr")[1:]:
                cols = row.find_all("td")
                row_data = [col.text.strip() for col in cols]
                if len(row_data) > 0:
                    data.append(row_data)
            
            return headers, data

        # Extraer datos de la tabla de jockeys
        jockey_headers, jockey_data = extract_table_data(jockey_table)
        jockey_df = pd.DataFrame(jockey_data, columns=jockey_headers)

        # Extraer datos de la tabla de entrenadores
        trainer_headers, trainer_data = extract_table_data(trainer_table)
        trainer_df = pd.DataFrame(trainer_data, columns=trainer_headers)

        # Mostrar las primeras filas de los DataFrames
        print("Estadísticas de Jockeys")
        print(jockey_df.head())

        print("\nEstadísticas de Entrenadores")
        print(trainer_df.head())

        # Guardar los DataFrames en archivos CSV para análisis posterior
        jockey_df.to_csv("C:\Python Varios\AnalisisHipico\estadisticas_jockeys_2024.csv", index=False, encoding='utf-8-sig')
        trainer_df.to_csv("C:\Python Varios\AnalisisHipico\estadisticas_entrenadores_2024.csv", index=False, encoding='utf-8-sig')
    else:
        print("No se encontraron las tablas de estadísticas esperadas.")
else:
    print(f"Error al acceder a la página web: {response.status_code}")
