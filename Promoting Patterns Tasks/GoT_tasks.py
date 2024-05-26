import utils
from SimpleParser import SimpleParser
from SimplePrompter import SimplePrompter
from graph_of_thoughts import controller, operations,prompter,parser

from language_models.chatgpt import ChatGPT

prompter = SimplePrompter()
parser = SimpleParser()

gop = operations.GraphOfOperations()
gop.append_operation(operations.Generate())
# Configure the Language Model (Assumes config.json is in the current directory with OpenAI API key)
initial_state = {
    "question": "If John is taller than Jake, and Jake is taller than Paul, who is the shortest."
}
lm = ChatGPT("config.json", model_name="chatgpt4")

# Create the Controller
ctrl = controller.Controller(
  lm,
  gop,
  prompter,
  parser,
  initial_state
  # The following dictionary is used to configure the initial thought state
)

# Run the Controller and generate the output graph
ctrl.run()
ctrl.output_graph("output.json")