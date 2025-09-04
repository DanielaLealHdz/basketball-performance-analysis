import pandas as pd 

df_stats = pd.read_csv("estadisticas_8_grandes_limpias.csv", encoding= "latin1")

df_info = pd.read_csv("info_jugadores.csv", encoding="latin1")

df_info.rename(columns={"ï»¿ID": "ID"}, inplace=True)

df_info["POSICION"] = df_info["POSICION"].str.strip()
df_info["POSICION"] = df_info["POSICION"].replace({
    "DELANTERO PEQUEÃ\x91O": "DELANTERO PEQUEÑO",
    "DELANTERO": "DELANTERO",
    "DELANTERO ": "DELANTERO"  # espacio extra
})

df_merged = pd.merge(df_stats, df_info, on="ID", how="left")

df_merged.to_csv("base_completa_basket.csv", index=False, encoding= "utf-8-sig")

