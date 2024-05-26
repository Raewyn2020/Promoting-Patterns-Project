# ANOVA test for each of the q1(task1) to q5(task5) tables
import pandas as pd
from scipy.stats import f_oneway
anova_results = {}

# Perform ANOVA for each table
for i in range(1, 6):
    # Load each table
    table_data = pd.read_excel(f'q{i}.xlsx')
    # Perform the ANOVA test
    result = f_oneway(table_data['Answer A'], table_data['Answer B'], table_data['Answer C'], table_data['Answer D'])
    # Store the result
    anova_results[f'q{i}'] = {
        'F-value': result.statistic,
        'p-value': float(result.pvalue)

    }
print(anova_results)