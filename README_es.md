# 🏀 Basketball Performance Dashboard  

Este proyecto es un **dashboard interactivo en Power BI** diseñado para analizar el rendimiento de jugadoras de basketball universitario. Integra tanto estadísticas de juego como métricas de salto obtenidas en plataforma de fuerza.  

## 📂 Estructura del repositorio  
- **/data** → Contiene las bases de datos utilizadas (con nombres anonimizados de jugadores).  
- **/dashboard** → Incluye la plantilla de Power BI (`.pbit`).  
- **/images** → Capturas del dashboard para referencia.  
- **/scripts** → Código en Python para limpieza, preprocesamiento y generación automática de texto con OpenAI.  

## ⚙️ Funcionalidades  
- 📊 Visualización de **estadísticas de partido** (minutos, puntos, rebotes, tiros intentados y convertidos).  
- 🦵 Integración con métricas de **salto CMJ** (altura, RSI-mod, fuerza pico, etc.).  
- 🔄 Filtros interactivos por jugador y por rival.  
- 📈 Análisis biomecánico mediante **cuadrantes de frenado y propulsión**.  
- 🤖 Generación de reportes automáticos con **OpenAI API**.  
- 🌍 Versión online disponible en Power BI.  

## 🚀 Cómo usarlo  
1. Descargar la plantilla desde `/dashboard/basketball_dashboard.pbit`.  
2. Conectar a los archivos de `/data`.  
3. Explorar las visualizaciones interactivas.  

## 🌐 Demo Online  
👉 [Ver Dashboard Interactivo en Power BI](https://app.powerbi.com/view?r=eyJrIjoiYjNhN2FhZmEtMmUzZS00ZmE2LWIwMmUtNzgwN2Q0MzlhMGJkIiwidCI6ImNhY2E5MDExLTdiNmEtNDRkZS04NjFmLTA5NWEyY2E4ODNiNyIsImMiOjR9)  

## 📸 Vista previa  
Aquí se muestran ejemplos del dashboard (archivos en `/images`):  

- **Página principal**  
  ![Página Principal](/images/Pagina_principal.png)  

- **Estadísticas filtradas por partido**  
  ![Estadísticas por Partido](/images/EstadisticasFiltradasPorPartido.png)  

- **Estadísticas filtradas por jugador**  
  ![Estadísticas por Jugador](/images/EstadisticasFiltradasPorJugador.png)  

- **Página individual del jugador**  
  ![Página Individual](/images/Pagina_individual.png)  

- **Comparaciones biomecánicas**  
  ![Comparaciones](/images/Pagina_Comparaciones.png)  

## 🛠️ Tecnologías  
- **Power BI** para la visualización.  
- **Python (pandas)** para limpieza de datos.  
- **Excel** como fuente de datos.  
- **OpenAI API** para generación de reportes automáticos.  