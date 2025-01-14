# Boxplot Visualization with Standard Deviation

This repository provides a Python script to generate a boxplot with optional standard deviation overlay based on enzyme activity or other experimental data. The script is flexible and parametrized to support different datasets.

## Features
- Dynamically loads data based on a specified filename.
- Generates boxplots with labeled outliers (stars).
- Adds error bars for standard deviation overlay.
- Supports multiple datasets with predefined metadata for titles and labels.

## Prerequisites
- **Python 3.x**
- **A virtual environment** (optional but recommended)

## Setup Instructions
### 1. Clone the Repository(this step can be skipped if you download the repository)
```bash
git clone https://github.com/your-repo-name.git
cd your-repo-name
```

### 2. Set up the Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

# How to run the Script
Place your dataset in the ./data/ directory. Ensure the file format is CSV.

Run the script with the file name (without .csv) as an argument:

```bash
python main.py <file_name>
```
Example:
```bash
python main.py ache_3
```
The script will generate a boxplot based on the dataset, with appropriate titles and labels.