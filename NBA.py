import pandas as pd

# URL de la tabla de estadísticas por partido NBA 2025
url = "https://www.basketball-reference.com/leagues/NBA_2025_per_game.html"

# Usa pandas para leer la tabla directamente
tables = pd.read_html(url)

# La primera tabla (posiblemente única) es la que queremos
df = tables[0]

# Eliminar filas repetidas del encabezado (algunos jugadores tienen dos filas por traspasos)
df = df[df['Player'] != 'Player']  # Quita los duplicados del header

# Reiniciar el índice
df.reset_index(drop=True, inplace=True)

# Convertir columnas numéricas adecuadamente
drop_cols = [col for col in ['Player', 'Pos', 'Tm'] if col in df.columns]
numeric_cols = df.columns.drop(drop_cols)


# Mostrar primeras filas
print(df.head())

# Guardar en CSV
df.to_csv('nba_2025_per_game.csv', index=False)


