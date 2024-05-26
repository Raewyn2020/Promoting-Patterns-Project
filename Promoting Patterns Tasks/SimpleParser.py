from graph_of_thoughts.parser import Parser
from typing import List, Dict, Union

class SimpleParser(Parser):
    def parse_aggregation_answer(self, states: List[Dict], texts: List[str]) -> Union[Dict, List[Dict]]:
        # Implement your logic here
        # Example implementation
        return {"aggregated": texts[-1]}

    def parse_improve_answer(self, state: Dict, texts: List[str]) -> Dict:
        # Implement your logic here
        # Example implementation
        return {"improved": texts[-1]}

    def parse_generate_answer(self, state: Dict, texts: List[str]) -> List[Dict]:
        # Implement your logic here
        # Example implementation
        return [{"generated": text} for text in texts]

    def parse_validation_answer(self, state: Dict, texts: List[str]) -> bool:
        # Implement your logic here
        # Example implementation
        return "true" in texts[-1].lower()

    def parse_score_answer(self, states: List[Dict], texts: List[str]) -> List[float]:
        # Implement your logic here
        # Example implementation
        return [float(text) for text in texts]


