from openevals.llm import create_llm_as_judge
from openevals.prompts import CORRECTNESS_PROMPT
from dotenv import load_dotenv

load_dotenv()

evaluator = create_llm_as_judge(
    prompt = CORRECTNESS_PROMPT,
    continuous= True,
    model = 'openai:o3-mini'
)

# test case 1

input = "What is the boiling point of water at sea level?"
output = "Water boils at around 99 degrees Celsius at sea level."
reference_output = "Water boils at 100°C (212°F) at standard atmospheric pressure."
eval_result = evaluator(inputs=input, outputs=output, reference_outputs=reference_output)
print("test case 1",eval_result)

# test case 2 
input = "What is the boiling point of water at sea level?"
output = "Water boils at around 100 degrees Celsius at sea level."
reference_output = "Water boils at 100°C (212°F) at standard atmospheric pressure."
eval_result = evaluator(inputs=input, outputs=output, reference_outputs=reference_output)
print("test case 2   ",eval_result)

