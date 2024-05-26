import pandas as pd

task_mapping = {
    'Q1': 'Mathematical Reasoning',
    'Q2': 'Natural Language Understanding',
    'Q3': 'Logical Deduction',
    'Q4': 'Spatial Reasoning',
    'Q5': 'Common Sense Reasoning'
}

method_mapping = {
    'Answer A': 'Chain of Thought (CoT)',
    'Answer B': 'Tree of Thought (ToT)',
    'Answer C': 'Algorithm of Thought (AoT)',
    'Answer D': 'Graph of Thought (GoT)'
}

def load_and_transform_data(file_path):
    data = pd.read_excel(file_path)
    data['Task'] = data['Question_Answer'].str.split().str[0].map(task_mapping)
    data['Method'] = data['Question_Answer'].str.extract('(Answer [A-D])')[0].map(method_mapping)
    return data

def extract_themes(data, task, method):
    filtered_data = data[(data['Task'] == task) & (data['Method'] == method)]
    all_words = filtered_data['Feedback'].str.lower().str.replace('[^\w\s]', '', regex=True).str.split(expand=True).stack()
    common_words = set()
    with open('stopwords.txt', 'r', encoding='utf-8') as file:
        for line in file:
            common_words.add(line.strip())
    meaningful_words = all_words[~all_words.isin(common_words)].value_counts()
    return meaningful_words

file_path = 'final_open_ended_feedback.xlsx'
data = load_and_transform_data(file_path)

unique_keywords = set()

for task, task_name in task_mapping.items():
    for method, method_name in method_mapping.items():
        themes = extract_themes(data, task_name, method_name)
        unique_keywords.update(themes.index)

print("All unique keywords across all tasks and methods:")
print(unique_keywords)
f = open("keywords.txt", "w")
for i in unique_keywords:
    print(i, file=f)

