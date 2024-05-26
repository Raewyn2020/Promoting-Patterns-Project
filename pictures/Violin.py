import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams['figure.dpi'] = 300
file_path = 'Users\' tasks scores.xlsx'  # Update the path
data = pd.read_excel(file_path)

melted_data = data.melt(id_vars=['User', 'Task'], var_name='Model', value_name='Score')

plt.figure(figsize=(14, 8))
sns.violinplot(x='Task', y='Score', hue='Model', data=melted_data, palette='Set3')
plt.title('User Trust Score Distribution Across Different Promoting Patterns by Different Cognitive Tasks')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('Violin.png')
plt.show()

