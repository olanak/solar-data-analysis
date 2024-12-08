import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

# Load datasets
benin = pd.read_csv('data/benin-malanville.csv')
sierra_leone = pd.read_csv('data/sierraleone-bumbuna.csv')
togo = pd.read_csv('data/togo-dapaong_qc.csv')

# Add a column to identify the source
benin['Location'] = 'Benin-Malanville'
sierra_leone['Location'] = 'SierraLeone-Bumbuna'
togo['Location'] = 'Togo-Dapaong'

# Combine datasets
combined_df = pd.concat([benin, sierra_leone, togo], ignore_index=True)

# Drop unnecessary or entirely null columns
if 'Comments' in combined_df.columns:
    combined_df = combined_df.drop(columns=['Comments'])

# Convert Timestamp column to datetime
combined_df['Timestamp'] = pd.to_datetime(combined_df['Timestamp'])

# Save the combined dataset for future use
combined_df.to_csv('data/combined_solar_data.csv', index=False)

# Display dataset information
print("Combined Dataset Info:")
print(combined_df.info())

# Check for missing values
print("\nMissing Values by Column:")
print(combined_df.isnull().sum())

# Visualize GHI trends by location
print("\nVisualizing GHI Trends by Location...")
plt.figure(figsize=(10, 6))
for location in combined_df['Location'].unique():
    subset = combined_df[combined_df['Location'] == location]
    plt.plot(subset['Timestamp'], subset['GHI'], label=location)

plt.legend()
plt.title('GHI Trends by Location')
plt.xlabel('Timestamp')
plt.ylabel('GHI')
plt.show()

# Correlation analysis for each location
#print("\nGenerating Correlation Heatmaps by Location...")
#for location in combined_df['Location'].unique():
 #   subset = combined_df[combined_df['Location'] == location]
  #plt.figure(figsize=(8, 6))
   # sns.heatmap(subset.corr(), annot=True, cmap='coolwarm')
    #plt.title(f'Correlation Heatmap: {location}')
    #plt.show()

# Correlation analysis for each location
print("\nGenerating Correlation Heatmaps by Location...")
for location in combined_df['Location'].unique():
    subset = combined_df[combined_df['Location'] == location]
    numeric_subset = subset.select_dtypes(include=['float64', 'int64'])  # Select only numeric columns
    plt.figure(figsize=(8, 6))
    sns.heatmap(numeric_subset.corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title(f'Correlation Heatmap: {location}')
    plt.show()


# Outlier detection using Z-scores
print("\nDetecting Outliers using Z-Scores...")
for location in combined_df['Location'].unique():
    subset = combined_df[combined_df['Location'] == location]
    subset['z_score_GHI'] = zscore(subset['GHI'])
    outliers = subset[subset['z_score_GHI'] > 3]
    print(f"{location} - Outliers:")
    print(outliers)

# Evaluate the impact of cleaning
print("\nEvaluating Cleaning Impact on Sensor Readings...")
for location in combined_df['Location'].unique():
    subset = combined_df[combined_df['Location'] == location]
    print(f"{location} - Cleaning Impact on Sensor Readings")
    print(subset.groupby('Cleaning')[['ModA', 'ModB']].mean())

# Summary statistics and data distribution
print("\nSummary Statistics for Combined Data:")
print(combined_df.describe())

print("\nGenerating Histograms for Key Variables...")
variables = ['GHI', 'DNI', 'DHI', 'WS', 'ModA', 'ModB']
for var in variables:
    plt.figure()
    combined_df[var].hist(bins=20)
    plt.title(f'Histogram of {var}')
    plt.xlabel(var)
    plt.ylabel('Frequency')
    plt.show()

print("EDA Complete!")
