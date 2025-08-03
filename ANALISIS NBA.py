import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar datos
df = pd.read_csv('nba_2025_per_game.csv')

# Revisar estructura
print(df.info())
print(df.describe())

# Top 10 anotadores
top_scorers = df.sort_values(by='PTS', ascending=False).head(10)
print("Top 10 anotadores:\n", top_scorers[['Player', 'PTS', 'G']])

# Visualización: Top 10 jugadores por puntos por partido
plt.figure(figsize=(12, 6))
sns.barplot(x='PTS', y='Player', data=top_scorers, palette='viridis')
plt.title('Top 10 Jugadores - Puntos por Partido (NBA 2025)')
plt.xlabel('Puntos por Partido')
plt.ylabel('Jugador')
plt.tight_layout()
plt.show()

# Relación entre minutos jugados y puntos
plt.figure(figsize=(10, 6))
sns.barplot(x='PTS', y='Player', data=top_scorers, palette='viridis', legend=False)
plt.title('Minutos vs Puntos por Partido')
plt.xlabel('Minutos por Partido')
plt.ylabel('Puntos por Partido')
plt.grid(True)
plt.tight_layout()
plt.show()

# Correlación entre estadísticas clave
# Correlación entre estadísticas clave
correlation = df[['PTS', 'AST', 'TRB', 'STL', 'BLK']].corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Correlación entre estadísticas clave')
plt.show()
