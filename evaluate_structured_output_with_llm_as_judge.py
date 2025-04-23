from openevals.json import create_json_match_evaluator
from dotenv import load_dotenv

load_dotenv()

outputs = [
    {"a": "Mango, Bananas", "b": 2},
    {"a": "Apples", "b": 2, "c": [1,2,3]},
]
reference_outputs = [
    {"a": "Mango, Bananas", "b": 2},
    {"a": "Apples, Mango", "b": 2,"c":[1,2,3]},]

evaluator = create_json_match_evaluator(
    aggregator = "average",
    list_aggregator = 'average',
    model = 'openai:o3-mini',
    use_reasoning = True,
    rubric={"a":"Does the answer mention fruits correctly?"}
)

eval_result = evaluator(
    outputs=outputs, 
    reference_outputs= reference_outputs
)
print(eval_result)