from openevals.llm import create_llm_as_judge
from openevals.prompts import CORRECTNESS_PROMPT
from dotenv import load_dotenv

load_dotenv()


evaluator = create_llm_as_judge(
    prompt=CORRECTNESS_PROMPT, 
    feedback_key="correctness",
    model = 'openai:o3-mini')


# test case  1 
input = "What is the boiling point of water at sea level?"
output = "Water boils at 100 degrees Celsius at sea level."
reference_output = "Water boils at 100°C (212°F) at standard atmospheric pressure."

eval_result = evaluator(inputs=input,outputs=output,reference_outputs=reference_output)
print("test case 1", eval_result)

# test case 2 
input = "What is the capital of Australia?"
output = "Sydney is the capital of Australia." 
reference_output = "Canberra is the capital city of Australia."
eval_result = evaluator(inputs=input, outputs=output, reference_outputs=reference_output)
print("test case 2", eval_result)