from openevals.llm import create_llm_as_judge
from openevals.prompts import RAG_HELPFULNESS_PROMPT

evaluator = create_llm_as_judge(
    prompt=RAG_HELPFULNESS_PROMPT,
    feedback_key="helpfulness_rag",
    model="openai:o3-mini",
)


# test case 1 
inputs = {
    "question": "Where was the first president of FoobarLand born?",
}

outputs = {
    "answer": "The first president of FoobarLand was Bagatur Askaryan.",
}

eval_result = evaluator(
  inputs=inputs,
  outputs=outputs,
)

print("test case 1",eval_result)

# test case 2 

inputs = {
    "question": "How many clients do we have in our database?"
}

outputs = {
    "answer": " Amazon, Google and Meta are our clients"
}

eval_result = evaluator(
  inputs=inputs,
  outputs=outputs,
)

print("test case 2",eval_result)

# test case 3

inputs = {
    "question": "How many clients do we have in our database?"
}

outputs = {
    "answer": " We have ten clients"
}

eval_result = evaluator(
  inputs=inputs,
  outputs=outputs,
)

print("test case 3",eval_result)

