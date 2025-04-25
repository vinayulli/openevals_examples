from openevals.llm import create_llm_as_judge
from openevals.prompts import RAG_RETRIEVAL_RELEVANCE_PROMPT

evaluator = create_llm_as_judge(
    prompt=RAG_RETRIEVAL_RELEVANCE_PROMPT,
    feedback_key="retrieval_relevance",
    model="openai:o3-mini",
)

# test case 1 
inputs = {
    "question": "Where was the first president of FoobarLand born?",
}

context = {
    "documents": [
        "FoobarLand is a new country located on the dark side of the moon",
        "Space dolphins are native to FoobarLand",
        "FoobarLand is a constitutional democracy whose first president was Bagatur Askaryan",
        "The current weather in FoobarLand is 80 degrees and clear.",
    ],
}

eval_result = evaluator(
    inputs=inputs,
    context=context,
)

print("test case 1",eval_result)

# test case 2 

inputs = {
    "question": "What are the main exports of FoobarLand?",
}

context = {
    "documents": [
        "FoobarLand is known for its lunar-based architecture and eco-domes.",
        "It has a strong emphasis on space education and robotic research.",
        "A key tourist attraction in FoobarLand is the zero-gravity amphitheater.",
        "FoobarLand is a constitutional democracy whose first president was Bagatur Askaryan.",
    ],
}

eval_result = evaluator(
    inputs=inputs,
    context=context,
)

print("test case 2", eval_result)

# test case 3

inputs = {
    "question": "What are the main exports of FoobarLand?",
}

context = {
    "documents": [
        "FoobarLand exports lunar minerals such as Helium-3 and rare earth elements used in advanced electronics.",
        "The space-grown algae from FoobarLand is a major export for pharmaceutical companies on Earth.",
        "FoobarLands robotic manufacturing units also export precision space equipment to Earth-based agencies.",
        "Exports account for 60% of FoobarLands GDP, primarily focused on space tech and bioengineering products.",
    ],
}

eval_result = evaluator(
    inputs=inputs,
    context=context,
)

print("test case 3", eval_result)

