Solar Data Dashboard Project

Overview
This project focuses on analyzing solar radiation data from multiple locations and building an interactive dashboard to visualize and explore insights. The dashboard is built using Streamlit and leverages cleaned and combined datasets for enhanced usability.

Features
- Interactive Data Exploration:
  - Filter data by location (e.g., Benin-Malanville, Sierra Leone-Bumbuna, Togo-Dapaong).
  - Visualize trends over time for key metrics like GHI (Global Horizontal Irradiance).
  - Correlation heatmaps for understanding relationships between variables.
  - Histograms to explore the distribution of selected variables.
  - Evaluate the impact of cleaning on sensor readings.

- Streamlit Dashboard:
  - User-friendly and highly interactive.
  - Deployed online for easy access.

Project Structure
```plaintext
├── .streamlit/
│   └── config.toml          # Streamlit configuration file
├── app/
│   ├── main.py              # Main Streamlit application script
│   ├── utils.py             # Utility functions for data processing
├── data/
│   ├── benin-malanville.csv # Dataset for Benin
│   ├── sierraleone-bumbuna.csv # Dataset for Sierra Leone
│   ├── togo-dapaong_qc.csv  # Dataset for Togo
│   └── combined_solar_data.csv # Combined and cleaned dataset
├── requirements.txt         # List of Python dependencies
├── README.md                # Project documentation (this file)
└── scripts/
    └── eda.py               # Script for exploratory data analysis
```

Installation
To run this project locally, follow these steps:

1. Clone the repository:
   
   git clone https://github.com/olanak/solar-data-analysis
   cd solar-data-analysis
   

2. Create and activate a virtual environment:

   python -m venv venv
   source venv/bin/activate  # On Linux/MacOS
   venv\Scripts\activate     # On Windows
   

3. Install dependencies:

   pip install -r requirements.txt
   

4. Run the Streamlit app:

   streamlit run app/main.py
   

Usage
- Launch the dashboard using the above command.
- Use the sidebar to:
  - Select a location for analysis.
  - Choose variables for visualizations like histograms.
  - Toggle options like correlation heatmaps or cleaning impact evaluation.

Data Sources
The project uses datasets from three locations:
1. Benin-Malanville
2. Sierra Leone-Bumbuna
3. Togo-Dapaong

These datasets were combined and cleaned for analysis. The cleaned dataset is stored as `combined_solar_data.csv`.

Key Visualizations
1. Time-Series Trends:
   - Analyze GHI trends over time for each location.
2. Correlation Heatmaps:
   - Discover relationships between variables like GHI, DNI, DHI, wind speed, and temperature.
3. Histograms:
   - Visualize distributions for key metrics like solar radiation and wind speed.
4. Impact of Cleaning:
   - Compare sensor readings before and after cleaning events.

Deployment
The dashboard is deployed using Streamlit Community Cloud:
- Live Dashboard: [Dashboard Link](#) (Add your deployed link here)






