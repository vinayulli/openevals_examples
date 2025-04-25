from openevals.llm import create_llm_as_judge
from dotenv import load_dotenv

load_dotenv()

custom_prompt = """ You are a professional communication reviewer.
Evaluate the following message for tone, politeness, and professionalism.
The ideal message:
- Is friendly and polite
- Avoids rude or abrupt phrases
- Has a professional and respectful tone
Given this message:
"{outputs}"
"""

evaluator = create_llm_as_judge(
    prompt = custom_prompt,
    model= 'openai:o3-mini',
    feedback_key="custom"
)

# test case 1
output = "Thank you for reaching out. We appreciate your patience and are working on resolving your issue promptly."
eval_result = evaluator(outputs=output)
print("test case 1", eval_result)

# test case 2
output = "Stop emailing us again and again. We already told you it’s not our problem."
eval_result = evaluator(outputs=output)
print("test case 2", eval_result)
