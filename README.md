# 🏀 Basketball Performance Dashboard  

This project is an **interactive Power BI dashboard** designed to analyze the performance of university basketball players. It integrates both game statistics and jump metrics collected with force platforms.  

## 📂 Repository Structure  
- **/data** → Contains the datasets (with anonymized player names).  
- **/dashboard** → Includes the Power BI template (`.pbit`).  
- **/images** → Dashboard screenshots for reference.  
- **/scripts** → Python code for data cleaning, preprocessing, and automatic text generation with OpenAI.  

## ⚙️ Features  
- 📊 Visualization of **game statistics** (minutes, points, rebounds, attempted and made shots).  
- 🦵 Integration with **CMJ jump metrics** (height, RSI-mod, peak force, etc.).  
- 🔄 Interactive filters by player and rival.  
- 📈 Biomechanical analysis with **braking and propulsion quadrants**.  
- 🤖 Automatic report generation using **OpenAI API**.  
- 🌍 Online demo available in Power BI.  

## 🚀 How to Use  
1. Download the template from `/dashboard/basketball_dashboard.pbit`.  
2. Connect it to the files in `/data`.  
3. Explore the interactive visualizations.  

## 🌐 Online Demo  
👉 [View Interactive Dashboard in Power BI](https://app.powerbi.com/view?r=eyJrIjoiYjNhN2FhZmEtMmUzZS00ZmE2LWIwMmUtNzgwN2Q0MzlhMGJkIiwidCI6ImNhY2E5MDExLTdiNmEtNDRkZS04NjFmLTA5NWEyY2E4ODNiNyIsImMiOjR9)  

## 📸 Preview  
Examples of the dashboard (files in `/images`):  

- **Main Page**  
  ![Main Page](/images/Pagina_principal.png)  

- **Game Statistics (Filtered by Match)**  
  ![Stats by Match](/images/EstadisticasFiltradasPorPartido.png)  

- **Player Statistics (Filtered by Player)**  
  ![Stats by Player](/images/EstadisticasFiltradasPorJugador.png)  

- **Individual Player Page**  
  ![Individual Page](/images/Pagina_individual.png)  

- **Biomechanical Comparisons**  
  ![Comparisons](/images/Pagina_Comparaciones.png)  

## 🛠️ Tech Stack  
- **Power BI** for visualization.  
- **Python (pandas)** for data cleaning.  
- **Excel** as data source.  
- **OpenAI API** for automated report generation.  

---

🌐 This README is also available in [Spanish](README_es.md).