from aot.main import AoT

task = """
Is it safe to go outside during a thunderstorm?
"""


dfs = AoT(
    num_thoughts=2,
    max_steps=10, 
    value_threshold=1,
    initial_prompt=task,
    openai_api_key="your-key"
)

result = dfs.solve()
print(result)