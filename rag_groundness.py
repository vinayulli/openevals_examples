from openevals.llm import create_llm_as_judge
from openevals.prompts import RAG_GROUNDEDNESS_PROMPT

evaluator = create_llm_as_judge(
    prompt=RAG_GROUNDEDNESS_PROMPT,
    feedback_key="groundedness_rag",
    model="openai:o3-mini",
)

context = {
    "documents": [
        "FoobarLand is a new country located on the dark side of the moon",
        "Space dolphins are native to FoobarLand",
        "FoobarLand is a constitutional democracy whose first president was Bagatur Askaryan",
        "The current weather in FoobarLand is 80 degrees and clear."
    ],
}

outputs = {
    "answer": "The first president of FoobarLand was Bagatur Askaryan.",
}

eval_result = evaluator(
    context=context,
    outputs=outputs,
)

print("test-case- 1 ",eval_result)

# test-case -2 

context = {
    "documents": [
        "FoobarLand is located on the dark side of the moon and has a population of 50,000 lunar citizens.",
        "The country has established a space-based agriculture system to sustain its residents.",
        "A unique feature of FoobarLand is its underground thermal energy network powering the lunar colonies.",
        "Its governance structure follows a lunar-adapted democratic model, with local councils elected every two years."
    ],
}

outputs = {
    "answer": "FoobarLand's democracy is modeled after Switzerland's direct democracy, adapted for lunar governance."
}

eval_result = evaluator(
    context=context,
    outputs=outputs,
)

print("test-case- 2 ", eval_result)