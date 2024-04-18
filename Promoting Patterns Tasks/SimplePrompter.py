from graph_of_thoughts.prompter import Prompter
from typing import List, Dict, Union


class SimplePrompter(Prompter):
    def aggregation_prompt(self, state_dicts: List[Dict], **kwargs) -> str:
        # Implement your logic here
        return "Aggregation prompt based on the provided states."

    def generate_prompt(self, num_branches: int, **kwargs) -> str:
        # Implement your logic here
        question = kwargs.get('question', 'Default question?')
        return f"Generate {num_branches} answers for the following question: {question}"

    def improve_prompt(self, **kwargs) -> str:
        # Implement your logic here
        state = kwargs.get('state', 'Default state')
        return f"How can the following state be improved? {state}"

    def score_prompt(self, state_dicts: List[Dict], **kwargs) -> str:
        # Implement your logic here
        states = ', '.join([str(state) for state in state_dicts])
        return f"Please score the following states: {states}"

    def validation_prompt(self, **kwargs) -> str:
        # Implement your logic here
        statement = kwargs.get('statement', 'Default statement')
        return f"Is the following statement true or valid? {statement}"

