import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# ==========================
# DATA LOADING
# ==========================

print("Loading Dataset...")

df = pd.read_csv("dataset.csv")

print("\nDataset Loaded Successfully!")
print(df.head())

# ==========================
# DATA CLEANING
# ==========================

print("\n========== DATA CLEANING ==========")

# Missing Values Before Cleaning
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# Fill Missing Values
numeric_cols = df.select_dtypes(include='number').columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

# Remove Duplicates
duplicates = df.duplicated().sum()
print(f"\nDuplicate Rows Found: {duplicates}")

df = df.drop_duplicates()

# Missing Values After Cleaning
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nData Cleaning Completed Successfully!")

# ==========================
# DATASET INFORMATION
# ==========================

print("\n========== DATASET INFO ==========")

print("\nShape of Dataset:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nStatistical Summary:")
print(df.describe())

# ==========================
# VISUALIZATION
# ==========================

print("\nGenerating Graphs...")

# Top 10 Happiest Countries
top10 = df.sort_values(by='Score', ascending=False).head(10)

plt.figure(figsize=(10,5))
sns.barplot(x='Score', y='Country or region', data=top10)
plt.title("Top 10 Happiest Countries")
plt.tight_layout()
plt.show()

# GDP vs Happiness Score
plt.figure(figsize=(8,5))
sns.scatterplot(x='GDP per capita', y='Score', data=df)
plt.title("GDP vs Happiness Score")
plt.tight_layout()
plt.show()

# Social Support vs Happiness Score
plt.figure(figsize=(8,5))
sns.scatterplot(x='Social support', y='Score', data=df)
plt.title("Social Support vs Happiness Score")
plt.tight_layout()
plt.show()

# Correlation Heatmap
plt.figure(figsize=(10,6))
sns.heatmap(
    df.select_dtypes(include='number').corr(),
    annot=True
)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

print("\nGraphs Generated Successfully!")

# ==========================
# FINDINGS
# ==========================

highest_country = df.loc[df['Score'].idxmax(), 'Country or region']
lowest_country = df.loc[df['Score'].idxmin(), 'Country or region']

print("\n========== FINDINGS ==========")

print(f"\nHappiest Country : {highest_country}")
print(f"Least Happy Country : {lowest_country}")

print("\nObservation 1:")
print("Countries with higher GDP generally have higher happiness scores.")

print("\nObservation 2:")
print("Social support has a positive relationship with happiness.")

print("\nObservation 3:")
print("Life expectancy contributes significantly to happiness levels.")

# ==========================
# STREAMLIT DASHBOARD
# ==========================

st.title("🌍 World Happiness Report Dashboard")

st.header("Dataset Preview")
st.dataframe(df.head())

st.header("Dataset Shape")
st.write(df.shape)

st.header("Top 10 Happiest Countries")
st.bar_chart(top10.set_index('Country or region')['Score'])

st.header("Findings")

st.write(f"✅ Happiest Country: {highest_country}")
st.write(f"✅ Least Happy Country: {lowest_country}")

st.write("✅ Higher GDP is associated with higher happiness.")
st.write("✅ Strong social support improves happiness.")
st.write("✅ Healthy life expectancy impacts happiness positively.")

st.success("Data Cleaning, Visualization and Analysis Completed Successfully!")