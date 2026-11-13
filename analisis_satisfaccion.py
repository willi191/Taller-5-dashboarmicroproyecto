import pandas as pd
from pathlib import Path

ruta = Path(__file__).parents[1] / 'data' / 'respuestas_satisfaccion.csv'
df = pd.read_csv(ruta, parse_dates=['fecha'])
print('Registros:', len(df))
print('Satisfacción media:', round(df['satisfaccion_general'].mean(), 2))
print('Satisfacción positiva (% >= 4):', round((df['satisfaccion_general'].ge(4).mean())*100, 1))
print('Insatisfacción (% <= 2):', round((df['satisfaccion_general'].le(2).mean())*100, 1))
print('\nPromedio por servicio:')
print(df.groupby('servicio')['satisfaccion_general'].mean().round(2))
print('\nPromedio por dimensión:')
cols=['calidad','atencion','tiempo_respuesta','claridad','solucion']
print(df[cols].mean().round(2))
