from openevals.llm import create_llm_as_judge
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()


class output_format(BaseModel):
    score: bool = Field(description="True if the message is polite, False otherwise")
    comment: str = Field(description="brief explanation")
    tone_category: str = Field(description="Choose from [polite, neutral, rude]")


prompt = """You are a tone evaluator for customer support conversations.
Judge the tone of the following customer message.

<message>
{message}
</message>

"""

evaluator = create_llm_as_judge(
    prompt=prompt, 
    model = 'openai:o3-mini',
    output_schema=output_format,
    feedback_key="custom_schema_test"
)

eval_result = evaluator(message="Hi there, I’m having a small issue with my order. Could you please help me resolve it?")
print(eval_result)