import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import seaborn as sns
plt.rcParams['figure.dpi'] = 300
import pandas as pd


file_path = 'Users\' tasks scores.xlsx'  # Update the path
data = pd.read_excel(file_path)
# Set the style of seaborn for better aesthetics
sns.set(style="whitegrid")

# Prepare the data for seaborn's boxplot by melting it into a long format
# Make sure to adjust 'value_vars' if your thought models are named differently
df_melted = data.melt(id_vars=['Task'], var_name='Thought Model', value_name='Score',
                      value_vars=['Chain of Thought', 'Tree of Thought', 'Algorithm of Thought', 'Graph of Thought'])

# Plotting the boxplot with seaborn
plt.figure(figsize=(12, 8))  # Adjust the figure size if needed to accommodate the rotated labels
boxplot = sns.boxplot(x='Task', y='Score', hue='Thought Model', data=df_melted, palette='Set3')

# Adding titles and labels
boxplot.set_title('Boxplot of Distribution of User Trust Scores by Thought Models Across Different Tasks', fontsize=16)
boxplot.set_xlabel('Task', fontsize=12)
boxplot.set_ylabel('Score', fontsize=12)
plt.legend(title='Thought Model', loc='upper left')

# Rotate x-axis labels to prevent overlap
plt.xticks(rotation=45, ha='right')  # Rotate labels and align them to the right for better legibility

plt.tight_layout()  # This will adjust subplot parameters to give some padding and prevent overlap

plt.savefig('Boxplot.png')
plt.show()
