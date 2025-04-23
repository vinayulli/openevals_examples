from openevals.llm import create_llm_as_judge
from openevals.prompts import CORRECTNESS_PROMPT
from dotenv import load_dotenv

load_dotenv()


system_prompt  = "You are a strict legal reviewer. Any answer not citing the relevant IPC or IT Act section must be marked as incorrect."

evaluator = create_llm_as_judge( 
    prompt= CORRECTNESS_PROMPT,
    model = 'openai:o3-mini',
    system=system_prompt
)


# test-case - 1 
input = "Can someone be punished for cyberbullying under Indian law?"
output = "Yes, cyberbullying is punishable under IT Act."
reference_output = "Yes, under Section 66A of the Information Technology Act, cyberbullying is punishable."
eval_result = evaluator(inputs=input, outputs=output, reference_outputs=reference_output)
print("test-case-1   ", eval_result)

# test-cass - 2 
input = "Can someone be punished for sending threatening messages online under Indian law?"
output = "Yes, under Section 66A of the Information Technology Act, sending offensive or threatening messages through communication service is punishable."
reference_output = "Yes, sending threatening or offensive messages is punishable under Section 66A of the IT Act."
eval_result = evaluator(inputs=input,outputs=output, reference_outputs=reference_output)
print("test-case-2  ", eval_result)