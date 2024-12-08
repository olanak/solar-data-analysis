import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the combined dataset
@st.cache
def load_data():
    df = pd.read_csv('data/combined_solar_data.csv', parse_dates=['Timestamp'])
    return df

df = load_data()

# Dashboard title
st.title("Solar Data Dashboard")
st.sidebar.title("Dashboard Options")

# Dataset Overview
st.header("Dataset Overview")
st.write("Below is a preview of the dataset:")
st.dataframe(df.head())

# Filter by Location
locations = df['Location'].unique()
selected_location = st.sidebar.selectbox("Select a Location", locations)
filtered_df = df[df['Location'] == selected_location]

# Visualization: GHI Trends
st.header("GHI Trends Over Time")
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(filtered_df['Timestamp'], filtered_df['GHI'], label='GHI', color='blue')
ax.set_title(f"GHI Trends: {selected_location}")
ax.set_xlabel("Timestamp")
ax.set_ylabel("GHI")
st.pyplot(fig)

# Correlation Analysis
st.header("Correlation Analysis")
if st.checkbox("Show Correlation Heatmap"):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(filtered_df.corr(), annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
    st.pyplot(fig)

# Data Distribution: Histograms
st.header("Data Distribution")
selected_variable = st.sidebar.selectbox("Select a Variable for Histogram", ['GHI', 'DNI', 'DHI', 'WS', 'ModA', 'ModB'])
fig, ax = plt.subplots()
filtered_df[selected_variable].hist(bins=20, ax=ax)
ax.set_title(f"Histogram of {selected_variable}")
ax.set_xlabel(selected_variable)
ax.set_ylabel("Frequency")
st.pyplot(fig)

# Impact of Cleaning on Sensor Readings
st.header("Impact of Cleaning")
if 'Cleaning' in df.columns:
    cleaning_effect = filtered_df.groupby('Cleaning')[['ModA', 'ModB']].mean()
    st.write("Average Sensor Readings Before and After Cleaning:")
    st.dataframe(cleaning_effect)

# Conclusion
st.write("This dashboard allows you to explore solar radiation data interactively. Use the sidebar to filter data and explore insights.")
