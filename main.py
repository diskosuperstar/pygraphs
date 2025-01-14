import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sys

# Dictionary to store file-specific metadata
file_metadata = {
    "ache_3": {"title": "Specific enzyme activity of acetylcholinesterase (AChE)", "ylabel": "Values (nM/min*mg)"},
    "glave_3": {"title": "Tadpole Head Length", "ylabel": "Values (mm)"},
    "gst_3": {"title": "Specific Enzyme Activity of Glutathione S-transferase", "ylabel": "Values (nM/min*mg)"},
    "lip_3": {"title": "Total Lipid Concentration", "ylabel": "Values (mg/ml)"},
    "mase_3": {"title": "Tadpole Mass", "ylabel": "Values (g)"},
    "prot_3": {"title": "Total Protein Concentration", "ylabel": "Values (mg/μl)"},  # μl = microliters
    "rep_3": {"title": "Tadpole Tail Length", "ylabel": "Values (mm)"},
    "uh_3": {"title": "Total Carbohydrate Concentration", "ylabel": "Values (μg/ml)"}  # μg = micrograms
}

# Get file name as an input parameter
if len(sys.argv) < 2:
    print("Usage: python script.py <file_name>")
    sys.exit(1)

name = sys.argv[1]

# Get metadata for the file
if name not in file_metadata:
    print(f"File metadata for '{name}' not found.")
    sys.exit(1)

file_path = f"./data/{name}.csv"
title = file_metadata[name]["title"]
ylabel = file_metadata[name]["ylabel"]

# Load the dataset
df = pd.read_csv(file_path)

# Reshape the dataset into long format
df_long = df.melt(var_name="Group", value_name="Values")

# Create the boxplot with the updated approach
plt.figure(figsize=(10, 6))
ax = sns.boxplot(data=df_long, x="Group", y="Values", 
                 hue="Group",  # Assign `x` to `hue`
                 dodge=False,  # Prevent separating boxes by hue
                 palette=["green", "orange", "lightblue"], 
                 showmeans=True, 
                 meanprops={"marker": "o", "markerfacecolor": "black"},
                 flierprops=dict(marker='*', color='black', alpha=0.8))

# Calculate the standard deviation for each group
std_dev = df_long.groupby('Group')['Values'].std()

# Overlay standard deviation as error bars
for i, group in enumerate(df_long['Group'].unique()):
    group_data = df_long[df_long['Group'] == group]
    mean = group_data['Values'].mean()
    ax.errorbar(x=i, y=mean, yerr=std_dev[group], fmt='o', color='red', capsize=5, alpha=0.7)

# Add labels and title
ax.set_title(title, fontsize=14)
ax.set_xlabel("Group", fontsize=12)
ax.set_ylabel(ylabel, fontsize=12)

# Show the plot
plt.tight_layout()
plt.show()
