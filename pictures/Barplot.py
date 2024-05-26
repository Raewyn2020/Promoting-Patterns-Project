import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['figure.dpi'] = 300
# Load the data from the Excel file
file_path = 'Users\' tasks scores.xlsx'  # Update the path
data = pd.read_excel(file_path)

# Group the data by task and calculate mean and standard deviation for each thought model
grouped_data = data.groupby('Task').agg(['mean', 'std'])

# Define a color palette
# colors = ['#BDAEE8', '#AFD1FA', '#D1E3D8', '#F6E9CB']
colors = ['#8dd3c7', '#ffffb3', '#bebada', '#fb8072']

# Set up the bar chart
fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.15
indices = np.arange(len(grouped_data))

# Plot bars for each thought model
for i, model in enumerate(['Chain of Thought', 'Tree of Thought', 'Algorithm of Thought', 'Graph of Thought']):
    r = [x + bar_width * i for x in indices]
    mean_scores = grouped_data[(model, 'mean')]
    std_devs = grouped_data[(model, 'std')]
    ax.bar(r, mean_scores, color=colors[i], width=bar_width, label=model, yerr=std_devs, capsize=5)

# Add labels, title, and legend
ax.set_xlabel('Task', fontsize=14)
ax.set_ylabel('Score', fontsize=14)
ax.set_title('Barplot of User Trust Scores Across Different Thought Models by Tasks', fontsize=16)
ax.set_xticks([r + bar_width * 1.5 for r in range(len(grouped_data))])
ax.set_xticklabels(grouped_data.index, rotation=45)
ax.legend(fontsize=12)

# Improve layout and aesthetics
plt.tight_layout()
plt.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)
plt.savefig('Barplot.png')
plt.show()
