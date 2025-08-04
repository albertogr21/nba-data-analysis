import pandas as pd


url = "https://www.basketball-reference.com/leagues/NBA_2025_per_game.html"

# Usa pandas para leer la tabla directamente
tables = pd.read_html(url)


df = tables[0]


df = df[df['Player'] != 'Player']  # Quita los duplicados del header


df.reset_index(drop=True, inplace=True)


drop_cols = [col for col in ['Player', 'Pos', 'Tm'] if col in df.columns]
numeric_cols = df.columns.drop(drop_cols)



print(df.head())


df.to_csv('nba_2025_per_game.csv', index=False)


