from openevals.json import create_json_match_evaluator

outputs = [
    {"a": "Mango, Bananas", "b": 2},
    {"a": "Apples", "b": 2, "c": [1,2,3]},
]
reference_outputs = [
    {"a": "Mango, Bananas", "b": 2},
    {"a": "Apples", "b": 2, "c": [1,2,3]},
]

evaluator = create_json_match_evaluator(aggregator="average", 
                                        list_aggregator = 'all')

eval_result = evaluator(outputs=outputs,reference_outputs=reference_outputs)
print("evaluation results are ", eval_result)

