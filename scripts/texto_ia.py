import pandas as pd 
from openai import OpenAI
import os
from dotenv import load_dotenv
import numpy as np
import time

# Cargar archivo .env
load_dotenv()

# Crear cliente OpenAI con API Key desde entorno
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Cargar CSV de estadísticas de partidos
basket_df = pd.read_csv('base_completa_basket.csv')

# Cargar CSV de métricas físicas (CMJ)
cmj_df = pd.read_csv('CMJ.csv')

# Limpieza de nombres de columnas
basket_df.columns = basket_df.columns.str.strip()
cmj_df.columns = cmj_df.columns.str.strip()

# Agrupar estadísticas de partidos por jugadora
agrupados = basket_df.groupby(['ID', 'Jugador'], as_index=False).agg({
    'Pt': 'sum',
    'MIN': 'sum',
    'TC': 'mean',
    'TirInt': 'mean',
    '2PC': 'mean',
    '3PC': 'mean',
    'TLC': 'mean'
})

#Calcular el porcentaje de tiro real antes de unir
agrupados['Porcentaje_Tiro_Real'] = agrupados['TC'] / agrupados['TirInt'].replace(0, np.nan)

# Unir las tablas manteniendo todos los jugadores del archivo de basket
df_completo = pd.merge(agrupados, cmj_df, on='ID', how='left')

#cuadrantes excentricos
umbral_duracion_eccentric = df_completo['Eccentric Duration [ms]'].median(skipna=True)
umbral_fuerza_eccentric = df_completo['Eccentric Peak Force [N]'].median(skipna=True)

def asignar_cuadrante_excentrico(row, umbral_duracion_eccentric , umbral_fuerza_eccentric):
    ed = row.get('Eccentric Duration [ms]', None)
    epf = row.get('Eccentric Peak Force [N]', None)

    if pd.isnull(ed) or pd.isnull(epf):
        return 'No disponible'
    
    if ed < umbral_duracion_eccentric and epf < umbral_fuerza_eccentric:
        return 'Cuadrante 1'
    elif ed < umbral_duracion_eccentric and epf >= umbral_fuerza_eccentric:
        return 'Cuadrante 2'
    elif ed >= umbral_duracion_eccentric and epf < umbral_fuerza_eccentric:
        return 'Cuadrante 4'
    elif ed >= umbral_duracion_eccentric and epf >= umbral_fuerza_eccentric:
        return 'Cuadrante 3'
    else:
        return 'Sin clasificar'
    
df_completo['Cuadrante_Excentrico'] = df_completo.apply(
    lambda row: asignar_cuadrante_excentrico(row, umbral_duracion_eccentric, umbral_fuerza_eccentric),
    axis=1
)

#cuadrantes concentricos
umbral_duracion_concentric = df_completo['Concentric Duration [ms]'].median(skipna=True)
umbral_fuerza_concentric = df_completo['Concentric Peak Force [N]'].median(skipna=True)

def asignar_cuadrante_concentrico(row, umbral_duracion_concentric, umbral_fuerza_concentric):
    cd = row.get('Concentric Duration [ms]', None)
    cpf = row.get('Concentric Peak Force [N]', None)

    if pd.isnull(cd) or pd.isnull(cpf):
        return 'No disponible'
     
    if cd < umbral_duracion_concentric and cpf < umbral_fuerza_concentric:
        return 'Cuadrante 5'
    elif cd < umbral_duracion_concentric and cpf >= umbral_fuerza_concentric:
        return 'Cuadrante 6'
    elif cd >= umbral_duracion_concentric and cpf < umbral_fuerza_concentric:
        return 'Cuadrante 8'
    elif cd >= umbral_duracion_concentric and cpf >= umbral_fuerza_concentric:
        return 'Cuadrante 7'
    else:
        return 'Sin clasificar'
    
df_completo['Cuadrante_Concentrico'] = df_completo.apply(
    lambda row: asignar_cuadrante_concentrico(row, umbral_duracion_concentric, umbral_fuerza_concentric),
    axis=1
)

#Lista para guardar resultados
textos_generados = []

#Bucle para cada jugador
for i, row in df_completo.iterrows():
    print(f"Procesando jugador {i+1} de {len(df_completo)}: {row['Jugador_x']}")
    try:
        nombre = row['Jugador_x']
        puntos = row['Pt']
        minutos = row['MIN']
        porcentaje_tiro_real = round(row['Porcentaje_Tiro_Real'] * 100, 2)
        cuadrante_excentrico = row.get('Cuadrante_Excentrico', 'no determinado')
        cuadrante_concentrico = row.get('Cuadrante_Concentrico', 'no determinado')
    
        prompt = f"""
Eres un analista deportivo. Elabora un texto de 3 renglones para un informe de scouting. Escribe en español y usa un tono técnico pero claro. 
Incluye nombre, puntos anotados, minutos jugados, y el porcentaje de tiro real. 
Después, da una recomendación de ejercicio basada en el cuadrante biomecánico. 

Datos:
Jugador: {nombre}
Puntos: {puntos}
Minutos jugados: {minutos}
Porcentaje de tiro real: {porcentaje_tiro_real}%
Cuadrante Excentrico: {cuadrante_excentrico}
Cuadrante Concentrico: {cuadrante_concentrico}

Cuadrantes y recomendaciones:
- Cuadrante 1: "Trabajar tiempo bajo tensión."
- Cuadrante 2: "Se sugiere trabajar excéntricos acentuados."
- Cuadrante 3: "Conviene trabajar drop landings."
- Cuadrante 4: "Podemos enfocarnos en trabajar drop & catch."
- Cuadrante 5: "Trabajar ejercicios isocinéticos."
- Cuadrante 6: "Se sugiere trabajar ejercicios balisticos."
- Cuadrante 7: "Conviene realizar levantamientos olimpicos."
- Cuadrante 8: "Podemos enfocarnos en trabajar iso-hold."
    """

        respuesta = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Eres un analista deportivo que genera descripciones técnicas de jugadores."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        texto = respuesta.choices[0].message.content.strip()
        textos_generados.append(texto)
        time.sleep(2)
    
    except Exception as e:
        print(f"Error con el jugador {nombre}: {e}")
        textos_generados.append("Error al generar texto")

df_completo['Texto_IA'] = textos_generados
df_completo[['ID', 'Jugador_x', 'Texto_IA']].to_csv('scouting_automatico.csv', index=False, encoding='utf-8-sig')
print("¡Listo! Archivo generado como 'scouting_automatico.csv'.")
