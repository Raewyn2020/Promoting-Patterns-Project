# Setup Guide for Thought Process Frameworks

This guide provides detailed instructions for setting up and using the Tree of Thought (ToT), Algorithm of Thought (AoT), and Graph of Thought (GoT) frameworks. Each framework requires a specific configuration to function correctly with the OpenAI GPT-4 model.

## Prerequisites
Before you begin, ensure you have:
- Python 3.9 installed.
- Access to modify and set environment variables on your system.

## General Setup
- **OpenAI API Key**: Ensure that your OpenAI API key is set up and available as an environment variable `OPENAI_API_KEY`.

## Tree of Thought (ToT)
### Setup Instructions
1. **Install Package**:
   - Run `pip install tree-of-thoughts-llm`.
2. **Prepare the Environment**:
   - Store your OpenAI API key in the environment variable `OPENAI_API_KEY`.
3. **Configure Questions**:
   - Add your questions to `/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/tot/data/text/data_100_random_text.txt`.
4. **Run the Script**:
   - Execute `ToT_tasks.py` to process the questions using the ToT framework.
5. **Package Version**:
   - Ensure that the version of the `openai` package is `0.28.1`.

### GitHub Reference
- [https://github.com/princeton-nlp/tree-of-thought-llm](#) (tree-of-thought-llm GitHub)

## Algorithm of Thought (AoT)
### Setup Instructions
1. **Install Package**:
   - Run `pip install aot-x`.
2. **Modify API Model Settings**:
   - Locate the file `/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/aot/openai.py`.
   - Find the code snippet handling the API model setting:
     ```python
     else:
         self.api_model = "gpt-3.5-turbo"
         print(f"Using api_model {self.api_model}")
     ```
   - Modify this snippet to use the GPT-4 model by changing it to:
     ```python
     else:
         self.api_model = "gpt-4"
         print(f'Using api_model {self.api_model}')
     ```
     This change ensures that all experiments use the ChatGPT-4 model, maintaining consistency across different runs.
3. **Run the Script**:
   - Execute `AoT_tasks.py`. Input your question at the designated `task =` location in the script.
   - Configure your OpenAI API key on line 13 as `openai_api_key="your-api-key"`.
4. **Package Version**:
   - The `openai` package version should be `0.28.1`.

### GitHub Reference
- [https://github.com/kyegomez/Algorithm-Of-Thoughts/tree/main](#) (Algorithm-Of-Thoughts GitHub)

## Graph of Thought (GoT)
### Setup Instructions
1. **Install Package**:
   - Run `pip install graph_of_thoughts`.
2. **Configure API Key**:
   - Set the OpenAI API key on line 20 as `"api_key": "your-api-key"` in `config.json`.
3. **Run the Script**:
   - Execute `GoT_tasks.py` with your question in the `initial_state =` field. Results are output to `output.json`.
4. **Package Version**:
   - The `openai` package version should be `1.25.0`.

### GitHub Reference
- [https://github.com/spcl/graph-of-thoughts](#) (Graph-of-Thoughts GitHub)

## Notes
- The version differences in the `openai` package across different frameworks are due to updates in API interfaces; however, these do not affect the underlying models which remain consistent across all implementations.

## Troubleshooting
For any issues related to the setup or execution, check the configuration settings, verify the API key, and ensure the correct versions of the packages are installed. If problems persist, consider revisiting the GitHub repositories for additional troubleshooting tips.

