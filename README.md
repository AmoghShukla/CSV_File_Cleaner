# 📂 CSV_File_Cleaner

A simple Python script to clean CSV files by removing duplicates and handling missing values.  
Built with **Python** and **pandas**.

---

## 🚀 Features
- Remove duplicate rows automatically  
- Handle missing values with different strategies:
  - Drop rows with missing values  
  - Fill missing values with `"Unknown"`  
  - Fill numeric columns with `mean` or `median`  
  - Fill missing values with `0`  

---

## 🛠 Installation
1. Clone this repository or download the script.
2. Install dependencies:
   ```bash
   pip install pandas

---

## ▶️ Usage

Import the function into your Python script or run directly:

import cleaner

# Clean CSV (drop missing values)
cleaner.clean_csv("data.csv", "cleaned_data.csv")

# Clean CSV (fill missing with mean)
cleaner.clean_csv("data.csv", "cleaned_data.csv", missing_strategy="mean")

# Clean CSV (fill missing with 'Unknown')
cleaner.clean_csv("data.csv", "cleaned_data.csv", missing_strategy="unknown")

