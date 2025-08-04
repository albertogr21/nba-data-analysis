import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('nba_2025_per_game.csv')


print(df.info())
print(df.describe())


top_scorers = df.sort_values(by='PTS', ascending=False).head(10)
print("Top 10 anotadores:\n", top_scorers[['Player', 'PTS', 'G']])


plt.figure(figsize=(12, 6))
sns.barplot(x='PTS', y='Player', data=top_scorers, palette='viridis')
plt.title('Top 10 Jugadores - Puntos por Partido (NBA 2025)')
plt.xlabel('Puntos por Partido')
plt.ylabel('Jugador')
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 6))
sns.barplot(x='PTS', y='Player', data=top_scorers, palette='viridis', legend=False)
plt.title('Minutos vs Puntos por Partido')
plt.xlabel('Minutos por Partido')
plt.ylabel('Puntos por Partido')
plt.grid(True)
plt.tight_layout()
plt.show()

correlation = df[['PTS', 'AST', 'TRB', 'STL', 'BLK']].corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Correlación entre estadísticas clave')
plt.show()

df.to_csv('nba_2025_clean.csv', index=False)
