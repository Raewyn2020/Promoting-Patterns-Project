import pandas as pd
from scipy.stats import ttest_ind

# Load the data
file_path = 'q2_new.xlsx'
data = pd.read_excel(file_path)

# Perform two-sample t-tests for each pair of answers
pairs = [('Answer A', 'Answer B'), ('Answer A', 'Answer C'), ('Answer A', 'Answer D'),
         ('Answer B', 'Answer C'), ('Answer B', 'Answer D'), ('Answer C', 'Answer D')]

results = {}

for pair in pairs:
    stat, p_value = ttest_ind(data[pair[0]], data[pair[1]])
    results[f"{pair[0]} vs {pair[1]}"] = {'t-statistic': stat, 'p-value': p_value}

results_df = pd.DataFrame(results).T

# Adjust the significance level for multiple comparisons (Bonferroni correction)
corrected_alpha = 0.05 / 4
results_df['Bonferroni Significant'] = results_df['p-value'] < corrected_alpha

print(results_df)
