import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.dpi'] = 300

# Load the data from the new Excel file
file_path = 'mean_scores.xlsx'
mean_scores = pd.read_excel(file_path, index_col=0)

# Define new answer and question names based on the previous data snippet
answer_names = {
    'Answer A': 'Chain of Thought',
    'Answer B': 'Tree of Thought',
    'Answer C': 'Algorithm of Thought',
    'Answer D': 'Graph of Thought'
}

question_names = {
    'q1': 'Mathematical Reasoning',
    'q2': 'Natural Language Understanding',
    'q3': 'Logical Deduction',
    'q4': 'Spatial Reasoning',
    'q5': 'Common Sense Reasoning'
}

# Update DataFrame with new answer and question names
mean_scores_renamed = mean_scores.rename(columns=answer_names, index=question_names)

# Prepare data for the new radar chart
labels = np.array(mean_scores_renamed.index)
num_vars = len(labels)

# Calculate angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Ensure the loop is closed by repeating the first value

# Plot
fig, ax = plt.subplots(figsize=(9, 7), subplot_kw=dict(polar=True))
plt.title("Comparison of Promoting Patterns' User Trust Across Different Cognitive Tasks", size=15, color='black', y=1.1)

# Draw one axe per variable + add labels with English descriptions
plt.xticks(angles[:-1], labels)

# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks([1,2,3,4,5], ["1","2","3","4","5"], color="grey", size=7)
plt.ylim(0,5)
ax.spines['polar'].set_visible(True)
ax.spines['polar'].set_color('grey')

# Plot each answer
for column in mean_scores_renamed.columns:
    values = mean_scores_renamed[column].values.flatten().tolist()
    values += values[:1]  # Ensure the loop is closed by repeating the first value
    ax.plot(angles, values, linewidth=1, linestyle='solid', label=column)
    ax.fill(angles, values, alpha=0.1)

plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

# Display the plot
plt.savefig('Radar.png')
plt.show()