from openevals.llm import create_llm_as_judge
from openevals.prompts import CONCISENESS_PROMPT
from dotenv import load_dotenv
load_dotenv()
conciness_evaluator = create_llm_as_judge(
    prompt=CONCISENESS_PROMPT,
    feedback_key="conciseness",
    model= 'openai:o3-mini'
)


# test case 1 
input = "How is the weather in San Francisco?"
output = "Thanks for asking! The current weather in San Francisco is sunny and 90 degrees"
eval_result = conciness_evaluator(inputs=input, outputs=output)
print("test case 1", eval_result)

# test case 2
input = "How is the weather in San Francisco?" 
output = " The current weather is sunny and 90 degrees"
eval_result = conciness_evaluator(inputs=input, outputs=output)
print("test case 2", eval_result)